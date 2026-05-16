# RAG Pipeline

## Overview

RAG Pipeline is a Dockerized Retrieval-Augmented Generation (RAG) backend built using FastAPI, Gemini API, and ChromaDB.

The application allows users to:

* Upload PDF documents
* Generate embeddings for semantic search
* Store embeddings in ChromaDB
* Ask questions based on uploaded documents
* Retrieve relevant chunks and generate answers using Gemini

---

# Tech Stack

* FastAPI
* Gemini API
* ChromaDB
* SQLite
* Docker
* Pytest
* tiktoken
* pypdf

---

# Project Structure

```text
Panscience/
│
├── app/                 # Main backend code
├── data/                # Runtime storage
├── tests/               # Automated tests
├── pansc/               # Virtual environment
│
├── Dockerfile           # Docker image setup
├── docker-compose.yml   # Docker Compose configuration
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variable template
├── .gitignore           # Git ignore rules
└── .dockerignore        # Docker ignore rules
```

---

# Important Folders

## app/

Contains the main backend application.

* `api/` → API routes
* `rag/` → chunking, embeddings, retrieval, generation
* `db/` → SQLite metadata handling
* `services/` → PDF processing utilities
* `main.py` → FastAPI entry point

---

## data/

Stores runtime-generated data.

* `uploads/` → uploaded PDFs
* `chroma/` → ChromaDB vector database files

---

## tests/

Contains automated API tests.

---

# Environment Variables

Create a `.env` file in the project root.

Example:

```env
GEMINI_API_KEY=your_api_key_here
```

`.env.example` is included as a template.

---

# Running the Project

## Using Docker

```bash
docker compose up --build
```

---

# Swagger Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

---

# Application Flow

1. User uploads a PDF using the `/upload` endpoint.
2. Text is extracted from the PDF using `pypdf`.
3. Extracted text is split into token-based chunks.
4. Gemini generates embeddings for each chunk.
5. Embeddings are stored in ChromaDB.
6. Metadata is stored in SQLite.
7. User sends a question using the `/query` endpoint.
8. Relevant chunks are retrieved from ChromaDB.
9. Retrieved context is sent to Gemini.
10. Gemini generates the final contextual answer.

---

# API Endpoints

## Upload PDF

```http
POST /upload
```

## Query Documents

```http
POST /query
```

Example Request:

```json
{
  "question": "What vector databases are mentioned in the assignment?"
}
```

## View Metadata

```http
GET /documents
```

---

# Running Tests

```bash
pytest
```

---

# Validation Features

* PDF-only upload support
* Maximum 20 documents
* Maximum 1000 pages per document

---
