from fastapi import FastAPI

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
