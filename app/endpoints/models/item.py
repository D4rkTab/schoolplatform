from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.db.crud import ItemCrud
from app.dependencies.db import get_db
from app.core.db import models
from app.core.db import schema
router = APIRouter(
    prefix="/items",
    tags=["items"]
)



@router.get("/")
def get_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return ItemCrud(db, models.Item).findAll(skip, limit)

@router.post("/")
def create_item(item: schema.ItemCreate, owner_id: int = 1, db: Session = Depends(get_db)) -> schema.Item:
    return ItemCrud(db, models.Item).create(item, owner_id)


