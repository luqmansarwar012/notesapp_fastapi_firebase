from pydantic import BaseModel


class UserSignup(BaseModel):
    email: str
    password: str


class UserSignupResponse(BaseModel):
    message: str
    email: str
    uuid: str
