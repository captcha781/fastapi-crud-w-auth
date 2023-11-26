from pydantic import BaseModel, EmailStr
from typing import Annotated, Optional, Any
from beanie import Document, Indexed

class UserRegister(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str

class UserReturn(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    
class UserReturnList(UserReturn):
    users: list
    
class UserSignin(BaseModel):
    email: EmailStr
    password: str

class User (Document):
    email: Annotated[str, Indexed(EmailStr, unique=True)]
    password: str
    first_name: str
    last_name: str
    
    @classmethod
    async def find_by_email(cls, email_id):
        return await cls.find_one(cls.email == email_id)
    
    class Settings:
        name = 'users'