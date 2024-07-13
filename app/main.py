from fastapi import FastAPI
from app.api.v1 import users, auth, content
from app.core.config import settings, setup_logging, setup_cors

# Set up logging
logger = setup_logging()

# Define lifespan event handlers
async def lifespan(app: FastAPI):
    logger.info("Starting up the application...")
    yield
    logger.info("Shutting down the application...")

app = FastAPI(lifespan=lifespan)

# Set up CORS
setup_cors(app)

app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(content.router, prefix="/api/v1/contents", tags=["contents"])

@app.get("/")
async def root():
    logger.info("Root endpoint accessed")
    return {"message": "Hello World"}
