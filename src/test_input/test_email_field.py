"""
Test scenarios for Email Field based on QA Practice requirements.
"""
import pytest
import re


class EmailFieldForm:
    """Mock form class to simulate email input behavior."""

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
        """Validate the email according to requirements."""
        self.errors = []

        # Required field check
        if not self.input_value.strip():
            self.errors.append("Please fill out this field")
            return False

        # Basic email format validation
        # Allow localhost domain as specified
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$|^[a-zA-Z0-9._%+-]+@localhost$'
        if not re.match(email_pattern, self.input_value):
            # self.errors.append("Invalid email format")
            self.errors.append("Enter a valid email address.")
            
            return False

        # Additional validation for localhost
        if '@localhost' in self.input_value:
            return True

        # Check for consecutive dots in domain
        local_part, domain = self.input_value.split('@', 1)
        if '..' in domain:
            # self.errors.append("Invalid email format")
            self.errors.append("Enter a valid email address.")
            return False

        # Check for invalid domain endings
        if domain.startswith('.') or domain.endswith('.'):
            # self.errors.append("Invalid email format")
            self.errors.append("Enter a valid email address.")
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
def email_form():
    """Fixture to provide a fresh EmailFieldForm instance."""
    return EmailFieldForm()


class TestEmailFieldPositive:
    """Positive test cases for Email Field."""

    def test_enter_valid_email_addresses(self, email_form):
        """Enter valid email addresses and verify acceptance."""
        valid_emails = [
            "user@example.com",
            "test.email+tag@domain.org",
            "simple@test.com",
            "user.name@company.net",
            "test_123@email-provider.co.uk"
        ]

        for email in valid_emails:
            email_form.set_input(email)
            assert email_form.validate(), f"Failed to validate email: {email}"
            assert email_form.errors == [], f"Unexpected errors for email {email}: {email_form.errors}"

    def test_enter_email_with_localhost_domain(self, email_form):
        """Enter email with localhost domain and verify it's accepted."""
        localhost_emails = [
            "user@localhost",
            "test@localhost",
            "admin@localhost"
        ]

        for email in localhost_emails:
            email_form.set_input(email)
            assert email_form.validate(), f"Failed to validate localhost email: {email}"
            assert email_form.errors == []

    def test_submit_form_by_enter_key(self, email_form):
        """Submit form by pressing Enter key and verify form submission."""
        email_form.set_input("test@example.com")
        result = email_form.submit_with_enter()
        assert result is True
        assert email_form.submitted is True

    def test_verify_submitted_email_displayed(self, email_form):
        """Verify submitted email is displayed on the page after form submission."""
        input_email = "user@test.com"
        email_form.set_input(input_email)
        email_form.submit()
        assert email_form.displayed_text == input_email

    def test_enter_email_with_valid_special_chars_in_local_part(self, email_form):
        """Enter email with valid special characters in local part (dots, plus signs) and verify acceptance."""
        emails_with_special = [
            "user.name@example.com",
            "test+tag@domain.com",
            "user.name+tag@test.org",
            "test.email_123@example.com"
        ]

        for email in emails_with_special:
            email_form.set_input(email)
            assert email_form.validate(), f"Failed for email: {email}"
            assert email_form.errors == []

    def test_enter_email_with_subdomain(self, email_form):
        """Enter email with subdomain and verify acceptance."""
        subdomain_emails = [
            "user@sub.domain.com",
            "test@mail.example.org",
            "admin@service.company.net"
        ]

        for email in subdomain_emails:
            email_form.set_input(email)
            assert email_form.validate(), f"Failed for subdomain email: {email}"
            assert email_form.errors == []


class TestEmailFieldNegative:
    """Negative test cases for Email Field."""

    def test_enter_invalid_email_formats(self, email_form):
        """Enter invalid email formats and verify validation error."""
        invalid_emails = [
            "userexample.com",  # missing @
            "user@",  # missing domain
            "user@.com",  # domain starts with dot
            "user@domain.",  # domain ends with dot
            "@domain.com",  # missing local part
            "user name@domain.com",  # space in local part
            "user@domain..com",  # consecutive dots in domain
            "user#name@example.com"  # invalid character #
        ]

        for email in invalid_emails:
            email_form.set_input(email)
            assert not email_form.validate(), f"Should fail for invalid email: {email}"
            assert len(email_form.errors) > 0, f"No errors reported for invalid email: {email}"

    def test_enter_email_with_invalid_domain(self, email_form):
        """Enter email with invalid domain and verify rejection."""
        invalid_domain_emails = [
            "user@.com",
            "user@domain.",
            "user@domain..com",
            "user@.domain.com"
        ]

        for email in invalid_domain_emails:
            email_form.set_input(email)
            assert not email_form.validate(), f"Should fail for invalid domain email: {email}"
            # assert "Invalid domain format" in str(email_form.errors)
            assert "Enter a valid email address." in str(email_form.errors)
            

    def test_enter_email_with_consecutive_dots_in_domain(self, email_form):
        """Enter email with consecutive dots in domain and verify validation error."""
        email_form.set_input("user@domain..com")
        assert not email_form.validate()
        # assert "Invalid domain format" in str(email_form.errors)
        assert "Enter a valid email address." in str(email_form.errors)

    def test_enter_email_without_local_part(self, email_form):
        """Enter email without local part and verify rejection."""
        email_form.set_input("@domain.com")
        assert not email_form.validate()
        assert len(email_form.errors) > 0

    def test_submit_empty_form_prevents_submission(self, email_form):
        """Try submitting empty form and verify validation prevents submission."""
        email_form.set_input("")
        result = email_form.submit()
        assert result is False
        assert email_form.submitted is False
        assert "Please fill out this field" in email_form.errors