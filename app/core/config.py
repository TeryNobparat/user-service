import os
from dotenv import load_dotenv

load_dotenv()

class Settings:

    APP_NAME: str = os.getenv("APP_NAME", "User Service")
    APP_VERSION: str = os.getenv("APP_VERSION", "1.0.0")    
    DEBUG: bool = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
    API_V1_STR: str = os.getenv("API_V1_STR", "/api/v1")
    BACKEND_CORS_ORIGINS: list[str] = ["*"]  # Allow all origins for simplicity
    DATABASE_URL: str = os.getenv("DATABASE_URL", "mssql+pyodbc://sa:sqladmin@srt02fa018/FA_Waste?driver=ODBC+Driver+17+for+SQL+Server")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecretkey")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

settings = Settings()