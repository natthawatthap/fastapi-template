from sqlalchemy.orm import Session
from app.db.models.content import Content
from app.schemas.content import ContentCreate

def get_content(db: Session, content_id: int):
    return db.query(Content).filter(Content.id == content_id).first()

def get_contents(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Content).offset(skip).limit(limit).all()

def create_content(db: Session, content: ContentCreate, owner_id: int):
    db_content = Content(**content.dict(), owner_id=owner_id)
    db.add(db_content)
    db.commit()
    db.refresh(db_content)
    return db_content
