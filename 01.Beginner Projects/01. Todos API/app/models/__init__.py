"""
Models Package

Contains all SQLAlchemy ORM models representing database tables.

Important: All models must be imported here so that SQLAlchemy's 
Base.metadata knows about them when creating tables.

Models:
    todo: Todo model for task management
"""

from app.models.todo import Todo

__all__ = ["Todo"]
