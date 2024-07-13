import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.db.base import Base
from app.db.session import get_db
from app.schemas.user import UserCreate
from app.services.user import create_user
from app.schemas.content import ContentCreate
from app.services.auth import get_password_hash

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Override the get_db dependency to use the test database
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="module")
def test_client():
    Base.metadata.create_all(bind=engine)
    client = TestClient(app)
    yield client
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="module")
def test_db():
    db = TestingSessionLocal()
    # Create a test user
    user = UserCreate(email="testuser@example.com", password="password")
    db_user = create_user(db, user)
    yield db
    db.close()

def get_token(client: TestClient):
    response = client.post("/api/v1/auth/token", data={"username": "testuser@example.com", "password": "password"})
    assert response.status_code == 200
    return response.json()["access_token"]

def test_create_content(test_client: TestClient, test_db):
    token = get_token(test_client)
    headers = {"Authorization": f"Bearer {token}"}
    response = test_client.post("/api/v1/contents/", json={"title": "Test Title", "body": "Test Body"}, headers=headers)
    assert response.status_code == 200
    assert response.json()["title"] == "Test Title"

def test_read_contents(test_client: TestClient, test_db):
    token = get_token(test_client)
    headers = {"Authorization": f"Bearer {token}"}
    response = test_client.get("/api/v1/contents/", headers=headers)
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_read_content(test_client: TestClient, test_db):
    token = get_token(test_client)
    headers = {"Authorization": f"Bearer {token}"}
    response = test_client.get("/api/v1/contents/1", headers=headers)
    assert response.status_code == 200
    assert response.json()["title"] == "Test Title"
