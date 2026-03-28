"""
Test scenarios for Text Input field based on QA Practice requirements.
"""
import pytest
from unittest.mock import Mock, MagicMock


class TextInputForm:
    """Mock form class to simulate text input behavior."""

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
        """Validate the input according to requirements."""
        self.errors = []

        # Required field check
        if not self.input_value.strip():
            self.errors.append("This field is required")
            return False

        # Length validation
        if len(self.input_value) < 2:
            self.errors.append("Text must be at least 2 characters long")
            return False

        if len(self.input_value) > 25:
            self.errors.append("Text must not exceed 25 characters")
            return False

        # Character validation - only English letters, numbers, underscores, hyphens
        import re
        if not re.match(r'^[a-zA-Z0-9_-]+$', self.input_value):
            self.errors.append("Text can only contain English letters, numbers, underscores, or hyphens")
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
def text_form():
    """Fixture to provide a fresh TextInputForm instance."""
    return TextInputForm()


class TestTextInputPositive:
    """Positive test cases for Text Input field."""

    def test_enter_valid_text_2_to_25_chars(self, text_form):
        """Enter valid text (2-25 characters, English letters, numbers, underscores, hyphens) and verify it's accepted."""
        valid_inputs = [
            "ab",  # minimum length
            "test123",  # alphanumeric
            "test_input",  # with underscore
            "test-input",  # with hyphen
            "TestInput123_Value",  # mixed case with underscore
            "abcdefghijklmnopqrstuvwxy",  # 25 characters
        ]

        for input_value in valid_inputs:
            text_form.set_input(input_value)
            assert text_form.validate(), f"Failed to validate input: {input_value}"
            assert text_form.errors == [], f"Unexpected errors for input {input_value}: {text_form.errors}"

    def test_enter_minimum_length_text(self, text_form):
        """Enter minimum length text (2 characters) and verify it's accepted."""
        text_form.set_input("ab")
        assert text_form.validate()
        assert text_form.errors == []

    def test_enter_maximum_length_text(self, text_form):
        """Enter maximum length text (25 characters) and verify it's accepted."""
        max_length_text = "abcdefghijklmnopqrstuvwxy"  # 25 chars
        text_form.set_input(max_length_text)
        assert text_form.validate()
        assert text_form.errors == []

    def test_submit_form_by_enter_key(self, text_form):
        """Submit form by pressing Enter key and verify form submission."""
        text_form.set_input("validtext")
        result = text_form.submit_with_enter()
        assert result is True
        assert text_form.submitted is True

    def test_verify_submitted_text_displayed(self, text_form):
        """Verify submitted text is displayed on the page after form submission."""
        input_text = "testinput"
        text_form.set_input(input_text)
        text_form.submit()
        assert text_form.displayed_text == input_text

    def test_enter_text_with_allowed_special_chars(self, text_form):
        """Enter text with allowed special characters (underscores, hyphens) and verify acceptance."""
        inputs_with_special = [
            "test_input",
            "test-input",
            "test_input-value",
            "a_b-c_d"
        ]

        for input_value in inputs_with_special:
            text_form.set_input(input_value)
            assert text_form.validate(), f"Failed for input: {input_value}"
            assert text_form.errors == []

    def test_enter_mixed_alphanumeric_text(self, text_form):
        """Enter mixed alphanumeric text and verify it's accepted."""
        mixed_inputs = [
            "abc123",
            "Test123",
            "a1b2c3",
            "123abc",
            "a1B2c3D4"
        ]

        for input_value in mixed_inputs:
            text_form.set_input(input_value)
            assert text_form.validate(), f"Failed for input: {input_value}"
            assert text_form.errors == []


class TestTextInputNegative:
    """Negative test cases for Text Input field."""

    def test_leave_field_empty_required_validation(self, text_form):
        """Leave field empty and verify required field validation error."""
        text_form.set_input("")
        assert not text_form.validate()
        assert "This field is required" in text_form.errors

    def test_enter_text_shorter_than_2_chars(self, text_form):
        """Enter text shorter than 2 characters and verify validation error."""
        text_form.set_input("a")
        assert not text_form.validate()
        assert "at least 2 characters" in text_form.errors[0]

    def test_enter_text_longer_than_25_chars(self, text_form):
        """Enter text longer than 25 characters and verify it's rejected."""
        long_text = "abcdefghijklmnopqrstuvwxyz123"  # 29 chars
        text_form.set_input(long_text)
        assert not text_form.validate()
        assert "must not exceed 25 characters" in text_form.errors[0]

    def test_enter_text_with_prohibited_chars(self, text_form):
        """Enter text with prohibited characters (special symbols, spaces) and verify validation error."""
        prohibited_inputs = [
            "test input",  # space
            "test@input",  # @
            "test.input",  # dot
            "test#input",  # #
            "test$input",  # $
            "test%input",  # %
            "test^input",  # ^
            "test&input",  # &
            "test*input",  # *
            "test(input)",  # parentheses
        ]

        for input_value in prohibited_inputs:
            text_form.set_input(input_value)
            assert not text_form.validate(), f"Should fail for input: {input_value}"
            assert "can only contain" in text_form.errors[0]

    def test_submit_empty_form_prevents_submission(self, text_form):
        """Try submitting empty form and verify validation prevents submission."""
        text_form.set_input("")
        result = text_form.submit()
        assert result is False
        assert text_form.submitted is False
        assert "This field is required" in text_form.errors