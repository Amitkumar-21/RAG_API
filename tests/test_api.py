from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "RAG API Running"
    }

def test_query():
    response = client.post(
        "/query",
        json={
            "question": "What vector databases are mentioned?"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "answer" in data

def test_invalid_file_upload():
    response = client.post(
        "/upload",
        files={
            "file": (
                "test.txt",
                b"hello world",
                "text/plain"
            )
        }
    )
    assert response.status_code == 400
    assert response.json()["detail"] == (
        "Only PDF files are allowed"
    )