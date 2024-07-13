from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.user import User, UserCreate, UserUpdate
from app.services import user as user_service
from app.core.dependencies import get_db
from app.core.constants import UserMessages

router = APIRouter()

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = user_service.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=UserMessages.EMAIL_ALREADY_REGISTERED)
    return user_service.create_user(db=db, user=user)

@router.get("/{user_id}", response_model=User, status_code=status.HTTP_200_OK)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_service.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=UserMessages.USER_NOT_FOUND)
    return db_user

@router.get("/", response_model=List[User], status_code=status.HTTP_200_OK)
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = user_service.get_users(db, skip=skip, limit=limit)
    return users

@router.put("/{user_id}", response_model=User, status_code=status.HTTP_200_OK)
def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    db_user = user_service.update_user(db, user_id, user_update)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=UserMessages.USER_NOT_FOUND)
    return db_user

@router.delete("/{user_id}", response_model=User, status_code=status.HTTP_200_OK)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_service.delete_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=UserMessages.USER_NOT_FOUND)
    return db_user
