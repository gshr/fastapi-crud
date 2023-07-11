from pydantic import BaseModel
from typing import Optional



class UserModel(BaseModel):
    username: str
    email: str
    password: str
    
    
    
class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    