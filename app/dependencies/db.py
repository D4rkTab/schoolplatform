from app.core.db import crud, models, schema
from app.core.db.database import SessionLocal, engine

#models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

