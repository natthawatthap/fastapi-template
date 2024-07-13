from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.core.security import (
    create_access_token,
    create_refresh_token,
    verify_password,
    decode_refresh_token,
)
from app.services.user import get_user_by_email
from app.core.constants import AuthMessages
from app.schemas.auth import AuthTokenResponse

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/login")


def authenticate_user(
    db: Session, form_data: OAuth2PasswordRequestForm
) -> AuthTokenResponse:
    user = get_user_by_email(db, email=form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=AuthMessages.INVALID_CREDENTIALS,
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"user_id": user.id})
    refresh_token = create_refresh_token(data={"user_id": user.id})
    return AuthTokenResponse(
        access_token=access_token, refresh_token=refresh_token, token_type="bearer"
    )


def refresh_access_token(refresh_token: str) -> AuthTokenResponse:
    payload = decode_refresh_token(refresh_token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user_id = payload.get("user_id")
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"user_id": user_id})
    return AuthTokenResponse(
        access_token=access_token, refresh_token=refresh_token, token_type="bearer"
    )
