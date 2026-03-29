"""
Test scenarios for Password Field based on QA Practice requirements.
"""
import pytest
import re


class PasswordFieldForm:
    """Mock form class to simulate password input behavior."""

    def __init__(self):
        self.input_value = ""
        self.submitted = False
        self.displayed_text = ""
        self.errors = []

    def set_input(self, value):
        """Set the input field value."""
        self.input_value = value
        self.errors = []

    def validate(self):
        """Validate the password according to requirements."""
        self.errors = []

        # Required field check
        if not self.input_value.strip():
            self.errors.append("Please fill out this field")
            return False

        # Minimum 8 characters
        if len(self.input_value) < 8:
            # self.errors.append("Password must be at least 8 characters long")
            self.errors.append("Low password complexity")
            return False

        # At least one uppercase English letter
        if not re.search(r'[A-Z]', self.input_value):
            # self.errors.append("Password must contain at least one uppercase letter")
            self.errors.append("Low password complexity")
            return False

        # At least one lowercase English letter
        if not re.search(r'[a-z]', self.input_value):
            # self.errors.append("Password must contain at least one lowercase letter")
            self.errors.append("Low password complexity")
            return False

        # At least one digit
        if not re.search(r'[0-9]', self.input_value):
            # self.errors.append("Password must contain at least one digit")
            self.errors.append("Low password complexity")
            return False

        # At least one special character
        if not re.search(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>\/?]', self.input_value):
            # self.errors.append("Password must contain at least one special character")
            self.errors.append("Low password complexity")
            return False

        return True

    def submit(self):
        """Submit the form."""
        if self.validate():
            self.submitted = True
            self.displayed_text = self.input_value
            return True
        return False

    def submit_with_enter(self):
        """Submit form by pressing Enter key."""
        return self.submit()


@pytest.fixture
def password_form():
    """Fixture to provide a fresh PasswordFieldForm instance."""
    return PasswordFieldForm()


class TestPasswordFieldPositive:
    """Positive test cases for Password Field."""

    def test_enter_password_minimum_8_chars_with_all_requirements(self, password_form):
        """Enter password with minimum 8 characters including uppercase, lowercase, digit, and special character and verify acceptance."""
        valid_passwords = [
            "Passw0rd!",
            "Test123!",
            "Secure1@",
            "MyPass9#",
            "Valid$123"
        ]

        for password in valid_passwords:
            password_form.set_input(password)
            assert password_form.validate(), f"Failed to validate password: {password}"
            assert password_form.errors == [], f"Unexpected errors for password {password}: {password_form.errors}"

    def test_enter_password_longer_than_8_chars_meeting_requirements(self, password_form):
        """Enter password longer than 8 characters meeting all requirements and verify acceptance."""
        long_valid_passwords = [
            "VerySecurePassword123!",
            "MySuperStrongPassword9@",
            "ComplexPasswordWithManyChars456#",
            "AnotherLongPasswordForTesting789$"
        ]

        for password in long_valid_passwords:
            password_form.set_input(password)
            assert password_form.validate(), f"Failed for long password: {password}"
            assert password_form.errors == []

    def test_submit_form_by_enter_key(self, password_form):
        """Submit form by pressing Enter key and verify form submission."""
        password_form.set_input("ValidPass1!")
        result = password_form.submit_with_enter()
        assert result is True
        assert password_form.submitted is True

    def test_verify_submitted_password_displayed(self, password_form):
        """Verify submitted password is displayed on the page after form submission."""
        input_password = "TestPass123!"
        password_form.set_input(input_password)
        password_form.submit()
        assert password_form.displayed_text == input_password

    def test_enter_password_with_various_special_characters(self, password_form):
        """Enter password with various special characters and verify acceptance."""
        passwords_with_special = [
            "Password1!",
            "Test123@",
            "Secure9#",
            "c",
            "Strong%789",
            "Power^123",
            "Force&789",
            "Might*456",
            "Super(123)",
            "Ultra_789",
            "Mega+456",
            "Hyper-123",
            "Ultra=789",
            "Max[456]",
            "Top{123}",
            "Best;789",
            "Prime:456",
            "Elite'123",
            "Pro\"789",
            "Star\\456",
            "Nova|123",
            "Beam,789",
            "Ray.456",
            "Light<123",
            "Bright>789",
            "Glow/456",
            "Shine?123"
        ]

        for password in passwords_with_special:
            password_form.set_input(password)
            assert password_form.validate(), f"Failed for password with special char: {password}"
            assert password_form.errors == []

    def test_enter_password_with_numbers_and_letters_different_positions(self, password_form):
        """Enter password with numbers and letters in different positions and verify acceptance."""
        varied_position_passwords = [
            "1Password!",
            "P2assword!",
            "Pa3sword!",
            "Pass4ord!",
            "Passw5rd!",
            "Passwo6d!",
            "Passwor7!",
            "Password8!",
            "Strong1!",
            "!Password1",
            "@Password2",
            "#Password3",
            "$Password4",
            "%Password5",
            "^Password6",
            "&Password7",
            "*Password8"
        ]

        for password in varied_position_passwords:
            password_form.set_input(password)
            assert password_form.validate(), f"Failed for varied position password: {password}"
            assert password_form.errors == []


class TestPasswordFieldNegative:
    """Negative test cases for Password Field."""

    def test_enter_password_shorter_than_8_chars(self, password_form):
        """Enter password shorter than 8 characters and verify validation error."""
        short_passwords = [
            "Pass1!",
            "Test!",
            "Ab1!",
            "Short"
        ]

        for password in short_passwords:
            password_form.set_input(password)
            assert not password_form.validate(), f"Should fail for short password: {password}"
            assert "Low password complexity" in str(password_form.errors)

    def test_enter_password_without_uppercase_letter(self, password_form):
        """Enter password without uppercase letter and verify validation error."""
        no_uppercase_passwords = [
            "password1!",
            "test123!",
            "lowercase9@"
        ]

        for password in no_uppercase_passwords:
            password_form.set_input(password)
            assert not password_form.validate(), f"Should fail for no uppercase: {password}"
            assert "Low password complexity" in str(password_form.errors)

    def test_enter_password_without_lowercase_letter(self, password_form):
        """Enter password without lowercase letter and verify validation error."""
        no_lowercase_passwords = [
            "PASSWORD1!",
            "TEST123!",
            "UPPERCASE9@"
        ]

        for password in no_lowercase_passwords:
            password_form.set_input(password)
            assert not password_form.validate(), f"Should fail for no lowercase: {password}"
            assert "Low password complexity" in str(password_form.errors)

    def test_enter_password_without_digit(self, password_form):
        """Enter password without digit and verify validation error."""
        no_digit_passwords = [
            "Password!",
            "TestPass!",
            "NoNumbers@"
        ]

        for password in no_digit_passwords:
            password_form.set_input(password)
            assert not password_form.validate(), f"Should fail for no digit: {password}"
            assert "Low password complexity" in str(password_form.errors)

    def test_enter_password_without_special_character(self, password_form):
        """Enter password without special character and verify validation error."""
        no_special_passwords = [
            "Password1",
            "TestPass123",
            "NoSpecial9"
        ]

        for password in no_special_passwords:
            password_form.set_input(password)
            assert not password_form.validate(), f"Should fail for no special char: {password}"
            assert "Low password complexity" in str(password_form.errors)

    def test_submit_empty_form_prevents_submission(self, password_form):
        """Try submitting empty form and verify validation prevents submission."""
        password_form.set_input("")
        result = password_form.submit()
        assert result is False
        assert password_form.submitted is False
        assert "Please fill out this field" in password_form.errors