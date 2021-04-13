from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from . import methods, schemas
from freelay.dependencies import get_db


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("", response_model=List[schemas.User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return methods.get_all_users(db, skip, limit)


@router.get("/{user_id:int}", response_model=schemas.User)
def get_user_by_id(user_id, db: Session = Depends(get_db)):
    return methods.get_user_by_id(db, user_id)


@router.post("", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return methods.create_user(db, user)


@router.post("/{user_id:int}/emails", response_model=schemas.User)
def create_email_for_user(user_id, email: schemas.EmailCreate,  db: Session = Depends(get_db)):
    return methods.create_user_email(db, email, user_id)


@router.post("/{user_id:int}/emails/generate", response_model=schemas.Email)
def generate_email_for_user(user_id,  db: Session = Depends(get_db)):
    return methods.generate_email_for_user(db, user_id)


@router.get("/emails", response_model=List[schemas.Email], tags=["Email"])
def get_emails(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    emails = methods.get_all_emails(db, skip=skip, limit=limit)
    return emails
