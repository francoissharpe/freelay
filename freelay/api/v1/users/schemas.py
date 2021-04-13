from typing import List, Optional

from pydantic import BaseModel, EmailStr


class EmailBase(BaseModel):
    address: EmailStr


class EmailCreate(EmailBase):
    pass


class Email(EmailBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    generated_emails: List[Email]

    class Config:
        orm_mode = True
