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

@app.get("/search")
async def search(username:str):
    for user in user_list:
        if user == username:
            return {"message":f"details for {username}"}
        else:
            return {"message":"no user with the specified username exist"}