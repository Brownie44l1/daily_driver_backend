from apscheduler.schedulers.asyncio import AsyncIOScheduler
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import random
from src.apps.todos.crud import get_todos
from src.core.database import SessionLocal

def check_reminders():
    db = SessionLocal()
    try:
        # Get incomplete todos with due_date or reminder_time in the past
        todos = get_todos(db, skip=0, limit=100)
        for todo in todos:
            if todo.completed:
                continue
            if todo.due_date and todo.due_date <= datetime.utcnow():
                print(f"Reminder: '{todo.title}' is overdue! (Due: {todo.due_date})")
            elif todo.reminder_time and todo.reminder_time <= datetime.utcnow():
                print(f"Reminder: '{todo.title}' needs attention! (Reminder: {todo.reminder_time})")
    finally:
        db.close()

def start_scheduler():
    scheduler = AsyncIOScheduler()
    # Run check_reminders randomly every 1-5 minutes
    scheduler.add_job(
        check_reminders,
        "interval",
        minutes=random.randint(1, 5),
        next_run_time=datetime.utcnow() + timedelta(seconds=10)
    )
    scheduler.start()