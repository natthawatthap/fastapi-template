from fastapi import FastAPI

def create_start_app_handler(app: FastAPI):
    async def start_app() -> None:
        # Custom startup logic here
        pass
    return start_app

def create_stop_app_handler(app: FastAPI):
    async def stop_app() -> None:
        # Custom shutdown logic here
        pass
    return stop_app
