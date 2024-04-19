from functools import wraps

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

SQLALCHEMY_DATABASE_URI = "postgresql://postgres:1234@localhost:5432/TMS"

engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def inject(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        db = SessionLocal()
        try:
            return func(*args, **kwargs, db=db)
        finally:
            db.close()
    return wrapper
