from typing import List
from fastapi import HTTPException, Depends, status
from sqlalchemy.orm import Session
from database import get_db
import model
import Schema
from fastapi import APIRouter
router = APIRouter(
    prefix='/users',
    tags=['Users']
)


@router.get('/', response_model=List[Schema.createUserDto])
def test_users(db: Session = Depends(get_db)):
    user = db.query(model.User).all()

    return user


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=List[Schema.createUserDto])
def create_users(user_create: Schema.createUserDto, db: Session = Depends(get_db)):
    new_user = model.User(**user_create.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return [new_user]