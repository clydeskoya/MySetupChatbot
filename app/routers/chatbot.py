from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..models.query_model import query_model

router = APIRouter()

class Query(BaseModel):
    question: str

@router.post("/ask")
def ask_question(query: Query):
    try:
        answer = query_model(query.question)
        return {"question": query.question, "answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
