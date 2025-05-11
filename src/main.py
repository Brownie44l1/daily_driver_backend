from fastapi import FastAPI
from src.apps.todos.routers import router as todos_router
from src.core.database import Base, engine
from src.apps.todos.notifications import start_scheduler

app = FastAPI(title="Daily Driver Backend")

# Create database tables
Base.metadata.create_all(bind=engine)

# Include the todos router
app.include_router(todos_router, prefix="/todos", tags=["todos"])

# Start the notification scheduler
start_scheduler()

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "ok"}