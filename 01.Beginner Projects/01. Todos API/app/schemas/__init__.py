"""
Schemas Package

Contains all Pydantic schemas used for:
- Request body validation (Input schemas)
- Response serialization (Output schemas)
- Data transfer between layers

Schemas:
    todo: Todo schemas (TodoBase, TodoCreate, TodoUpdate, TodoResponse)
"""

from app.schemas.todo import (
    TodoBase,
    TodoCreate,
    TodoUpdate,
    TodoResponse,
)

__all__ = [
    "TodoBase",
    "TodoCreate",
    "TodoUpdate",
    "TodoResponse",
]
