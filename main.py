from uuid import UUID
from fastapi import FastAPI, HTTPException

from model import Gender, Role, User, updateUser

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
    raise HTTPException(
        status_code=404,
        detail="User not found"
    )
    
@app.patch("/api/v1/users/{user_id}")
async def updateUser(user_id:UUID, user:updateUser):
    for u in db:
        if u.id == user_id:
            if user.first_name:
                u.first_name = user.first_name
            if user.last_name:
                u.last_name = user.last_name
            if user.middle_name:
                u.middle_name = user.middle_name
            if user.role:
                u.role = user.role
            return {"message":"user updated successfully"}
            