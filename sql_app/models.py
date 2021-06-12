# define class object models for FastAPI

from sql_app.database import Base
# imports
from sqlalchemy import Column, Integer, String


class UserInfo(Base):
    __tablename__ = "user_info"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    fullname = Column(String, unique=True)