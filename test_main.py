from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Task Manager API is running for TEST"}

def test_create_task():
    response = client.post("/tasks/", json={"title": "new task", "description": "Description of new task"})
    assert response.status_code == 200
    assert response.json()["title"] == "new task"

def test_read_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_task():
    response = client.put("/tasks/1", json={"title": "update task", "description": "new description", "completed": True})
    assert response.status_code == 200
    assert response.json()["completed"] == True

def test_delete_task():
    response = client.delete("/tasks/1")
    assert response.status_code == 200
    assert response.json()["message"] == "deleted successfully"