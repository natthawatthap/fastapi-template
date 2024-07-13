from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.auth import AuthTokenResponse
from app.core.dependencies import get_db
from app.services import auth as auth_service

router = APIRouter()

@router.post("/login", response_model=AuthTokenResponse)
def login(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    return auth_service.authenticate_user(db, form_data)

@router.post("/refresh", response_model=AuthTokenResponse)
def refresh_token(refresh_token: str):
    return auth_service.refresh_access_token(refresh_token)
