from typing import Optional

from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    username: str 
    email: EmailStr
    fullname: str 
    disabled: bool 

