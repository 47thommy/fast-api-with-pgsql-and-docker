from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

books = [
    {
        "id": "1",
        "title": "Think Python",
        "author": "Allen B. Downey",
        "publisher": "O'Reilly Media",
        "published_date": "2021-01-01",
        "page_count": 1234,
        "language": "English",
    },
    {
        "id": "2",
        "title": "Django By Example",
        "author": "Antonio Mele",
        "publisher": "Packt Publishing Ltd",
        "published_date": "2022-01-19",
        "page_count": 1023,
        "language": "English",
    },
    {
        "id": "3",
        "title": "The web socket handbook",
        "author": "Alex Diaconu",
        "publisher": "Xinyu Wang",
        "published_date": "2021-01-01",
        "page_count": 3677,
        "language": "English",
    },
    {
        "id": "4",
        "title": "Head first Javascript",
        "author": "Hellen Smith",
        "publisher": "Oreilly Media",
        "published_date": "2021-01-01",
        "page_count": 540,
        "language": "English",
    },
    {
        "id": "5",
        "title": "Algorithms and Data Structures In Python",
        "author": "Kent Lee",
        "publisher": "Springer, Inc",
        "published_date": "2021-01-01",
        "page_count": 9282,
        "language": "English",
    },
    {
        "id": "6",
        "title": "Head First HTML5 Programming",
        "author": "Eric T Freeman",
        "publisher": "O'Reilly Media",
        "published_date": "2011-21-01",
        "page_count": 3006,
        "language": "English",
    },
]


class Book (BaseModel):
    id:str
    title:str
    author:str
    publisher:str
    published_date:str
    page_count:int
    language:str
    
class updateBook(BaseModel):
    title:str
    author:str
    publisher:str
    page_count:int
    language:str
    
@app.get("/books", response_model=List[Book])
async def get_all_books():
    return books

@app.get("/books/{book_id}")
async def get_book_by_id(book_id:str):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books", status_code=201)
async def add_book(book:Book):
    new_book = book.model_dump()
    books.append(new_book)
    return new_book

@app.patch("/books/{book_id}")
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

@app.delete("/books/delete/{book_id}")
async def delete_book(book_id:str):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return book
    raise HTTPException(status_code=201, detail="book not found")


    
            
        