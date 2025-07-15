"""
Configuration settings for the application.
"""
import os
from typing import Optional


class Config:
    """Basic configuration class for application settings."""
    
    # Application settings
    APP_NAME: str = "12-factor-agent-python-demo"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    
    # API settings
    API_HOST: str = os.getenv("API_HOST", "localhost")
    API_PORT: int = int(os.getenv("API_PORT", "8000"))
    
    # Database settings (if needed)
    DATABASE_URL: Optional[str] = os.getenv("DATABASE_URL")
    
    # External API settings
    API_KEY: Optional[str] = os.getenv("API_KEY")
    API_TIMEOUT: int = int(os.getenv("API_TIMEOUT", "30"))


# Global config instance
config = Config()
