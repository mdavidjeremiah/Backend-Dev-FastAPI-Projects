"""
API Package

Contains all HTTP layer concerns:
- Dependency injection functions (deps.py)
- Versioned API routes (v1/)

Submodules:
    deps: Shared FastAPI dependencies (get_db, etc.)
    v1: Version 1 API endpoints
"""

from app.api import deps

__all__ = ["deps"]
