from src.books.routes import book_router
from fastapi import FastAPI
version = "v1"
app = FastAPI(
    title="bookly",
    description="A RESTful API for a book review web service",
    version=version
)

app.include_router(book_router, prefix=f"/api/{version}/books", tags={'books'})