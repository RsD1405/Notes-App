# tests/conftest.py
import pytest
from sqlmodel import SQLModel, create_engine, Session
from fastapi.testclient import TestClient
from app.main import app
from app.database import get_session

# tests/conftest.py
TEST_DATABASE_URL = "sqlite:///./test.db"  # file-based SQLite
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})


# Override the session dependency
def get_test_session():
    with Session(engine) as session:
        yield session

@pytest.fixture(scope="module")
def client():
    # Create tables in test DB
    SQLModel.metadata.create_all(engine)

    # Override FastAPI dependency
    app.dependency_overrides[get_session] = get_test_session

    with TestClient(app) as c:
        yield c

    # Optional: drop tables after tests
    SQLModel.metadata.drop_all(engine)
