from uuid import uuid4

from fastapi.testclient import TestClient

from src.database import SessionLocal
from src.main import app
from src.models import User

client = TestClient(app)


def unique_email(prefix: str) -> str:
    return f"{prefix}-{uuid4().hex[:8]}@example.com"


def test_create_user_success():
    email = unique_email("create-user")
    response = client.post("/users", json={"name": "Alice", "email": email})
    assert response.status_code == 201
    payload = response.json()
    assert payload["name"] == "Alice"
    assert payload["email"] == email
    assert payload["id"] is not None


def test_list_users_returns_users():
    email = unique_email("list-user")
    client.post("/users", json={"name": "Bob", "email": email})
    response = client.get("/users")
    assert response.status_code == 200
    result = response.json()
    assert any(item["email"] == email for item in result)


def test_get_user_by_id_success():
    email = unique_email("get-user")
    created = client.post("/users", json={"name": "Carol", "email": email})
    user_id = created.json()["id"]

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    payload = response.json()
    assert payload["name"] == "Carol"
    assert payload["email"] == email


def test_invalid_user_payload_is_rejected():
    response = client.post("/users", json={"name": "", "email": "not-an-email"})
    assert response.status_code == 422


def test_user_not_found_returns_404():
    response = client.get("/users/999999")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"


def test_duplicate_email_returns_conflict():
    email = unique_email("duplicate-user")
    first = client.post("/users", json={"name": "Alice", "email": email})
    assert first.status_code == 201

    second = client.post("/users", json={"name": "Alice Duplicate", "email": email})
    assert second.status_code == 409
    assert second.json()["detail"] == "A user with this email already exists."
