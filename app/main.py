from typing import List

from fastapi import FastAPI
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from app.router import qa
# from app.exception.handlers import custom_exception_handler
from app.exception.custom_exceptions import CustomException
from app.middleware.response_logger import ResponseLoggerMiddleware

app = FastAPI()

def init_routers(app_: FastAPI) -> None:
    app.include_router(qa.router)

def init_listeners(app_: FastAPI) -> None:
    @app_.exception_handler(CustomException)
    async def custom_exception_handler(request: Request, exc: CustomException):
        return JSONResponse(
            status_code=exc.code,
            content={"error_code": exc.error_code, "message": exc.message},
        )

# app.add_exception_handler(Exception, custom_exception_handler)

def make_middleware() -> List[Middleware]:
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
        Middleware(ResponseLoggerMiddleware),
    ]
    return middleware

def create_app() -> FastAPI:
    app_ = FastAPI(
        title="QA Bot App",
        description="QA Bot App",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
        middleware=make_middleware(),
    )
    init_routers(app_=app_)
    init_listeners(app_=app_)
    return app_

app = create_app()
