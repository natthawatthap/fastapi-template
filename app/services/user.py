from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.core.security import get_password_hash
from app.repositories import user as user_repo

def get_user_by_email(db: Session, email: str):
    return user_repo.get_user_by_email(db, email)

def create_user(db: Session, user: UserCreate):
    user.hashed_password = get_password_hash(user.password)
    return user_repo.create_user(db, user)

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return user_repo.get_users(db, skip, limit)

def get_user(db: Session, user_id: int):
    return user_repo.get_user(db, user_id)
