# tests/conftest.py
import pytest
from sqlmodel import SQLModel, create_engine, Session
from fastapi.testclient import TestClient
from app.main import app
from app.database import get_session

TEST_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})

# Override the session dependency
def get_test_session():
    with Session(engine) as session:
        yield session

@pytest.fixture(scope="module")
def client():
    # Create tables once
    SQLModel.metadata.create_all(engine)
    app.dependency_overrides[get_session] = get_test_session

    with TestClient(app) as c:
        yield c

    # Drop tables after all tests
    SQLModel.metadata.drop_all(engine)

@pytest.fixture()
def auth_headers(client):
    # Register/login user once per test
    client.post("/auth/register", json={
        "email": "test@example.com",
        "password": "password123"
    })
    login_resp = client.post("/auth/login", json={
        "email": "test@example.com",
        "password": "password123"
    })
    access_token = login_resp.json()["access_token"]
    return {"Authorization": f"Bearer {access_token}"}
