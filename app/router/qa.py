import json
import tempfile
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.schema.qa import QuestionAnswerResponse
from app.service.qa_service import get_answers, extract_pdf

router = APIRouter()

@router.post("/qa", response_model=QuestionAnswerResponse)
async def qa_endpoint(questions_file: UploadFile = File(...), document_file: UploadFile = File(...)):
    try:
        questions_content = await questions_file.read()
        questions = json.loads(questions_content)
        questions_list = [q['content'] for q in questions]

        if document_file.filename.endswith('.pdf'):
            with tempfile.NamedTemporaryFile(delete=False) as temp_pdf:
                temp_pdf.write(await document_file.read())
                extracted_pdf_text = extract_pdf(temp_pdf.name)
        else:
            raise HTTPException(status_code=400, detail="Unsupported document file type")

        answers = get_answers(extracted_pdf_text, questions_list)
        return QuestionAnswerResponse(answers=answers)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
