from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.products.db_model import BaseDB

DATABASE_URI = "sqlite://sql-lite/./todos.db"

engine = create_engine(DATABASE_URI)
BaseDB.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
