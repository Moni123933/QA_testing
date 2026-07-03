import pytest
from pages.login_page import LoginPage
from config.config import TestConfig

class TestLogin:
    """
    Test suite containing automated Login scenarios using the Page Object Model.
    Covers positive verification, invalid password rejection, and invalid email formatting.
    """

    def test_successful_login(self, driver):
        """
        Verify that a user is successfully authenticated and redirected
        when entering valid credentials.
        """
        login_page = LoginPage(driver)
        
        # Act
        login_page.login(TestConfig.VALID_EMAIL, TestConfig.VALID_PASSWORD)
        
        # Assert
        assert login_page.is_login_successful(), "Login failed with valid credentials. Expected redirection or dashboard display."

    def test_failed_login_invalid_password(self, driver):
        """
        Verify that entering an incorrect password for a registered email
        fails authentication and presents an error message.
        """
        login_page = LoginPage(driver)
        
        # Act
        login_page.login(TestConfig.VALID_EMAIL, TestConfig.INVALID_PASSWORD)
        
        # Assert
        assert not login_page.is_login_successful(), "User logged in with an invalid password, which is a critical security vulnerability."
        assert login_page.is_error_displayed(), "No validation error message was displayed for invalid password login."
        
        error_text = login_page.get_error_message()
        assert error_text != "", "Error message text is empty."

    def test_failed_login_invalid_email_format(self, driver):
        """
        Verify that inputting an invalid email format (e.g., 'testuser' without '@' or domain)
        is flagged by the frontend validator, preventing login attempts.
        """
        login_page = LoginPage(driver)
        
        # Act
        login_page.login(TestConfig.MALFORMED_EMAIL, TestConfig.VALID_PASSWORD)
        
        # Assert
        # The expected behavior should block login and show a validation warning
        assert not login_page.is_login_successful(), "System allowed login using an invalid email format (BUG-001)."
        assert login_page.is_error_displayed(), "No validation error message was shown for a malformed email format."
        
        error_text = login_page.get_error_message()
        # Common expected messages: "Please enter a valid email address", "Invalid email", etc.
        assert len(error_text) > 0, "Expected email format validation error to be displayed."
