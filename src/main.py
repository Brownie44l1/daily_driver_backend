from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.apps.todos.routers import router as todos_router
from src.core.database import Base, engine
from src.apps.todos.notifications import start_scheduler

app = FastAPI(title="Daily Driver Backend")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://daily-driver-frontend.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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