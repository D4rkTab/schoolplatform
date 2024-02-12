from fastapi import APIRouter
from .models.item import router as itemRouter
from .models.user import router as userRouter
router = APIRouter(
    prefix="/api/v1",
    tags=["api"]
)

router.include_router(itemRouter)
router.include_router(userRouter)
