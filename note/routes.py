from fastapi import APIRouter, status, Depends, HTTPException
from .schemas import NoteCreate, NoteResponse, DeleteNoteResponse
from .service import save_note, fetch_notes, remove_note, edit_note
from auth.service import verify_user
from typing import List

router = APIRouter()


@router.post(
    "/{access_token}", response_model=NoteResponse, status_code=status.HTTP_201_CREATED
)
def create_note(
    access_token,
    note: NoteCreate,
    user: dict = Depends(verify_user),
):
    try:
        new_note_key = save_note(user_uid=user["uid"], note=note)
        return NoteResponse(key=new_note_key, **note.model_dump(), uid=user["uid"])

    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get(
    "/{access_token}/notes",
    response_model=List[NoteResponse],
    status_code=status.HTTP_200_OK,
)
def get_notes(
    access_token,
    user: dict = Depends(verify_user),
):
    try:
        notes = fetch_notes(user_uid=user["uid"])

        if not notes:
            raise HTTPException(status_code=404, detail="No notes found for the user")

        return [NoteResponse(key=key, **note) for key, note in notes.items()]

    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


@router.delete(
    "/{access_token}/notes/{note_key}",
    response_model=DeleteNoteResponse,
    status_code=status.HTTP_200_OK,
)
def delete_note(
    access_token,
    note_key: str,
    user: dict = Depends(verify_user),
):
    try:
        remove_note(user_uid=user["uid"], note_key=note_key)

        return DeleteNoteResponse(message="Note deleted successfully")

    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


@router.put(
    "/{access_token}/notes/{note_key}",
    response_model=NoteResponse,
    status_code=status.HTTP_200_OK,
)
def update_note(
    access_token,
    note_key: str,
    updated_note: NoteCreate,
    user: dict = Depends(verify_user),
):
    try:
        updated_note_data = edit_note(
            user_uid=user["uid"],
            note_key=note_key,
            updated_data=updated_note.model_dump(),
        )

        if not updated_note_data:
            raise HTTPException(status_code=404, detail="Note not found")

        return NoteResponse(key=note_key, **updated_note_data)

    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")
