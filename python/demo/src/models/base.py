"""
Base model classes.
"""
from typing import Dict, Any


class BaseModel:
    """Base model class for data entities."""
    
    def __init__(self, **kwargs):
        """Initialize model with keyword arguments."""
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert model to dictionary."""
        return {
            key: value for key, value in self.__dict__.items()
            if not key.startswith('_')
        }
    
    def __str__(self) -> str:
        """String representation of the model."""
        return f"{self.__class__.__name__}({self.to_dict()})" 