from typing import List
from fastapi import APIRouter, HTTPException, Depends
from src.books.book_data import books
from src.books.schemas import Book, updateBook
from src.db.main import get_session
from src.books.service import BookService
from sqlmodel.ext.asyncio.session import AsyncSession
from src.books.schemas import BookCreateModel
book_router = APIRouter()
book_service = BookService()


@book_router.get("/")
async def get_all_books(session:AsyncSession = Depends(get_session)):
    books = await book_service.get_all_books(session=session)
    return books

@book_router.get("/{book_id}")
async def get_book_by_id(book_id:str, session:AsyncSession = Depends(get_session)):
    book = await book_service.get_book(book_id=book_id, session=session)
    if book:
        return book
    else:
        raise HTTPException(status_code=404, detail="Book not found")

@book_router.post("/", status_code=201)
async def add_book(book:BookCreateModel, session:AsyncSession = Depends(get_session)):
    new_book = await book_service.create_book(book_data=book, session=session)
    return new_book

@book_router.patch("/{book_id}")
async def update_book(book_id:str, update_book:updateBook, session:AsyncSession = Depends(get_session)):
    updated_book = await book_service.update_book(book_id=book_id, update_data=update_book, session=session)
    if updated_book is not None:
        return update_book
    else:
        raise HTTPException(status_code=404, detail="book not found")

@book_router.delete("/{book_id}")
async def delete_book(book_id:str, session:AsyncSession = Depends(get_session)):
    deleted_book = await book_service.delete_book(book_id=book_id, session=session)
    
    if deleted_book is not None:
        return deleted_book
    else:
        raise HTTPException(status_code=404, detail="book not found")

    
            
        