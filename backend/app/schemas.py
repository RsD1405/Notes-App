from sqlmodel import SQLModel
from typing import Optional
from datetime import datetime, timezone

class NoteBase(SQLModel):
    title: str
    content: str

class NoteCreate(NoteBase):
    pass

class NoteRead(NoteBase):
    id: int
    created_at: datetime
    updated_at: datetime

class NoteUpdate(SQLModel):
    title: Optional[str] = None
    content: Optional[str] = None
