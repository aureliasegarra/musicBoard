from typing import Optional
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


# The ShowUser class is used to return only the necessary user data to the client.
class ShowUser(BaseModel):
    username: str
    email: EmailStr
    is_active: bool

    class Config():
        orm_mode = True
