from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.schema import Document
from app.schemas.qa import QuestionAnswerPair
from app.vector_db.milvus_client import MilvusClient

milvus_client = MilvusClient()

def get_answers(documents: list[Document], questions: list[str]) -> list[QuestionAnswerPair]:
    llm = OpenAI()
    chain = load_qa_chain(llm, chain_type="stuff")

    # Insert document embeddings into Milvus
    for doc in documents:
        embedding = chain.embed_document(doc)
        milvus_client.insert_embeddings([(doc.id, embedding)])

    answers = []
    for question in questions:
        embedding = chain.embed_question(question)
        similar_docs = milvus_client.search(embedding)
        answer = chain.run(input_documents=[Document(id=doc.id, text=doc.text) for doc in similar_docs], question=question)
        answers.append(QuestionAnswerPair(question=question, answer=answer))

    return answers
