from enum import Enum
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, Enum as SqlEnum, text
from database import Base  # Assuming you have Base properly set up from SQLAlchemy

# Define the Enum classes
class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"

# Define the User model
class User(Base):
    
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=True)
    
    # Use SQLAlchemy's Enum to define Enum columns
    gender = Column(SqlEnum(Gender), nullable=False)
    role = Column(SqlEnum(Role), nullable=False)
    
    createdAt = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)
