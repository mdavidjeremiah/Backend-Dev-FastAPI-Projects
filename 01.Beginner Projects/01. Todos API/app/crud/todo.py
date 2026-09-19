from sqlalchemy.orm import Session
from app.models.todo import Todo
from app.schemas.todo import TodoCreate, TodoUpdate
from typing import Optional, List

def get_todo(db: Session, todo_id: int) -> Optional[Todo]:
    """Fetch a single todo by ID"""
    return db.query(Todo).filter(Todo.id == todo_id).first()

def get_todos(db: Session, skip: int = 0, limit: int = 100, completed: Optional[bool] = None) -> List[Todo]:
    """Fetch a list of todos with optional filtering and pagination"""
    query = db.query(Todo)
    if completed is not None:
        query = query.filter(Todo.completed == completed)
    return query.offset(skip).limit(limit).all()

def create_todo(db: Session, todo_in: TodoCreate) -> Todo:
    """Create a new todo item"""
    db_todo = Todo(**todo_in.model_dump())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(db: Session, db_todo: Todo, todo_in: TodoUpdate) -> Todo:
    """Update an existing todo item"""
    update_data = todo_in.model_dump(exclude_unset=True)  # Only update provided fields
    for field, value in update_data.items():
        setattr(db_todo, field, value)
    
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, db_todo: Todo) -> None:
    """Delete a todo item"""
    db.delete(db_todo)
    db.commit()
