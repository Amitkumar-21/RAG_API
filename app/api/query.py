from fastapi import APIRouter
from pydantic import BaseModel
from app.rag.retriever import retrieve_chunks
from app.rag.generator import generate_answer

router = APIRouter()

class QueryRequest(BaseModel):
    question: str

@router.post("/query")
def query_documents(request: QueryRequest):
    retrieved_chunks = retrieve_chunks(
        request.question
    )
    answer = generate_answer(
        request.question,
        retrieved_chunks
    )
    return {
        "question": request.question,
        "answer": answer,
        "retrieved_chunks": retrieved_chunks
    }