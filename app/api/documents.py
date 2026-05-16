from fastapi import APIRouter

from app.db.metadata_db import get_all_documents
router = APIRouter()
@router.get("/documents")
def get_documents():
    documents = get_all_documents()
    return {
        "documents": documents
    }