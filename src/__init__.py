from src.books.routes import book_router
from src.auth.routes import auth_router
from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.db.main import initdb
# adding life span
@asynccontextmanager
async def life_span(app:FastAPI):
    await initdb()
    yield
    print("server is stopping")
version = "v1"
app = FastAPI(
    title="bookly",
    description="A RESTful API for a book review web service",
    version=version,
    lifespan=life_span
)

app.include_router(book_router, prefix=f"/api/{version}/books", tags={'books'})
app.include_router(auth_router, prefix=f"/api/{version}/auth")