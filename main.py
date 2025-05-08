import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.api.routers.router import api_router
from app.core.config import settings
from app.models import *
from app.core.database import Base, engine
from app.core.logger import AppLogger

log = AppLogger(settings.APP_NAME).get_logger()
Base.metadata.create_all(bind=engine)

def get_app() -> FastAPI:
    log.info("Starting process....")
    application = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION, debug=settings.DEBUG)

    if settings.BACKEND_CORS_ORIGINS:
        application.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    application.include_router(api_router, prefix=settings.API_V1_STR)
    return application

app = get_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)