from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_hello_crud_flow_with_valid_input():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "hello"}

    response = client.post("/hello", json={"message": "world"})
    assert response.status_code == 201
    assert response.json() == {"message": "created: world"}

    response = client.put("/hello", json={"message": "updated"})
    assert response.status_code == 200
    assert response.json() == {"message": "updated: updated"}

    response = client.patch("/hello", json={"message": "patched"})
    assert response.status_code == 200
    assert response.json() == {"message": "patched: patched"}

    response = client.delete("/hello")
    assert response.status_code == 200
    assert response.json() == {"deleted": "patched", "message": "hello"}


def test_hello_invalid_input_is_rejected():
    response = client.post("/hello", json={"message": "   "})
    assert response.status_code == 422
    assert "message cannot be empty" in response.text

    response = client.post("/hello", json={"message": "x" * 51})
    assert response.status_code == 422
    assert "at most 50 characters" in response.text


def test_docs_endpoints_are_available():
    response = client.get("/docs")
    assert response.status_code == 200
    assert "swagger" in response.text.lower()

    response = client.get("/openapi.json")
    assert response.status_code == 200
    assert response.json()["info"]["title"] == "CloudOps AI"
