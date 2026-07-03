import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config.config import TestConfig

@pytest.fixture(scope="function")
def driver():
    """
    Fixture to initialize Chrome WebDriver before each test function.
    Navigates automatically to the base URL and handles cleanup (quitting browser) post-execution.
    """
    # Configure Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # To run in headless mode (e.g. in CI/CD pipeline), uncomment the line below:
    # options.add_argument("--headless")

    # Initialize Chrome WebDriver using webdriver-manager to handle binary installation
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    # Navigate to target page
    driver.get(TestConfig.BASE_URL)
    
    # Pass control to the test function
    yield driver
    
    # Teardown: Ensure browser sessions are closed
    driver.quit()
