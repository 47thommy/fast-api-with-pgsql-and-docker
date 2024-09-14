from pydantic import BaseModel
from sqlmodel import Field

class userCreateModel(BaseModel):
    first_name:str = Field(max_length=25, min_length=3)
    last_name:str = Field(max_length=25, min_length=3)
    username:str = Field(max_length=8)
    email:str
    password:str = Field(min_length=8)
class userLoginModel(BaseModel):
    password:str = Field(min_length=8)
    email:str