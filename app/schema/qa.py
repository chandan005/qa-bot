from typing import List
from pydantic import BaseModel

class QuestionAnswerPair(BaseModel):
    question: str
    answer: str

class QuestionAnswerResponse(BaseModel):
    answers: List[QuestionAnswerPair]
