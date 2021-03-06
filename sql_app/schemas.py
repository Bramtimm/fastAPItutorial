# defines schemas for working with the specific API request/response

# imports
from pydantic import BaseModel

class UserInfoBase(BaseModel):
    username: str
    fullname: str

class UserCreate(UserInfoBase):
    password: str

class UserInfo(UserInfoBase):
    id: int

    class Config:
        orm_mode = True
