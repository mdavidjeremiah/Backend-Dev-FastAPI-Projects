"""
CRUD Package

Contains business logic for database operations (Create, Read, Update, Delete).
Each module provides pure functions that operate on database sessions.

This layer is independent of HTTP/FastAPI concerns, making it:
- Reusable across different interfaces (REST, GraphQL, CLI)
- Testable in isolation
- Easy to swap database implementations

Modules:
    todo: CRUD operations for Todo model
"""

from app.crud import todo

__all__ = ["todo"]
