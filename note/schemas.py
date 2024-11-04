from pydantic import BaseModel


class NoteCreate(BaseModel):
    title: str
    content: str


class NoteResponse(NoteCreate):
    key: str
    uid: str


class DeleteNoteResponse(BaseModel):
    message: str
