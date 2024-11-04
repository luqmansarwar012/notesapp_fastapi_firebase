from pydantic import BaseModel


class Login(BaseModel):
    email: str
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "testuser@example.com",
                "password": "123456",
            }
        }


class Token(BaseModel):
    access_token: str
    token_type: str
