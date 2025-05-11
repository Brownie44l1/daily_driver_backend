from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum
from src.core.database import Base
from datetime import datetime
import enum

class Priority(enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    due_date = Column(DateTime, nullable=True)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    priority = Column(Enum(Priority), nullable=True)
    tags = Column(String, nullable=True)
    reminder_time = Column(DateTime, nullable=True)