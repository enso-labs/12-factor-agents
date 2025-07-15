"""
General utility functions and helpers.
"""
import json
import logging
from typing import Any, Dict, Optional


def setup_logging(level: str = "INFO") -> logging.Logger:
    """Set up basic logging configuration."""
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger(__name__)


def safe_json_load(data: str) -> Optional[Dict[str, Any]]:
    """Safely load JSON data with error handling."""
    try:
        return json.loads(data)
    except (json.JSONDecodeError, TypeError):
        return None


def safe_json_dump(data: Any, indent: int = 2) -> str:
    """Safely dump data to JSON string with error handling."""
    try:
        return json.dumps(data, indent=indent, default=str)
    except (TypeError, ValueError):
        return "{}"


def validate_required_fields(data: Dict[str, Any], required_fields: list) -> bool:
    """Validate that required fields are present in data."""
    return all(field in data and data[field] is not None for field in required_fields) 