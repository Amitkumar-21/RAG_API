# RAG Pipeline

## Overview

RAG Pipeline is a Retrieval-Augmented Generation (RAG) backend system built using FastAPI, Gemini API, and ChromaDB.

The application allows users to:

* Upload PDF documents
* Extract and process document text
* Generate embeddings for semantic search
* Store embeddings in a vector database
* Ask questions based on uploaded documents
* Retrieve relevant document chunks and generate contextual answers

The project is fully Dockerized and includes automated API tests.

---

# Features

* PDF document upload support
* Token-based text chunking
* Gemini embedding generation
* ChromaDB vector database integration
* Retrieval-Augmented Generation (RAG)
* FastAPI REST APIs
* SQLite metadata storage
* Automated testing using pytest
* Docker and Docker Compose support
* Swagger API documentation

---

# Tech Stack

## Backend

* FastAPI
* Python

## AI / RAG

* Gemini API
* ChromaDB
* tiktoken
* pypdf

## Database

* SQLite

## Deployment

* Docker
* Docker Compose

## Testing

* Pytest

---

# Project Structure

```text
Panscience/
│
├── app/
├── data/
├── tests/
├── pansc/
│
├── .dockerignore
├── .env
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── README.md
└── requirements.txt
```

---

# Folder and File Explanation

## app/

This folder contains the main backend application code.

### app/api/

Contains all FastAPI API routes.

Files inside this folder:

* `upload.py`

  * Handles PDF uploads
  * Extracts and processes document text
  * Stores embeddings and metadata

* `query.py`

  * Handles user questions
  * Retrieves relevant chunks from ChromaDB
  * Generates final answers using Gemini

* `documents.py`

  * Returns metadata of uploaded documents
  * Displays filename, page count, and chunk count

---

### app/db/

Contains database-related logic.

Files inside this folder:

* `metadata_db.py`

  * Creates and manages SQLite metadata database
  * Stores uploaded document information
  * Retrieves document metadata

---

### app/rag/

Contains core RAG pipeline logic.

Files inside this folder:

* `chunker.py`

  * Splits extracted text into token-based chunks

* `embedder.py`

  * Generates embeddings using Gemini API

* `vector_store.py`

  * Stores and retrieves embeddings using ChromaDB

* `generator.py`

  * Sends retrieved context to Gemini
  * Generates final answers

---

### app/services/

Contains helper services used by APIs.

Files inside this folder:

* `pdf_service.py`

  * Extracts text from PDF documents
  * Counts PDF pages

---

### app/main.py

Main FastAPI application entry point.

Responsibilities:

* Creates FastAPI app
* Registers API routers
* Starts backend application

---

## data/

Stores runtime-generated data.

This folder is ignored from GitHub except for placeholder `.gitkeep` files.

### data/uploads/

Stores uploaded PDF documents temporarily.

### data/chroma/

Stores ChromaDB vector database files.

---

## tests/

Contains automated API tests.

Files inside this folder:

* `test_api.py`

  * Tests API endpoints
  * Verifies upload validation
  * Verifies query responses

---

## pansc/

Python virtual environment folder.

Contains installed dependencies and local Python packages.

This folder is ignored using `.gitignore` and is not pushed to GitHub.

---

# Root-Level Files

## requirements.txt

Contains all Python dependencies required to run the project.

Used during:

* Local setup
* Docker image build

---

## Dockerfile

Defines the Docker image configuration.

Responsibilities:

* Creates Python environment
* Installs dependencies
* Copies project files
* Starts FastAPI server

---

## docker-compose.yml

Defines Docker Compose services.

Responsibilities:

* Builds Docker container
* Maps ports
* Mounts data volume
* Loads environment variables

---

## .gitignore

Prevents unnecessary files from being pushed to GitHub.

Examples:

* Virtual environment
* Cache files
* Runtime databases
* Uploaded PDFs
* Environment variables

---

## .dockerignore

Prevents unnecessary files from being copied into Docker build context.

Improves:

* Build speed
* Docker image size
* Storage usage

---

## .env

Stores private environment variables.

Example:

```env
GEMINI_API_KEY=your_api_key_here
```

Important:

* This file should never be pushed to GitHub
* `.gitignore` prevents tracking this file

---

## .env.example

Template environment file.

Used to show required environment variables without exposing real secrets.

Example:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <repository-url>
cd Panscience
```

---

## 2. Create Environment File

Create a `.env` file in the project root.

Example:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## 3. Run Using Docker

```bash
docker compose up --build
```

---

# Access Swagger UI

Open:

```text
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## Upload PDF

```http
POST /upload
```

Uploads and processes PDF documents.

---

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

---

## View Document Metadata

```http
GET /documents
```

Returns:

* Filename
* Page count
* Chunk count

---

# Running Tests

Run automated tests using:

```bash
pytest
```

---

# Dockerized Deployment

The application is fully containerized using Docker and Docker Compose.

This ensures:

* Consistent environment setup
* Easier deployment
* Dependency isolation
* Reproducible builds

---

# Validation Features

The application includes:

* PDF-only upload validation
* Maximum 20 document limit
* Maximum 1000 pages per document

---

# Future Improvements

Possible future enhancements:

* OCR support for scanned PDFs
* Authentication system
* Frontend interface
* Document deletion endpoint
* Retrieval reranking
* Multi-user support

---

# Author

Amit Kumar
