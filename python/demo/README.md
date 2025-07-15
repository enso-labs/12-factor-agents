# 12-Factor Agent Python Demo

A simple Python project demonstration following 12-factor app principles, built with httpx for HTTP client functionality.

## Features

- Clean project structure following Python best practices
- Configuration management with environment variables
- Async HTTP client using httpx
- Modular design with services, models, and utilities
- Basic API routing framework
- Comprehensive test suite

## Project Structure

```
12-factor-agent-python-demo/
├── src/                    # Main application package
│   ├── __init__.py        # Package initialization
│   ├── main.py            # Application entry point
│   ├── config.py          # Configuration settings
│   ├── api/               # API endpoints and routing
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── models/            # Data models
│   │   ├── __init__.py
│   │   └── base.py
│   ├── services/          # Business logic
│   │   ├── __init__.py
│   │   └── base_service.py
│   ├── utils/             # Utility functions
│   │   ├── __init__.py
│   │   └── helpers.py
│   └── modules/           # Feature modules
│       └── __init__.py
├── tests/                 # Test suite
│   ├── __init__.py
│   ├── test_config.py
│   └── test_utils.py
├── docs/                  # Documentation
│   └── README.md
├── scripts/               # Utility scripts
│   └── setup.py
├── pyproject.toml         # Project configuration and dependencies
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd 12-factor-agent-python-demo
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -e .
   # or for development with all optional dependencies
   pip install -e ".[dev]"
   ```

4. **Run setup script** (optional)
   ```bash
   python scripts/setup.py
   ```

## Usage

### Running the Application

```bash
python src/main.py
```

### Configuration

The application uses environment variables for configuration:

- `DEBUG`: Enable debug mode (default: False)
- `API_HOST`: API host (default: localhost)
- `API_PORT`: API port (default: 8000)
- `API_KEY`: External API key
- `API_TIMEOUT`: HTTP client timeout in seconds (default: 30)
- `DATABASE_URL`: Database connection URL

### Example

```python
from src.config import config
from src.services.base_service import BaseService
from src.utils.helpers import setup_logging

# Set up logging
logger = setup_logging("INFO")

# Use configuration
print(f"App: {config.APP_NAME} v{config.APP_VERSION}")

# Use services
async with BaseService() as service:
    # Your async code here
    pass
```

## Development

### Running Tests

```bash
# Install development dependencies (includes pytest)
pip install -e ".[dev]"

# Run tests
pytest tests/
```

### Code Style

```bash
# Install development dependencies (includes formatting tools)
pip install -e ".[dev]"

# Format code
black src/ tests/
isort src/ tests/

# Lint code
flake8 src/ tests/
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run the test suite
6. Submit a pull request

## Author

Ryan Eggleston (ryan.adaptivebiz@gmail.com) 