from fastapi import FastAPI
from app.api.upload import router as upload_router
from app.api.query import router as query_router
from app.api.documents import router as documents_router

app = FastAPI()
app.include_router(upload_router)
app.include_router(query_router)
app.include_router(documents_router)

@app.get("/")
def home():
    return {"message": "RAG API Running"}

