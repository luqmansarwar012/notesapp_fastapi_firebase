from fastapi import HTTPException, APIRouter, status
from firebase.service import get_access_token
from .schemas import Login, Token


router = APIRouter()


@router.post("/login", response_model=Token, status_code=status.HTTP_201_CREATED)
def create_access_token(credentials: Login):
    try:
        token = get_access_token(credentials)
        return Token(access_token=token, token_type="bearer")
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error occurred.")
