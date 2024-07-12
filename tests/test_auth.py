# tests/test_auth.py

import pytest
from httpx import AsyncClient
from app.main import app
from app.db.session import SessionLocal
from app.db.models.user import User
from sqlalchemy.orm import Session

@pytest.fixture(scope="module")
def test_db():
    db = SessionLocal()
    yield db
    db.close()

@pytest.fixture(scope="module")
async def client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

def create_test_user(db: Session):
    db_user = User(email="test@example.com", hashed_password="$2b$12$KIXaJAdO.YOWZLr4rP71/.98E3GH4P2b6Q4z5A3HZ6Ez3zFS1P5jK")  # Password: "password"
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@pytest.mark.asyncio
async def test_get_access_token(client: AsyncClient, test_db: Session):
    create_test_user(test_db)
    response = await client.post("/api/v1/auth/token", data={"username": "test@example.com", "password": "password"})
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"
