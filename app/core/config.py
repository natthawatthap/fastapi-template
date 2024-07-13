import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("app.log"),
            logging.StreamHandler()
        ]
    )
    logger = logging.getLogger(__name__)
    return logger

def setup_cors(app: FastAPI):
    origins = [
        "http://localhost",
        "http://localhost:8000",
        "http://yourfrontenddomain.com",  # Add any other domains you want to allow
    ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
