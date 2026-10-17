# UI Automation Framework: Playwright + Pytest + Page Object Model

Automated UI tests for the demo e-commerce site https://www.saucedemo.com
covering **login, product search/sorting, cart and checkout**.

## Tech stack
| Tool | What it does |
|---|---|
| Playwright | Controls a real browser (clicks, typing, reading text) |
| Pytest | Finds and runs the tests, reports pass/fail |
| Page Object Model | Design pattern: one class per web page |
| pytest-xdist | Runs tests in parallel to save time |
| pytest-html | Creates an HTML report |

## Project structure
```
pages/       Page Objects: locators + actions for each page (login, inventory, cart, checkout)
tests/       Test files: only "what should happen", no locators
test_data/   Inputs and expected messages, kept separate from test logic
config/      Environment settings (URLs)
conftest.py  Shared fixtures + screenshot-on-failure hook
pytest.ini   Pytest settings and markers
```

## Setup
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
```

## Run
```bash
pytest                          # all tests, headless
pytest --headed                 # watch the browser
pytest -m smoke                 # only smoke tests
pytest --env staging            # pick an environment
pytest -n 4                     # 4 tests at once (xdist)
pytest -n auto                  # use all CPU cores
```
Report: `reports/report.html`. Failure screenshots: `screenshots/`.

## Measuring the parallel speed-up (for your resume)
```bash
time pytest -n 0                # serial: note the total seconds (A)
time pytest -n 4                # parallel: note the total seconds (B)
```
Reduction % = (A - B) / A x 100. Run each 2-3 times and use the average.

## Key concepts
- **Locator**: a way to find an element (`#user-name`, `.inventory_item`).
- **Page Object**: a class that hides locators and exposes actions like `login()`.
- **Fixture**: reusable setup code; tests ask for it by naming it as an argument.
- **Parametrize**: run one test many times with different data.
- **Marker**: a label (`smoke`, `regression`) so you can run groups of tests.
- **Hook**: a pytest function that runs at a certain moment (we use one after each test to screenshot failures).
- **xdist**: splits tests across worker processes; tests must be independent so they can run in any order.
