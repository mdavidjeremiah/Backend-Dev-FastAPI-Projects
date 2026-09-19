from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.api.deps import get_db
from app.schemas.todo import TodoCreate, TodoUpdate, TodoResponse
from app.crud import todo as crud_todo

router = APIRouter(prefix="/todos", tags=["Todos"])

@router.post("", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
def create_todo(todo_in: TodoCreate, db: Session = Depends(get_db)):
    """Create a new to-do item"""
    return crud_todo.create_todo(db=db, todo_in=todo_in)

@router.get("", response_model=List[TodoResponse])
def read_todos(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    completed: Optional[bool] = Query(None, description="Filter by completion status"),
    db: Session = Depends(get_db)
):
    """Get a list of to-do items with pagination and filtering"""
    return crud_todo.get_todos(db=db, skip=skip, limit=limit, completed=completed)

@router.get("/{todo_id}", response_model=TodoResponse)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    """Get a specific to-do item by ID"""
    db_todo = crud_todo.get_todo(db=db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Todo with id {todo_id} not found"
        )
    return db_todo

@router.put("/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, todo_in: TodoUpdate, db: Session = Depends(get_db)):
    """Update an existing to-do item"""
    db_todo = crud_todo.get_todo(db=db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Todo with id {todo_id} not found"
        )
    return crud_todo.update_todo(db=db, db_todo=db_todo, todo_in=todo_in)

@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    """Delete a to-do item"""
    db_todo = crud_todo.get_todo(db=db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Todo with id {todo_id} not found"
        )
    crud_todo.delete_todo(db=db, db_todo=db_todo)
    return None
