from sqlmodel import  SQLModel
from sqlalchemy.ext.asyncio import create_async_engine
from src.books.models import Book
from src.config import Config
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker


engine = create_async_engine(
    url=Config.DATABASE_URL,
    echo=True
)

async def initdb():
    """create a connection to our db"""

    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
        

async def get_session()-> AsyncSession:
    async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
    
    async with async_session() as session:
        yield session