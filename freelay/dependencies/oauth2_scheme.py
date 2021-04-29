from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hashed_password(password):
    return pwd_context.hash(password)
