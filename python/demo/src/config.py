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
    
    # LLM settings
    LLM_MODEL: str = os.getenv("LLM_MODEL", "gpt-4o-mini")
    LLM_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    LLM_BASE_URL: str = os.getenv("LLM_BASE_URL", "https://api.openai.com/v1/chat/completions")
    LLM_TIMEOUT: int = int(os.getenv("LLM_TIMEOUT", "30"))


# Global config instance
config = Config()
