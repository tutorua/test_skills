# That is a simple project to try skills for testing a web site using Playwright and Python


https://www.qa-practice.com/

## Installation

1. Create a project folder and cd into it
2. uv init --python 3.14
3. uv venv
5. uv add playwright
6. uv add pytest-playwright
7. uv add allure-pytest
8. playwright install

### Verifications:


## Execution

### Run all tests

pytest src/test_input/

### Run specific test file

pytest src/test_input/test_text_input.py -v

### Run the test and create allure report

python -m pytest src/test_input -v --alluredir allure-results
python -m pytest src/test_input/test_text_input.py -v --alluredir allure-results
python -m pytest src/test_input/test_email_field.py -v --alluredir allure-results


### Open Allure report

allure generate
allure open

or 
allure serve
