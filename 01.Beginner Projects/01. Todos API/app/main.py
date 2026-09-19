from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.config import settings
from app.db.init_db import init_db
from app.api.v1 import todos

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup actions
    print(f"Starting {settings.APP_NAME}...")
    init_db()  # Create tables on startup
    yield
    # Shutdown actions
    print("Shutting down...")

app = FastAPI(
    title=settings.APP_NAME,
    lifespan=lifespan,
    debug=settings.DEBUG
)

# Register Routers
app.include_router(todos.router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": f"Welcome to {settings.APP_NAME}"}
