from pydantic import BaseModel, Field, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    name: str = Field(min_length=4, max_length=20)
    email: EmailStr
    password: str = Field(max_length=250)
    created_at: datetime

class UserCreateReturn(UserCreate):
    id: str
    created_at: datetime

    class Config:
        from_attributes = True   