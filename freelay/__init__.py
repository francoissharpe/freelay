from typing import Optional

from fastapi import FastAPI

from .api import router as api_router
from .db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Freelay")

app.include_router(api_router)


