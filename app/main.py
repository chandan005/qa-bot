from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from app.core.config import settings
from app.routers import qa
from app.exceptions.handlers import http_exception_handler, custom_exception_handler
from app.exceptions.custom_exceptions import CustomException

app = FastAPI()

app.include_router(qa.router)

app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(CustomException, custom_exception_handler)


@app.on_event("startup")
async def startup_event():
    print(f"Starting up in {settings.Config.env_file} environment")
