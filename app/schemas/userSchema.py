from pydantic import BaseModel, Field, EmailStr, ConfigDict
from datetime import datetime
import uuid

class UserCreate(BaseModel):
    name: str = Field(min_length=4, max_length=20)
    email: EmailStr
    password: str = Field(max_length=250)

class UserCreateReturn(BaseModel):
    id: uuid.UUID
    name: str
    email: str
    created_at: datetime

    
    model_config = ConfigDict(from_attributes=True)  

class UserCredentials(BaseModel):
    email: EmailStr
    password: str = Field(max_length=250)

class UserLoginReturn(BaseModel):
    id: uuid.UUID
    name: str
    email: str

    model_config = ConfigDict(from_attributes=True)