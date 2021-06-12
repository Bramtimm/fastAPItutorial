# defines schemas for working with the specific API request/response

# imports
from typing import List
from pydantic import BaseModel

class UserInfoBase(BaseModel):
    username: str
    fullname: str

class UserCreate(UserInfoBase):
    password: str

class UserInfo(UserInfoBase):
    id: int

    class config:
        orm_mode = True