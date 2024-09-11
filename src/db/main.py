from sqlmodel import  text, SQLModel
from sqlalchemy.ext.asyncio import create_async_engine
from src.books.models import Book
from src.config import Config

print(Config.DATABASE_URL)

engine = create_async_engine(
    url=Config.DATABASE_URL,
    echo=True
)

async def initdb():
    """create a connection to our db"""

    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)