from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class User(UserBase): # Esquema para ler dados do utilizador
    id: int
    created_at: datetime

    class Config:
        from_attributes = True # Para Pydantic V2 (era orm_mode = True)