from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.core.security import create_access_token, verify_password
from app.services.user import get_user_by_email
from app.core.constants import AuthMessages
from app.schemas.auth import AuthTokenResponse

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/login")

def authenticate_user(db: Session, form_data: OAuth2PasswordRequestForm) -> AuthTokenResponse:
    user = get_user_by_email(db, email=form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=AuthMessages.INVALID_CREDENTIALS,
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"user_id": user.email})
    return AuthTokenResponse(access_token=access_token, token_type="bearer")
