from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    # Environment
    environment: str = "development"
    
    # Server Configuration
    host: str = "127.0.0.1"
    port: int = 8000
    
    # CORS Configuration
    cors_origins: str = "http://localhost:3000"
    
    # API Configuration
    api_v1_prefix: str = "/api/v1"
    
    @property
    def cors_origins_list(self) -> List[str]:
        """Convert comma-separated CORS origins string to list"""
        return [origin.strip() for origin in self.cors_origins.split(",")]
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()

