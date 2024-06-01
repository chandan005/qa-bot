
from typing import List
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain.chains import RetrievalQA
from app.schema.qa import QuestionAnswerPair
from app.config.config import settings

def extract_pdf(file_path: str) -> List[str]:
    loader = PyPDFLoader(file_path=file_path)
    docs = loader.load()
    return docs

def split_doc(docs: str) -> any:
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1500,chunk_overlap = 150)
    splits = text_splitter.split_documents(docs)
    return splits

def get_answers(docs: str, questions: List[str]) -> List[QuestionAnswerPair]:
    llm = ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=settings.OPENAI_KEY)
    documents = split_doc(docs=docs)
    embeddings = OpenAIEmbeddings(openai_api_key=settings.OPENAI_KEY)

    persist_directory = 'docs/chroma/'

    # Create the vector store
    vectordb = Chroma.from_documents(documents=documents, embedding=embeddings, persist_directory=persist_directory)
    qa_chain = RetrievalQA.from_chain_type(llm, retriever=vectordb.as_retriever())

    answers = []
    for question in questions:
        print('Question', question)
        result = qa_chain.invoke({"query": question})
        answers.append(QuestionAnswerPair(question=question, answer=result.get('result')))
        # embedding = chain.embed_question(question)
        # similar_docs = pinecone_client.search(embedding)
        # similar_documents = [{"page_content": doc.metadata['text']} for doc in similar_docs]
        # answer = chain.run(input_documents=similar_documents, question=question)
        # answers.append(QuestionAnswerPair(question=question, answer=answer))

    return answers
