from fastapi import Request
from fastapi.responses import JSONResponse
from app.exceptions.custom_exceptions import CustomException


def custom_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=exc.code,
        content={"error_code": exc.error_code, "message": exc.message},
    )
