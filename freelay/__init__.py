import logging
import sys

from fastapi import FastAPI

from .api import router as api_router
from .db import Base, engine

root = logging.getLogger()
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Freelay")

app.include_router(api_router)
