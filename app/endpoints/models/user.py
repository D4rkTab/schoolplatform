from fastapi import APIRouter,  Depends
from app.core.db import schema, models
from app.dependencies.db import get_db
from app.core.db.crud import UserCrud

from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/users',
    tags=['users']
)

@router.post("/")
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)) -> schema.User:
    return UserCrud(db, models.User).create(user)
