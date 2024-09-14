from fastapi import APIRouter, Depends, HTTPException, status
from.service import UserService
from src.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from .schemas import userCreateModel

auth_router = APIRouter()
user_service = UserService()

@auth_router.post("/", status_code=status.HTTP_201_CREATED)
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