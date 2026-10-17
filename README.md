# SauceDemo UI Automation Framework

A Python-based UI automation framework for [SauceDemo](https://www.saucedemo.com/) using **Playwright, Pytest, and the Page Object Model (POM)**.

The framework automates key e-commerce flows and validates login behavior, product visibility, product sorting, cart operations, and checkout functionality.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Test automation language |
| Playwright | Browser automation and UI interactions |
| Pytest | Test execution, assertions, and fixtures |
| Page Object Model (POM) | Separates page interactions from test logic |
| pytest-html | Generates HTML test reports |
| pytest-xdist | Parallel test execution, if configured |

## Features

- Automated login tests
- Product visibility and inventory validation
- Product sorting by name and price
- Shopping cart tests
- Checkout workflow tests
- Reusable page objects and shared fixtures
- Smoke and regression test markers
- HTML test reporting
- Screenshot capture on test failures, if configured

## Project Structure

```text
project-2-saucedemo-ui-automation/
├── config/
│   ├── __init__.py
│   └── settings.py
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── test_data/
│   ├── __init__.py
│   └── data.py
├── tests/
│   ├── __init__.py
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   └── test_checkout.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Prerequisites

- Python 3.10 or a compatible version for the dependencies
- pip
- Git
- A supported browser installed by Playwright

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/AtharvaN11/project-2-saucedemo-ui-automation.git
cd project-2-saucedemo-ui-automation
```

### 2. Create and activate a virtual environment

**Windows PowerShell**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies and browser

```bash
python -m pip install -r requirements.txt
playwright install chromium
```

## Running Tests

Run the complete test suite:

```bash
pytest
```

Run tests with verbose output:

```bash
pytest -v
```

Run tests with the browser visible, if supported by the project configuration:

```bash
pytest --headed
```

Run smoke tests:

```bash
pytest -m smoke
```

Run regression tests:

```bash
pytest -m regression
```

Generate an HTML report, if the pytest-html plugin is installed:

```bash
pytest --html=reports/report.html --self-contained-html
```

If the `reports` directory does not exist, create it before running the command:

```powershell
New-Item -ItemType Directory -Force reports
```

## Test Reports and Screenshots

- **HTML report:** `reports/report.html`, when generated using the command above.
- **Failure screenshots:** `screenshots/`, if screenshot capture is configured in the test hooks.

Generated reports and screenshots may be excluded from Git using `.gitignore`.

## Framework Design

- **Page Object Model:** Each page class encapsulates relevant locators and page actions.
- **Fixtures:** Shared setup and browser/page resources are provided through `conftest.py`.
- **Parametrization:** Runs the same test against multiple data inputs.
- **Markers:** Organizes tests into smoke and regression groups.
- **Assertions:** Checks that actual UI behavior matches expected results.

## Future Improvements

- Add cross-browser execution.
- Integrate the test suite into a CI/CD pipeline.
- Add structured logging and richer failure diagnostics.
- Configure parallel execution after verifying test independence.

## Author

**Atharva Prakash Nandgaonkar**

GitHub: [AtharvaN11](https://github.com/AtharvaN11)
