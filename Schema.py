from pydantic import BaseModel

from model import Gender, Role

class userBase(BaseModel):
    first_name:str
    last_name:str
    middle_name:str = None
    role:list[Role]
    gender: Gender
    
    class config:
        orm_mode=True   
        
class createUserDto(userBase):
    class config:
        orm_mode=True
        