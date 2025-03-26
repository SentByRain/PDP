import os
import time
import traceback

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from sqlalchemy.exc import SQLAlchemyError
from contextlib import asynccontextmanager

from src.config import CONFIG
from src.logger import logger
from src.models import Base
from src.database_control.db import engine
from src.database_control.s3 import MinioHandler



from src.routers import user_router
from src.routers import mail_router
from src.routers import lesson_router
# from src.routers import files_router


# routers = [schedule_router, user_router, mail_router, files_router]
class CustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):

        start_time = time.time()

        response = await call_next(request)

        end_time = time.time()
        time_taken = end_time - start_time

        logger.info(
            "\nЗакончили запрос",
            extra={
                "http_status_code": response.status_code,
                "time_taken": time_taken,
                "method": request.method,
                "host": request.url.netloc,
                "path": request.url.path,
            },
        )

        logger.dump()

        return response



@asynccontextmanager
async def lifespan(app: FastAPI):
    # Создаем таблицы при запуске приложения
    try:
        Base.metadata.create_all(bind=engine)
        print("Tables created successfully.")
    except SQLAlchemyError as e:
        print(f"Error creating tables: {e}")

    # Создаем бакет с файлами
    try:
        MinioHandler(bucket=CONFIG.MINIO_FILES_BUCKET_NAME)
    except Exception as e:
        raise e

    yield  # Proceed to app lifecycle


app = FastAPI(
    title="PDP",
    root_path="/pdp",
    description="Сервис для управления рассписанием уроков",
    lifespan=lifespan
)
app.add_middleware(CustomMiddleware)

app.include_router(user_router)
app.include_router(mail_router)
app.include_router(lesson_router)


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    tb_str = "".join(traceback.format_exception(type(exc), exc, exc.__traceback__))
    logger.error(f"""Exception detail: {exc.detail}\nTraceback: {tb_str}""")
    return JSONResponse(
        status_code=exc.status_code, content={"message": f"{exc.detail}"}
    )

@app.get("/actuator/health/liveness", status_code=200)
def liveness_check():
    return "Liveness check succeeded."


@app.get("/actuator/health/readiness", status_code=200)
def readiness_check():
    return "Service is ready"
 
