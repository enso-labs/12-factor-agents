"""
Tests for configuration module.
"""
import pytest
from src.config import Config, config


def test_config_instance():
    """Test that config instance is created properly."""
    assert config is not None
    assert isinstance(config, Config)


def test_config_defaults():
    """Test that config has expected default values."""
    assert config.APP_NAME == "12-factor-agent-python-demo"
    assert config.APP_VERSION == "0.1.0"
    assert config.API_HOST == "localhost"
    assert config.API_PORT == 8000
    assert config.API_TIMEOUT == 30


def test_config_class():
    """Test Config class initialization."""
    test_config = Config()
    assert test_config.APP_NAME == "12-factor-agent-python-demo"
    assert test_config.DEBUG is False 