from datetime import datetime
from sqlmodel.ext.asyncio.session import AsyncSession
from src.books.models import Book
from src.books.schemas import BookCreateModel
from sqlmodel import desc, select



class BookService:
    
    async def get_all_books(self,session:AsyncSession):
        
        statement = select(Book).order_by(desc(Book.created_at))
        result = await session.exec(statement)
        return result.all()

    async def create_book(self, session:AsyncSession, book_data:BookCreateModel):
        book_data_dict = book_data.model_dump()
        
        new_book = Book(
            **book_data_dict
        )
        
        new_book.published_date = datetime.strptime(book_data_dict['published_date'],"%Y-%m-%d")

        session.add(new_book)

        await session.commit()

        return new_book
    
    async def get_book(self, session:AsyncSession, book_id:str):
        
        statement = select(Book).where(Book.uid == book_id)
        result = await session.exec(statement)
        book= result.first()
        return book if book is not None else None
    
    
    
    async def update_book(self, session:AsyncSession, book_id:str,update_data:BookCreateModel ):
        
        book_to_update = await self.get_book(book_id, session)
        
        if book_to_update is not None:
            update_data_dict = update_data.model_dump()
            
            for k,v in update_data_dict.items():
                setattr(book_to_update,k,v)
            await session.commit(book_to_update)
            return book_to_update
        else:
            return None
    async def delete_book(self, session:AsyncSession, book_id:str):
        book_to_delete = await self.get_book(book_id, session)
        if book_to_delete is not None:
            await session.delete(book_to_delete)
            await session.commit
            return book_to_delete
        else:
            return None