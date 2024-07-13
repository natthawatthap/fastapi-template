from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.services import user as user_service

def test_create_user(db: Session):
    user_in = UserCreate(email="test@example.com", password="password")
    user = user_service.create_user(db, user_in)
    assert user.email == "test@example.com"
    assert user.id is not None

def test_get_user_by_email(db: Session):
    user_in = UserCreate(email="test@example.com", password="password")
    user_service.create_user(db, user_in)
    user = user_service.get_user_by_email(db, "test@example.com")
    assert user is not None
    assert user.email == "test@example.com"

def test_get_users(db: Session):
    user_in1 = UserCreate(email="test1@example.com", password="password")
    user_in2 = UserCreate(email="test2@example.com", password="password")
    user_service.create_user(db, user_in1)
    user_service.create_user(db, user_in2)
    users = user_service.get_users(db, skip=0, limit=10)
    assert len(users) == 2
