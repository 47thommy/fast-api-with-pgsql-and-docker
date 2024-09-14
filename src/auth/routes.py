from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from.service import UserService
from src.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from .schemas import userCreateModel,userLoginModel
from datetime import timedelta
from .utils import verify_password, create_access_token, decode_token
from src.config import Config

auth_router = APIRouter()
user_service = UserService()

@auth_router.post("/signup", status_code=status.HTTP_201_CREATED)
async def create_user_account(user_data:userCreateModel,session:AsyncSession = Depends(get_session)):
    user_email = user_data.email
    user_exists = await user_service.user_exists(user_email=user_email, session=session)
    if user_exists:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User with email already exists"
        )
    new_user = await user_service.create_user(session=session, user_data=user_data)
    return new_user
@auth_router.post("/login")
async def login(login_data:userLoginModel, session:AsyncSession = Depends(get_session)):
    email = login_data.email
    password = login_data.password
    user = await user_service.get_user_by_email(session=session, user_email=email)
    if user is not None:
        valid_password = verify_password(passord=password, hash=user.password_hash)
        if valid_password:
            user_data = {"email":user.email, "user_id":str(user.uid)}
            access_token  = create_access_token(user_data=user_data)
            refresh_token = create_access_token(user_data=user_data, expiry=timedelta(days=Config.REFRESH_TOKEN_EXPIRY), refresh=True)
            
            return JSONResponse(
                content={
                    "message":"Login successful",
                    "access_token":access_token,
                    "refresh_token":refresh_token,
                    "user_data":user_data
                }
            )
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Incorrect email or password")