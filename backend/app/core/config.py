from typing import List
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Portfolio API"
    PROJECT_VERSION: str = "1.0.0"
    PROJECT_DESCRIPTION: str = "Backend API for Portfolio Website"
    API_V1_STR: str = "/api/v1"
    
    # CORS Configuration
    BACKEND_CORS_ORIGINS: List[str] = ["*"]
    

    # JWT Configuration
    SECRET_KEY: str = "your-secret-key-here"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # AI Configuration
    GEMINI_API_KEY: str = ""
    
    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()