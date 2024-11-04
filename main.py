from user.routes import router as user_router
from auth.routes import router as auth_router
from note.routes import router as note_router
from fastapi import FastAPI


app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(user_router, prefix="/users", tags=["User"])
app.include_router(note_router, prefix="/notes", tags=["Note"])
