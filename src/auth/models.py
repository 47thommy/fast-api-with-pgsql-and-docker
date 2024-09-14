from sqlmodel import SQLModel, Column, Field
import sqlalchemy.dialects.postgresql as pg
import uuid
from datetime import datetime
class User(SQLModel, table=True):
    __tablename__ = "users"
    
    uid: uuid.UUID = Field(sa_column=Column(
        pg.UUID,
        primary_key=True,
        unique=True,
        nullable=False,
        default=uuid.uuid4,
        info={"description":"Unique identifier for the user account"}
    ))
    username:str
    first_name:str = Field(nullable=True)
    last_name:str = Field(nullable=True)
    is_verified:bool
    email:str
    password_hash:str
    created_at:datetime = Field(sa_column=(Column(pg.TIMESTAMP, default=datetime.now)))
    
    def __repr__(self) -> str:
        return f"<User {self.username}>"