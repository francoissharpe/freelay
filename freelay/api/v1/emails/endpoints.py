import logging

from fastapi import APIRouter, Response, status

from . import schemas


router = APIRouter(
    prefix="/emails",
    tags=["Emails"],
)


@router.post("/incoming")
def incoming_email(email: schemas.CloudMailIn):
    logging.info(email.json())
    print(email.json())
    return Response(status_code=status.HTTP_200_OK)
