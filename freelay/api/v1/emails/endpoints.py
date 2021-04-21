import logging

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from . import methods, schemas
from freelay.dependencies import get_db


router = APIRouter(
    prefix="/emails",
    tags=["Emails"],
)


@router.post("/incoming")
def incoming_email(email: schemas.CloudMailIn, db: Session = Depends(get_db)):
    methods.get_user_from_hook(db, email.envelope.to_address)
    return Response(status_code=status.HTTP_200_OK)
