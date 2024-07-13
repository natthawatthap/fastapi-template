from sqlalchemy.orm import Session
from app.schemas.content import ContentCreate, ContentUpdate
from app.repositories import content as content_repo

def get_content(db: Session, content_id: int):
    return content_repo.get_content(db, content_id)

def get_contents(db: Session, skip: int = 0, limit: int = 10):
    return content_repo.get_contents(db, skip, limit)

def create_content(db: Session, content: ContentCreate, owner_id: int):
    return content_repo.create_content(db, content, owner_id)

def update_content(db: Session, content_id: int, content_update: ContentUpdate):
    db_content = content_repo.get_content(db, content_id)
    if not db_content:
        return None
    return content_repo.update_content(db, db_content, content_update)

def delete_content(db: Session, content_id: int):
    db_content = content_repo.get_content(db, content_id)
    if not db_content:
        return None
    return content_repo.delete_content(db, db_content)
