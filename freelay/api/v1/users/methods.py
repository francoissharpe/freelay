import string, secrets

from sqlalchemy.orm import Session

from . import models, schemas


def get_all_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_all_emails(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Email).offset(skip).limit(limit).all()


def get_user_by_id(db: Session, _id: int):
    return db.query(models.User).get(_id)


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).one()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_user_email(db: Session, email: schemas.EmailCreate, user_id: int):
    db_email = models.Email(**email.dict(), owner_id=user_id)
    db.add(db_email)
    db.commit()
    db.refresh(db_email)
    return db_email


def get_random_string(n=32):
    
    return ''.join(secrets.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(n))


def generate_unique_email(db: Session, n=32, domain="freelay.com"):
    email = get_random_string(n)
    while db.query(models.Email).filter_by(address=email).one_or_none():
        print(email)
        email = get_random_string(n)
    return f"{email}@{domain}"


def generate_email_for_user(db: Session, user_id: int):
    db_email = models.Email(address=generate_unique_email(db), owner_id=user_id)
    db.add(db_email)
    db.commit()
    db.refresh(db_email)
    return db_email
