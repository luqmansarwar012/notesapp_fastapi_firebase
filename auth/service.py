from fastapi import Request, HTTPException
from firebase.service import verify_token


async def verify_user(access_token):
    try:
        if not access_token:
            raise HTTPException(status_code=401, detail="Access token is required")

        user_info = verify_token(access_token)

        if user_info is None:
            raise HTTPException(status_code=403, detail="Invalid access token")

        return user_info

    except Exception:
        raise HTTPException(
            status_code=500, detail="Internal Server Error during token verification"
        )
