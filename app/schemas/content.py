from pydantic import BaseModel

class ContentBase(BaseModel):
    title: str
    description: str = None

class ContentCreate(ContentBase):
    pass

class ContentUpdate(ContentBase):
    pass

class ContentInDBBase(ContentBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True

class Content(ContentInDBBase):
    pass
