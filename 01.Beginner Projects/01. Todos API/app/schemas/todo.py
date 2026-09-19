from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# Base schema: Shared fields
class TodoBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, description="The title of the task")
    description: Optional[str] = Field(None, max_length=500, description="Optional task details")

# Schema for creating a todo (Input)
class TodoCreate(TodoBase):
    pass

# Schema for updating a todo (Input - all fields optional)
class TodoUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    completed: Optional[bool] = None

# Schema for returning a todo (Output)
class TodoResponse(TodoBase):
    id: int
    completed: bool
    created_at: datetime
    
    class Config:
        from_attributes = True  # Allows Pydantic to read SQLAlchemy models
