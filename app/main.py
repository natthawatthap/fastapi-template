from fastapi import FastAPI
from app.api.v1 import users, auth, content
from app.core.config import setup_logging, setup_cors
from app.core.settings import settings
from app.core.events import create_start_app_handler, create_stop_app_handler
from app.core.exceptions import setup_exception_handlers

# Set up logging
logger = setup_logging()

app = FastAPI()

# Set up CORS
setup_cors(app)

# Set up exception handlers
setup_exception_handlers(app)

# Add startup and shutdown events
app.add_event_handler("startup", create_start_app_handler(app))
app.add_event_handler("shutdown", create_stop_app_handler(app))

app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(content.router, prefix="/api/v1/contents", tags=["contents"])

@app.get("/")
async def root():
    logger.info("Root endpoint accessed")
    return {"message": "Hello World"}
