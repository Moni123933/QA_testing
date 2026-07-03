# Tichi App Login Automation Framework

This project contains an automated test suite for the **Login** functionality of the Tichi web application (`https://tichi-app-webapp-stage.web.app`) using Python, Selenium WebDriver, and Pytest. The automation codebase implements the **Page Object Model (POM)** architectural pattern.

---

## 1. Directory Structure

```text
qa_test/
│
├── config/
│   └── config.py          # Centralized configuration variables (URL, timeouts, test credentials)
│
├── pages/
│   ├── base_page.py       # Reusable driver wrappers (clicks, typing, explicit waits)
│   └── login_page.py      # POM class representing Login page locators and actions
│
├── tests/
│   ├── conftest.py        # Pytest setup/teardown fixture for Chrome WebDriver instance
│   └── test_login.py      # Test cases (successful login, invalid password, malformed email)
│
├── manual_tests/
│   └── test_cases.md      # Excel/Sheets-ready manual test cases suite
│
├── defect_reports/
│   └── BUG_001_invalid_email_login.md  # Formal defect report for invalid email login bug
│
├── pytest.ini             # Pytest configurations and cli log settings
├── requirements.txt       # Python package dependencies list
└── README.md              # Framework configuration & reporting guide
```

---

## 2. Environment Setup

### Prerequisite
Ensure you have **Python 3.8 or higher** installed on your system.

### Installation Steps
1. Navigate to the root directory `qa_test`.
2. Install the required libraries using pip:
   ```bash
   pip install -r requirements.txt
   ```
   *Note: This will install Selenium, Pytest, `pytest-html` for basic HTML reporting, `allure-pytest` for advanced dashboard reporting, and `webdriver-manager` to handle Chrome Driver installations automatically.*

---

## 3. Configuration & Locators
Before running tests, configure your settings in [config/config.py](file:///f:/moniclg/qa_test/config/config.py):
*   Change the values of `VALID_EMAIL` and `VALID_PASSWORD` to your own test credentials (or set environment variables `TICHI_VALID_EMAIL` and `TICHI_VALID_PASSWORD`).
*   Verify and update the locators in [pages/login_page.py](file:///f:/moniclg/qa_test/pages/login_page.py) (e.g. `EMAIL_INPUT`, `PASSWORD_INPUT`, `LOGIN_BUTTON`) to match the exact HTML element tags/IDs in the application's DOM.

---

## 4. Running Tests & Generating Reports

You can choose between a standard HTML report or an advanced interactive Allure report.

### Option A: Standard Pytest-HTML Report
To run all tests and generate a clean, standalone, self-contained HTML test report:
```bash
pytest --html=reports/report.html --self-contained-html
```
*   The report will be generated as a single HTML page under the `reports/` folder.
*   Open the `reports/report.html` file in any browser to view the test outcomes.

### Option B: Advanced Interactive Allure QA Dashboard
To generate a comprehensive, recruiter-ready interactive QA dashboard, follow these steps:

#### Step 1: Run Pytest with Allure listener
Run the tests and tell Pytest to log outcomes to a raw data directory:
```bash
pytest --alluredir=reports/allure-results
```

#### Step 2: Install Allure Commandline (System Tool)
To compile the raw results into a web application dashboard, you must install the Allure command-line tool on your local machine:
*   **Windows (via Scoop):**
    ```bash
    scoop install allure
    ```
*   **macOS (via Homebrew):**
    ```bash
    brew install allure
    ```
*   **Linux (Debian/Ubuntu):**
    ```bash
    sudo apt-add-repository ppa:qameta/allure
    sudo apt-get update
    sudo apt-get install allure
    ```
*   *Alternatively, download the manual zip from the [Allure GitHub Releases Page](https://github.com/allure-framework/allure2/releases), extract it, and add the `bin/` folder to your system PATH.*

#### Step 3: Serve the Allure Dashboard
Launch a local web server to host and automatically open the interactive QA report dashboard in your browser:
```bash
allure serve reports/allure-results
```

#### Step 4: Build a Static Dashboard Report
To build a shareable folder containing the static HTML site (perfect for sharing zipped reports):
```bash
allure generate reports/allure-results -o reports/allure-report --clean
```
Open `reports/allure-report/index.html` to view the offline compilation.
