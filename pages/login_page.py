from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    """
    Page Object Model representing the Login Page of the Tichi application.
    Contains element locators and page actions.
    """

    # ==========================================
    # LOCATORS (Update these as per your actual HTML structure)
    # ==========================================
    EMAIL_INPUT = (By.ID, "email")                      # or (By.NAME, "email") / (By.CSS_SELECTOR, "input[type='email']")
    PASSWORD_INPUT = (By.ID, "password")                # or (By.NAME, "password") / (By.CSS_SELECTOR, "input[type='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']") # or (By.ID, "login-btn")
    
    # Inline or general error validation element
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message") # or (By.ID, "error-msg") / (By.CLASS_NAME, "validation-error")
    
    # Elements indicating successful login (located on Dashboard/Home Page)
    LOGOUT_BUTTON = (By.ID, "logout-btn")                # or (By.CSS_SELECTOR, "button.logout")
    DASHBOARD_HEADER = (By.CSS_SELECTOR, "h1.dashboard-title") # or any header on the post-login page

    # ==========================================
    # PAGE ACTIONS
    # ==========================================
    def enter_email(self, email):
        """Types the email in the email field."""
        self.type_text(self.EMAIL_INPUT, email)

    def enter_password(self, password):
        """Types the password in the password field."""
        self.type_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        """Clicks the login button."""
        self.click(self.LOGIN_BUTTON)

    def login(self, email, password):
        """Performs a full login attempt."""
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        """Retrieves validation or authentication error messages."""
        return self.get_text(self.ERROR_MESSAGE)

    def is_error_displayed(self):
        """Returns True if the login error message element is visible, otherwise False."""
        return self.is_displayed(self.ERROR_MESSAGE, timeout=3)

    def is_login_successful(self):
        """
        Verifies login success by checking the presence of a post-login element
        or verifying URL changes.
        """
        # Checks if either logout button is displayed or URL no longer contains '/login'
        return self.is_displayed(self.LOGOUT_BUTTON, timeout=5) or "login" not in self.get_current_url().lower()
