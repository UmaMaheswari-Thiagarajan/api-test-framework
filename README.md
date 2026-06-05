# API Test Automation Framework

A production-style REST API test automation framework built with Python, pytest, and requests.

## Tech Stack
- Python 3.14
- pytest
- requests
- pytest-html

## Project Structure
- `tests/` - Test files (positive, negative scenarios)
- `services/` - Service layer for API calls
- `utils/` - Reusable helper functions
- `conftest.py` - Shared pytest fixtures

## How to Run

### Install dependencies
pip install -r requirements.txt

### Run all tests
pytest

### Run with HTML report
pytest --html=report.html

## Test Coverage
- 21 test cases across Posts and Users endpoints
- GET, POST, PUT, DELETE operations
- Positive and negative scenarios
- Response structure validation