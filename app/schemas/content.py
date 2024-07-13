from pydantic import BaseModel

class ContentBase(BaseModel):
    title: str
    body: str

class ContentCreate(ContentBase):
    pass

class Content(ContentBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True
