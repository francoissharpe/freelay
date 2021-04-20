from fastapi import APIRouter

from .emails.endpoints import router as email_router
from .users.endpoints import router as user_router


router = APIRouter(prefix="/v1")
router.include_router(user_router)
router.include_router(email_router)
