"""
Base service classes.
"""
import httpx
from src.config import config


class BaseService:
    """Base service class for business logic operations."""
    
    def __init__(self):
        """Initialize the service."""
        self.config = config
        self.client = httpx.AsyncClient(timeout=config.API_TIMEOUT)
    
    async def __aenter__(self):
        """Async context manager entry."""
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.client.aclose()
    
    async def close(self):
        """Close the service and cleanup resources."""
        await self.client.aclose() 