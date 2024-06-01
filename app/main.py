from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from app.config.config import settings
from app.router import qa
from app.exceptions.handlers import custom_exception_handler
from app.exceptions.custom_exceptions import CustomException

app = FastAPI()

app.include_router(qa.router)

app.add_exception_handler(Exception, custom_exception_handler)


@app.on_event("startup")
async def startup_event():
    print(f"Starting up in {settings.Config.env_file} environment")
