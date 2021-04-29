from fastapi import APIRouter

from .emails.endpoints import router as email_router
from .token.endpoints import router as token_router
from .users.endpoints import router as user_router


router = APIRouter(prefix="/v1")
router.include_router(email_router)
router.include_router(token_router)
router.include_router(user_router)
