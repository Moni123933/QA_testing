import os

class TestConfig:
    # Target Application URL
    BASE_URL = "https://tichi-app-webapp-stage.web.app"
    
    # Explicit wait timeout in seconds
    DEFAULT_TIMEOUT = 10
    
    # Valid Test Credentials (User should replace these with their own created credentials)
    VALID_EMAIL = os.getenv("TICHI_VALID_EMAIL", "valid_user@example.com")
    VALID_PASSWORD = os.getenv("TICHI_VALID_PASSWORD", "ValidPassword123!")
    
    # Invalid Test Credentials
    INVALID_EMAIL = "invalid_user@example.com"
    INVALID_PASSWORD = "WrongPassword123!"
    MALFORMED_EMAIL = "testuser"
