from uuid import UUID
from fastapi import FastAPI

from model import Gender, Role, User

app = FastAPI()

db:list[User]=[
    User(first_name="Thomas",last_name="wondwosen",gender=Gender.male,role=[Role.admin,Role.student], id=UUID("2d281da4-6d79-4797-9b39-c50797960d7a")),
    
    User(first_name="lielina", last_name="endris", gender=Gender.female, role=[Role.user], id=UUID("f3866763-5cb9-4fce-993b-449fe7aa8b51"))  
]

@app.get("/")
async def root():
    return {"message":"Hello Thomas"}
@app.get("/api/v1/users")
async def getAllUsers():
    return db
@app.post("/api/v1/users")
async def registerUser(user:User):
    db.append(user)
    return {"id":user.id}
@app.delete("/api/v1/users/{user_id}")
async def deleteUser(user_id:UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"message":"user deleted successfully"}
    return {"message":"user not found"}