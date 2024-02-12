from sqlalchemy.orm import Session
from pydantic import BaseModel

from . import models, schema, database

class CrudBase:
    def __init__(self, db: Session, model: database.Base) -> None:
        self.db = db
        self.model = model
    
    
    def findAll(self, skip: int = 0, limit: int = 100):
        return self.db.query(self.model).offset(skip).limit(limit).all()

    
    def findById(self, id):
        return self.db.query(self.model).filter(self.model.id == id).first()
    
    


class ItemCrud(CrudBase):
    def __init__(self, db: Session, model: models.Item) -> None:
        self.db = db
        self.model = model
        super()
    def create(self, item: schema.ItemCreate, user_id: int = 1) -> schema.Item:
        db_item = models.Item(**item.dict(), owner_id = user_id)
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item

class UserCrud(CrudBase):
    def __init__(self, db: Session, model: models.User) -> None:
        self.db = db
        self.model = model
        super()
    def create(self, user: schema.UserCreate) -> schema.User:
        hash_password = "somefakehash_"+user.password
        db_user = models.User(email = user.email, hashed_password = hash_password)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
