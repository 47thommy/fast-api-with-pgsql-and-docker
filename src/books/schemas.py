from pydantic import BaseModel

class Book (BaseModel):
    id:str
    title:str
    author:str
    publisher:str
    published_date:str
    page_count:int
    language:str
    
class updateBook(BaseModel):
    title:str
    author:str
    publisher:str
    page_count:int
    language:str