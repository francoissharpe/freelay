from functools import lru_cache
import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Freelay"
    secret_key = os.environ.get("API_TOKEN_SECRET_KEY") or "secret"
    algorithm = os.environ.get("API_TOKEN_ALGORITHM") or "HS256"
    access_token_expire_minutes = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES") or 60


@lru_cache()
def get_settings():
    return Settings()
