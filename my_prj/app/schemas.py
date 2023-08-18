from typing import Union
from datetime import datetime

from pydantic import BaseModel

class UserBase(BaseModel):
    user_id: str
    name: str
    profile: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    
class Board(BaseModel):
    id: Union[int, None] = None
    title: str
    desc: str
    created_at: Union[datetime, None] = None
    user_id: Union[str, None] = None