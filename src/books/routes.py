from typing import List
from fastapi import FastAPI, HTTPException, APIRouter
from src.books.book_data import books
from src.books.schemas import Book, updateBook

book_router = APIRouter()
@book_router.get("/", response_model=List[Book])
async def get_all_books():
    return books

@book_router.get("/{book_id}")
async def get_book_by_id(book_id:str):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@book_router.post("/", status_code=201)
async def add_book(book:Book):
    new_book = book.model_dump()
    books.append(new_book)
    return new_book

@book_router.patch("/{book_id}")
async def update_book(book_id:str, update_book:updateBook):
    for book in books:
        if book["id"]==book_id:
            book["author"]=update_book.author
            book["publisher"]=update_book.publisher
            book["title"]=update_book.title
            book["page_count"]=update_book.page_count
            book["language"]=update_book.language
            return book
    return HTTPException(status_code=404, detail="book not found")

@book_router.delete("/delete/{book_id}")
async def delete_book(book_id:str):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return book
    raise HTTPException(status_code=201, detail="book not found")


    
            
        