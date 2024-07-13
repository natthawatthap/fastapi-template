from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.content import Content, ContentCreate
from app.services.content import create_content, get_contents, get_content
from app.core.dependencies import get_db, get_current_user
from app.schemas.user import User

router = APIRouter()

@router.post("/", response_model=Content)
def create_new_content(
    content: ContentCreate, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    return create_content(db=db, content=content, owner_id=current_user.id)

@router.get("/", response_model=List[Content])
def read_contents(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    contents = get_contents(db, skip=skip, limit=limit)
    return contents

@router.get("/{content_id}", response_model=Content)
def read_content(content_id: int, db: Session = Depends(get_db)):
    db_content = get_content(db, content_id=content_id)
    if db_content is None:
        raise HTTPException(status_code=404, detail="Content not found")
    return db_content
