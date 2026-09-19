from typing import Generator
from app.db.database import SessionLocal

def get_db() -> Generator:
    """
    Dependency that provides a database session per request.
    Ensures the session is closed after the request is finished.
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
