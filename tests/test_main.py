from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Task API is running"


def test_add_task():
    response = client.post("/tasks", json={"title": "Learn Docker"})
    assert response.status_code == 200
    assert response.json()["title"] == "Learn Docker"
