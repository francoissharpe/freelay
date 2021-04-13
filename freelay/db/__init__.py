import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


if os.environ.get("SQLALCHEMY_DATABASE_URI"):
    SQLALCHEMY_DATABASE_URL = os.environ.get("SQLALCHEMY_DATABASE_URI")
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
else:
    engine = create_engine(
        "sqlite:///./sql_app.db", connect_args={"check_same_thread": False}
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
