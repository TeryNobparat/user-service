from pydantic_settings import BaseSettings
from .logger import AppLogger



class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str
    DEBUG: bool
    API_V1_STR: str
    BACKEND_CORS_ORIGINS: list[str] = ["*"]  # Allow all origins for simplicity
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"

settings = Settings()