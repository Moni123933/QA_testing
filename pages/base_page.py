import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from config.config import TestConfig

# Set up logging configuration
logger = logging.getLogger(__name__)

class BasePage:
    """
    BasePage serves as a parent class for all Page Objects.
    It encapsulates common Selenium WebDriver operations and provides 
    explicit wait wrappers to handle asynchronous loading and race conditions.
    """

    def __init__(self, driver):
        self.driver = driver
        self.timeout = TestConfig.DEFAULT_TIMEOUT

    def wait_for_presence(self, locator, timeout=None):
        """Waits for an element to be present in the DOM."""
        timeout = timeout or self.timeout
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            logger.error(f"Element with locator {locator} was not present within {timeout} seconds.")
            raise

    def wait_for_visibility(self, locator, timeout=None):
        """Waits for an element to be visible on the page."""
        timeout = timeout or self.timeout
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            logger.error(f"Element with locator {locator} was not visible within {timeout} seconds.")
            raise

    def wait_for_element_to_be_clickable(self, locator, timeout=None):
        """Waits for an element to be clickable."""
        timeout = timeout or self.timeout
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            logger.error(f"Element with locator {locator} was not clickable within {timeout} seconds.")
            raise

    def find_element(self, locator, timeout=None):
        """Finds a single element, waiting for its visibility first."""
        return self.wait_for_visibility(locator, timeout)

    def find_elements(self, locator, timeout=None):
        """Finds multiple elements, waiting for their presence first."""
        timeout = timeout or self.timeout
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
            return self.driver.find_elements(*locator)
        except TimeoutException:
            logger.warning(f"Elements with locator {locator} were not present within {timeout} seconds.")
            return []

    def click(self, locator, timeout=None):
        """Clicks an element after ensuring it is clickable."""
        logger.info(f"Clicking element with locator: {locator}")
        element = self.wait_for_element_to_be_clickable(locator, timeout)
        element.click()

    def type_text(self, locator, text, timeout=None):
        """Clears an input field and types text into it after ensuring visibility."""
        logger.info(f"Typing '{text}' into element with locator: {locator}")
        element = self.wait_for_visibility(locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout=None):
        """Gets the text content of an element after ensuring visibility."""
        element = self.wait_for_visibility(locator, timeout)
        text = element.text
        logger.debug(f"Retrieved text '{text}' from locator: {locator}")
        return text

    def is_displayed(self, locator, timeout=None):
        """Checks if an element is visible on the page without raising a TimeoutException."""
        timeout = timeout or self.timeout
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except (TimeoutException, NoSuchElementException):
            logger.warning(f"Element with locator {locator} is not displayed.")
            return False

    def get_title(self):
        """Returns the title of the current page."""
        title = self.driver.title
        logger.debug(f"Current page title: {title}")
        return title

    def get_current_url(self):
        """Returns the current URL of the browser."""
        url = self.driver.current_url
        logger.debug(f"Current URL: {url}")
        return url
