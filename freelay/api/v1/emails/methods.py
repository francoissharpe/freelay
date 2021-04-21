import logging
from typing import Optional

from sqlalchemy.orm import Session

from freelay.api.v1.users.models import User, Email


def get_email_from_address(db: Session, email: str) -> Optional[Email]:
   return db.query(Email).filter_by(address=email).one_or_none()


def get_user_from_email(db: Session, email: Email) -> Optional[User]:
    return db.query(User).get(email.owner_id)


def get_user_from_hook(db: Session, recipient: str) -> Optional[User]:
    email = get_email_from_address(db, recipient)
    if email:
        user = get_user_from_email(db, email)
        if user:
            logging.info(f"Email [{email.address}] belongs to \"{user.email}\"")
            return user
        logging.warning(f"Unable to find owner of email [{email.address}] with owner_id={email.owner_id}")
    logging.warning(f"Email [{recipient}] is not assigned to a user. Ignoring...")
