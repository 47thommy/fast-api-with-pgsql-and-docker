import datetime
from sqlmodel import SQLModel, Column, Field

import sqlalchemy.dialects.postgresql as pg
from datetime import datetime


import uuid

class Book(SQLModel, table=True):
    __tablename__ = "books"
    uid:uuid.UUID = Field(sa_column=Column(
        pg.UUID,
        primary_key=True,
        nullable=False,
        unique=True,
        
    ))
    title:str
    author:str
    publisher:str
    published_date:str
    page_count:int
    language:str
    created_at:datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at:datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    
    def __repr__(self) -> str:
        return f"<Book {self.title}>"