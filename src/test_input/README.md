# Input Field Tests

This directory contains pytest test files for testing various input field types based on the QA Practice website requirements.

## Test Files

- `test_text_input.py` - Tests for text input field with validation for length and character restrictions
- `test_email_field.py` - Tests for email input field with email format validation
- `test_password_field.py` - Tests for password input field with strong password requirements

## Running the Tests

### Install dependencies
```bash
pip install pytest
```

### Run all tests
```bash
pytest src/test_input/
```

### Run specific test file
```bash
pytest src/test_input/test_text_input.py
pytest src/test_input/test_email_field.py
pytest src/test_input/test_password_field.py
```

### Run with verbose output
```bash
pytest src/test_input/ -v
```

### Run with coverage
```bash
pytest src/test_input/ --cov=src.test_input
```

## Test Coverage

The tests cover:
- **Positive tests**: Valid inputs that should be accepted
- **Negative tests**: Invalid inputs that should be rejected with appropriate error messages

Each test file includes mock form classes that simulate the behavior described in the QA Practice requirements.