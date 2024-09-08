from uuid import uuid4
from fastapi import FastAPI

from model import Gender, Role, User

app = FastAPI()

db:list[User]=[
    User(first_name="Thomas",last_name="wondwosen",gender=Gender.male,role=[Role.admin,Role.student], id=uuid4()),
    
    User(first_name="lielina", last_name="endris", gender=Gender.female, role=[Role.user], id=uuid4())  
]

@app.get("/")
def root():
    return {"message":"Hello Thomas"}