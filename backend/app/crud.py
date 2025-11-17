from app.schemas import NoteCreate, NoteRead, NoteUpdate
from app.models import Note
from sqlmodel import Session, select
from fastapi import Depends


def create_note(
        note: NoteCreate,
        session: Session
):
    db_note = Note(**note.model_dump()) # To convert pydantic schema to database model
    session.add(db_note)
    session.commit()
    session.refresh(db_note)
    return db_note


def get_note(session: Session, note_id: int) -> Note | None:
    return session.get(Note, note_id)


def read_notes(
        session: Session,
        skip: int = 0,
        limit: int = 100
):
    notes = session.exec(select(Note).offset(skip).limit(limit))
    return notes.all()


def update_note(
        note: NoteUpdate,
        db_note: Note,
        session: Session
) -> Note:
    update_dict = note.model_dump(exclude_unset=True)
    for field, value in update_dict.items():
        setattr(db_note, field, value)
    session.add(db_note)
    session.commit()
    session.refresh(db_note)
    return db_note


def delete_note(
        db_note: Note,
        session: Session
):
    session.delete(db_note)
    session.commit()
    return True