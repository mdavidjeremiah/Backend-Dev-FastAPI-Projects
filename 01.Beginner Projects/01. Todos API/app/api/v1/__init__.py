"""
API Version 1 Package

Contains all version 1 API route handlers.

Each module corresponds to a specific resource:
    todos: To-Do List endpoints (/api/v1/todos)
    notes: Notes endpoints (/api/v1/notes) - Coming in Project 2
    users: Users endpoints (/api/v1/users) - Coming in Project 3
    recipes: Recipes endpoints (/api/v1/recipes) - Coming in Project 4
    courses: Courses endpoints (/api/v1/courses) - Coming in Project 5

Routers are registered in app/main.py with the /api/v1 prefix.
"""

from app.api.v1 import todos

__all__ = ["todos"]
