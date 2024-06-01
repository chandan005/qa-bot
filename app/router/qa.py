from fastapi import APIRouter, UploadFile, File
from app.schema.qa import QuestionAnswerResponse
from app.utils.file_loader import load_questions, load_document
from app.service.qa_service import get_answers

router = APIRouter()

@router.post("/answer-questions/", response_model=QuestionAnswerResponse)
async def answer_questions(questions_file: UploadFile = File(...), document_file: UploadFile = File(...)):
    questions = load_questions(questions_file)
    documents = load_document(document_file)
    answers = get_answers(documents, questions['questions'])
    return QuestionAnswerResponse(answers=answers)
