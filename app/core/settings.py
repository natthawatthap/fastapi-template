# app/core/settings.py
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

class Settings:
    DATABASE_URL: str = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost/dbname')

settings = Settings()
