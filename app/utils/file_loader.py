import json
from fastapi import UploadFile
from langchain.document_loaders import TextLoader, PyPDFLoader
from app.exceptions.custom_exceptions import BadRequestException

def load_questions(questions_file: UploadFile):
    if questions_file.content_type != 'application/json':
        raise BadRequestException("Questions file must be a JSON file.")
    questions_content = questions_file.file.read().decode('utf-8')
    questions = json.loads(questions_content)
    return questions

def load_document(document_file: UploadFile):
    if document_file.content_type == 'application/pdf':
        loader = PyPDFLoader(document_file.file)
    elif document_file.content_type == 'application/json':
        loader = TextLoader(document_file.file.read().decode())
    else:
        raise BadRequestException("Document file must be a PDF or JSON file.")
    return loader.load()
