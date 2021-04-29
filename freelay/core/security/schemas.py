from typing import Optional

from pydantic import BaseModel

from freelay.api.v1.users.schemas import User


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class UserInDB(User):
    hashed_password: str
