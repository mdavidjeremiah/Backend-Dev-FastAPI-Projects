"""
Database Package

Handles database connection, session management, and initialization.

Modules:
    database: SQLAlchemy engine, session factory, and Base class
    init_db: Database initialization (table creation)
"""

from app.db.database import Base, SessionLocal, engine
from app.db.init_db import init_db

__all__ = [
    "Base",
    "SessionLocal",
    "engine",
    "init_db",
]
