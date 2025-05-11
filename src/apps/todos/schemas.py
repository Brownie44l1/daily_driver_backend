from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from src.apps.todos.models import Priority

class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    completed: Optional[bool] = False
    priority: Optional[Priority] = None
    tags: Optional[str] = None
    reminder_time: Optional[datetime] = None

class Todo(TodoCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True