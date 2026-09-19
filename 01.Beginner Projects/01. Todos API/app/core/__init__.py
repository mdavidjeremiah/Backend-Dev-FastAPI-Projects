"""
Core Package

Contains application-wide configuration and utility functions.

Modules:
    config: Application settings loaded from environment variables
"""

from app.core.config import settings

__all__ = ["settings"]
