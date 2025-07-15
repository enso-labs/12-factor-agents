"""
Tests for utility functions.
"""
import pytest
from src.utils.helpers import safe_json_load, safe_json_dump, validate_required_fields


def test_safe_json_load():
    """Test safe JSON loading function."""
    # Valid JSON
    result = safe_json_load('{"key": "value"}')
    assert result == {"key": "value"}
    
    # Invalid JSON
    result = safe_json_load('invalid json')
    assert result is None


def test_safe_json_dump():
    """Test safe JSON dumping function."""
    data = {"key": "value"}
    result = safe_json_dump(data)
    assert '"key": "value"' in result


def test_validate_required_fields():
    """Test required fields validation."""
    data = {"name": "test", "age": 25}
    
    # All required fields present
    assert validate_required_fields(data, ["name", "age"]) is True
    
    # Missing required field
    assert validate_required_fields(data, ["name", "email"]) is False
    
    # Empty data
    assert validate_required_fields({}, ["name"]) is False 