from typing import Optional

from pydantic import BaseModel

from model import Gender, Role


class updateUserDto(BaseModel):
    first_name:Optional[str] = None
    last_name:Optional[str] = None
    middle_name:Optional[str] = None
    role:Optional[list[Role]] = None
    
class createUserDto(BaseModel):
    first_name:str
    last_name:str
    middle_name:Optional[str] = None
    role:list[Role]
    gender:Gender