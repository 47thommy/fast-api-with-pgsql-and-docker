from typing import Optional
from fastapi import FastAPI
from fastapi import Header

app = FastAPI()

@app.get("/")
async def get_root():
    return {"message":"Hello, world!"}

@app.get("/greeting/{username}")
async def greet(username:str):
    return {"message":f"hello {username}"}


user_list =[
    "thomas","salahadin","yohannes","surafel","betselot"
]

@app.get("/search")
async def search(username:str):
    for user in user_list:
        if user == username:
            return {"message":f"details for {username}"}
        else:
            return {"message":"no user with the specified username exist"}
        
        
from pydantic import BaseModel

class userSchema(BaseModel):
    username:str
    email:str
        
users =[]

@app.post("/create")
async def create_user(user_data:userSchema):
    new_user = {
        "username":user_data.username,
        "email":user_data.email
    }
    users.append(new_user)
    return {"message":f"user with email: { user_data.email} created succesfully"}

@app.post("/login")
async def login(token:Optional[str]=Header(None)):
    if token:
        return {"token":token}
    return "no valid token provided"

# simple crud on book in memory database

books = [
    {
        "id": 1,
        "title": "Think Python",
        "author": "Allen B. Downey",
        "publisher": "O'Reilly Media",
        "published_date": "2021-01-01",
        "page_count": 1234,
        "language": "English",
    },
    {
        "id": 2,
        "title": "Django By Example",
        "author": "Antonio Mele",
        "publisher": "Packt Publishing Ltd",
        "published_date": "2022-01-19",
        "page_count": 1023,
        "language": "English",
    },
    {
        "id": 3,
        "title": "The web socket handbook",
        "author": "Alex Diaconu",
        "publisher": "Xinyu Wang",
        "published_date": "2021-01-01",
        "page_count": 3677,
        "language": "English",
    },
    {
        "id": 4,
        "title": "Head first Javascript",
        "author": "Hellen Smith",
        "publisher": "Oreilly Media",
        "published_date": "2021-01-01",
        "page_count": 540,
        "language": "English",
    },
    {
        "id": 5,
        "title": "Algorithms and Data Structures In Python",
        "author": "Kent Lee",
        "publisher": "Springer, Inc",
        "published_date": "2021-01-01",
        "page_count": 9282,
        "language": "English",
    },
    {
        "id": 6,
        "title": "Head First HTML5 Programming",
        "author": "Eric T Freeman",
        "publisher": "O'Reilly Media",
        "published_date": "2011-21-01",
        "page_count": 3006,
        "language": "English",
    },
]


    
    