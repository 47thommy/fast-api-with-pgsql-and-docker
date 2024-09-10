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
    
    