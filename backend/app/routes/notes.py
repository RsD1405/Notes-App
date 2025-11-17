from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List

from app.crud import (
    create_note,
    get_note,
    read_notes,
    update_note,
    delete_note
)

from app.database import get_session
from app.schemas import NoteCreate, NoteRead, NoteUpdate
from app.models import Note

router = APIRouter(
    prefix="/notes",
    tags=["Notes"]
)


@router.post("/", response_model=NoteRead, status_code=201)
def create_note_endpoint(
    note: NoteCreate,
    session: Session = Depends(get_session)
):
    return create_note(note, session)

@router.get("/", response_model=List[NoteRead])
def read_notes_endpoint(
    session: Session = Depends(get_session),
    skip: int = 0,
    limit: int = 100
):
    return read_notes(session, skip, limit)


@router.patch("/{note_id}", response_model=NoteRead)
def update_note_endpoint(
    note_id: int,
    note: NoteUpdate,
    session: Session = Depends(get_session)
):
    db_note = get_note(session, note_id)
    if not db_note:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )
    return update_note(note, db_note, session)


@router.delete("/{note_id}", status_code=204)
def delete_note_endpoint(
    note_id: int,
    session: Session = Depends(get_session)
):
    db_note = get_note(session, note_id)
    if not db_note:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )
    delete_note(db_note, session)
    return