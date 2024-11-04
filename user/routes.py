from fastapi import HTTPException, APIRouter, status
from .schemas import UserSignup, UserSignupResponse
from firebase.service import signup_user

router = APIRouter()


@router.post(
    "/signup", response_model=UserSignupResponse, status_code=status.HTTP_201_CREATED
)
def signup(user_info: UserSignup):
    try:
        user = signup_user(user_info)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="The email address is already in use.",
            )
        return UserSignupResponse(
            message="User created successfully",
            email=user["email"],
            uuid=user["localId"],
        )

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred.",
        )
