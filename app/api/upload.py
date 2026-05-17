from fastapi import APIRouter, UploadFile, File
from app.services.pdf_service import extract_text_from_pdf
from app.rag.chunker import chunk_text
from app.rag.embedder import generate_embedding
from app.db.vector_store import store_chunks
from app.services.pdf_service import (extract_text_from_pdf,get_pdf_page_count)
from app.db.metadata_db import save_document_metadata
from app.db.metadata_db import (save_document_metadata,get_document_count)
from fastapi import HTTPException
import os

os.makedirs("data/uploads", exist_ok=True)
os.makedirs("data/chroma", exist_ok=True)
router = APIRouter()
#Folder where pdfs will be stored
UPLOAD_DIR = "data/uploads"
@router.post("/upload")  #endpoint
async def upload_file(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)
    document_count = get_document_count()
    if document_count >= 20:
        raise HTTPException(
        status_code=400,
        detail="Maximum 20 documents allowed"
    )
    if not file.filename.endswith(".pdf"):
        raise HTTPException(
        status_code=400,
        detail="Only PDF files are allowed"
    )
    

    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)
    
    extracted_text = extract_text_from_pdf(file_path)
    chunks = chunk_text(extracted_text)
    page_count = get_pdf_page_count(file_path)
    if page_count > 1000:
        raise HTTPException(
        status_code=400,
        detail="PDF exceeds 1000 page limit"
    )
    store_chunks(chunks,file.filename,generate_embedding)
    save_document_metadata(file.filename,page_count,len(chunks)) 
    
    return {
        "message": "File uploaded successfully",
        "filename": file.filename,
        "total_chunks": len(chunks),
        "first_chunk_preview": chunks[0][:300]
    }