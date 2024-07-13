from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.content import Content, ContentCreate, ContentUpdate
from app.services import content as content_service
from app.core.dependencies import get_db, get_current_user
from app.core.constants import ContentMessages

router = APIRouter()


@router.post("/", response_model=Content, status_code=status.HTTP_201_CREATED)
def create_content(
    content: ContentCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return content_service.create_content(
        db=db, content=content, owner_id=current_user.id
    )


@router.get("/{content_id}", response_model=Content, status_code=status.HTTP_200_OK)
def read_content(content_id: int, db: Session = Depends(get_db)):
    db_content = content_service.get_content(db, content_id)
    if db_content is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=ContentMessages.CONTENT_NOT_FOUND,
        )
    return db_content


@router.get("/", response_model=List[Content], status_code=status.HTTP_200_OK)
def read_contents(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return content_service.get_contents(db, skip=skip, limit=limit)


@router.put("/{content_id}", response_model=Content, status_code=status.HTTP_200_OK)
def update_content(
    content_id: int, content_update: ContentUpdate, db: Session = Depends(get_db)
):
    db_content = content_service.update_content(db, content_id, content_update)
    if db_content is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=ContentMessages.CONTENT_NOT_FOUND,
        )
    return db_content


@router.delete("/{content_id}", response_model=Content, status_code=status.HTTP_200_OK)
def delete_content(content_id: int, db: Session = Depends(get_db)):
    db_content = content_service.delete_content(db, content_id)
    if db_content is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=ContentMessages.CONTENT_NOT_FOUND,
        )
    return db_content
