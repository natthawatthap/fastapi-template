from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import get_password_hash
from app.repositories import user as user_repo
from app.db.models.user import User

def get_user(db: Session, user_id: int):
    return user_repo.get_user(db, user_id)

def get_user_by_email(db: Session, email: str):
    return user_repo.get_user_by_email(db, email)

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return user_repo.get_users(db, skip, limit)

def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(
        email=user.email,
        hashed_password=hashed_password,
        is_active=user.is_active,
        is_superuser=user.is_superuser
    )
    return user_repo.create_user(db, db_user)

def update_user(db: Session, user_id: int, user_update: UserUpdate):
    db_user = user_repo.get_user(db, user_id)
    if not db_user:
        return None
    if user_update.password:
        user_update.hashed_password = get_password_hash(user_update.password)
    return user_repo.update_user(db, db_user, user_update)

def delete_user(db: Session, user_id: int):
    return user_repo.delete_user(db, user_id)
