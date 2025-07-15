"""
API routes and endpoints.
"""
from typing import Dict, Any


class APIRouter:
    """Simple API router for handling endpoints."""
    
    def __init__(self):
        """Initialize the router."""
        self.routes = {}
    
    def add_route(self, path: str, handler, method: str = "GET"):
        """Add a route to the router."""
        if path not in self.routes:
            self.routes[path] = {}
        self.routes[path][method] = handler
    
    def get_handler(self, path: str, method: str = "GET"):
        """Get handler for a specific path and method."""
        return self.routes.get(path, {}).get(method)


# Basic health check endpoint
def health_check() -> Dict[str, Any]:
    """Health check endpoint."""
    return {"status": "healthy", "service": "12-factor-agent-python-demo"}


# Initialize router
router = APIRouter()
router.add_route("/health", health_check) 