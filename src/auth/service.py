from src.auth.utils import generate_password_hash, verify_password
from src.auth.schemas import userCreateModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from src.auth.models import User

class UserService:
    async def get_user_by_email(self, session:AsyncSession, user_email:str):
        statement = select(User).where(User.email == user_email)
        
        result = await session.exec(statement)
        user = result.first()
        return user
    async def user_exists(self, session:AsyncSession, user_email:str):
        user = await self.get_user_by_email(session=session, user_email=user_email)
        return True if user is not None else False
    async def create_user(self, session:AsyncSession, user_data:userCreateModel):
        user_data_dict = user_data.model_dump()
        new_user = User(**user_data_dict)
        new_user.password_hash = generate_password_hash(user_data_dict["password"])
        session.add(new_user)
        await session.commit()
        return new_user