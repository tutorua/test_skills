"""
Test scenarios for Button elements based on QA Practice requirements.
"""
import pytest
from unittest.mock import Mock, MagicMock


class SimpleButton:
    """Mock class to simulate Simple Button behavior."""

    def __init__(self):
        self.label = "Click"
        self.enabled = True
        self.visible = True
        self.click_count = 0
        self.confirmation_message = ""

    def click(self):
        """Click the button."""
        if self.enabled and self.visible:
            self.click_count += 1
            self.confirmation_message = f"Button clicked {self.click_count} time(s)"
            return True
        return False

    def get_label(self):
        """Get button label."""
        return self.label

    def is_enabled(self):
        """Check if button is enabled."""
        return self.enabled

    def is_visible(self):
        """Check if button is visible."""
        return self.visible

    def get_confirmation_message(self):
        """Get the confirmation message."""
        return self.confirmation_message


class StyledLinkButton:
    """Mock class to simulate Looks Like a Button (link styled as button)."""

    def __init__(self):
        self.label = "Click"
        self.appears_as_button = True
        self.click_count = 0
        self.confirmation_message = ""
        self.url = "#"  # No navigation

    def click(self):
        """Click the styled link."""
        self.click_count += 1
        self.confirmation_message = f"Styled link clicked {self.click_count} time(s)"
        return True

    def get_label(self):
        """Get link text."""
        return self.label

    def appears_as_button(self):
        """Check if styled as button."""
        return self.appears_as_button

    def get_confirmation_message(self):
        """Get the confirmation message."""
        return self.confirmation_message

    def get_url(self):
        """Get the link URL."""
        return self.url


class DisabledButton:
    """Mock class to simulate Disabled Button behavior."""

    def __init__(self):
        self.label = "Submit"
        self.enabled = False
        self.dropdown_value = "Disabled"
        self.click_count = 0
        self.confirmation_message = ""

    def set_dropdown_value(self, value):
        """Set dropdown value and update button state."""
        self.dropdown_value = value
        if value == "Enabled":
            self.enabled = True
        elif value == "Disabled":
            self.enabled = False

    def click(self):
        """Click the button."""
        if self.enabled:
            self.click_count += 1
            self.confirmation_message = f"Button clicked {self.click_count} time(s)"
            return True
        return False

    def get_label(self):
        """Get button label."""
        return self.label

    def is_enabled(self):
        """Check if button is enabled."""
        return self.enabled

    def get_dropdown_value(self):
        """Get current dropdown value."""
        return self.dropdown_value

    def get_confirmation_message(self):
        """Get the confirmation message."""
        return self.confirmation_message


@pytest.fixture
def simple_button():
    """Fixture to provide a fresh SimpleButton instance."""
    return SimpleButton()


@pytest.fixture
def styled_link_button():
    """Fixture to provide a fresh StyledLinkButton instance."""
    return StyledLinkButton()


@pytest.fixture
def disabled_button():
    """Fixture to provide a fresh DisabledButton instance."""
    return DisabledButton()


class TestSimpleButtonPositive:
    """Positive test cases for Simple Button."""

    def test_click_button_once(self, simple_button):
        """Click the "Click" button."""
        result = simple_button.click()
        assert result is True
        assert simple_button.get_confirmation_message() == "Button clicked 1 time(s)"

    def test_button_label_verification(self, simple_button):
        """Verify button text is "Click"."""
        assert simple_button.get_label() == "Click"

    def test_button_is_enabled(self, simple_button):
        """Button should be clickable."""
        assert simple_button.is_enabled() is True

    def test_click_multiple_times(self, simple_button):
        """Click button repeatedly."""
        simple_button.click()
        simple_button.click()
        simple_button.click()
        assert simple_button.get_confirmation_message() == "Button clicked 3 time(s)"

    def test_button_visibility(self, simple_button):
        """Button should be visible on page load."""
        assert simple_button.is_visible() is True


class TestSimpleButtonNegative:
    """Negative test cases for Simple Button."""

    def test_double_click_handling(self, simple_button):
        """Double-click the button."""
        # Simulate double-click by clicking twice quickly
        simple_button.click()
        simple_button.click()
        # Should handle properly without adverse effects
        assert simple_button.click_count == 2

    def test_click_with_keyboard(self, simple_button):
        """Navigate to button and press Enter."""
        # Simulate keyboard activation
        result = simple_button.click()  # Mock keyboard press as click
        assert result is True
        assert simple_button.get_confirmation_message() == "Button clicked 1 time(s)"

    def test_rapid_successive_clicks(self, simple_button):
        """Click button very quickly multiple times."""
        for _ in range(10):
            simple_button.click()
        assert simple_button.click_count == 10
        assert simple_button.get_confirmation_message() == "Button clicked 10 time(s)"


class TestStyledLinkButtonPositive:
    """Positive test cases for Looks Like a Button (Link Style)."""

    def test_click_styled_link(self, styled_link_button):
        """Click the link styled as button."""
        result = styled_link_button.click()
        assert result is True
        assert styled_link_button.get_confirmation_message() == "Styled link clicked 1 time(s)"

    def test_visual_appearance(self, styled_link_button):
        """Link appears as button (not standard link appearance)."""
        assert styled_link_button.appears_as_button is True

    def test_label_verification(self, styled_link_button):
        """Verify link text is "Click"."""
        assert styled_link_button.get_label() == "Click"

    def test_multiple_clicks(self, styled_link_button):
        """Click styled link multiple times."""
        styled_link_button.click()
        styled_link_button.click()
        assert styled_link_button.get_confirmation_message() == "Styled link clicked 2 time(s)"


class TestStyledLinkButtonNegative:
    """Negative test cases for Looks Like a Button (Link Style)."""

    def test_standard_link_behavior(self, styled_link_button):
        """Verify it doesn't behave as standard link."""
        styled_link_button.click()
        # Should not navigate (URL is "#")
        assert styled_link_button.get_url() == "#"
        assert styled_link_button.get_confirmation_message() != ""  # But still shows message

    def test_text_selection(self, styled_link_button):
        """Try to select link text."""
        # In mock, assume text is selectable
        # Should not cause navigation
        assert styled_link_button.get_label() == "Click"

    def test_right_click_behavior(self, styled_link_button):
        """Right-click on styled link."""
        # In mock, assume right-click shows context menu
        # Should not affect functionality
        assert styled_link_button.label == "Click"


class TestDisabledButtonPositive:
    """Positive test cases for Disabled Button."""

    def test_button_disabled_by_default(self, disabled_button):
        """Load page and observe button state."""
        assert disabled_button.is_enabled() is False

    def test_enable_via_dropdown(self, disabled_button):
        """Select "Enabled" from dropdown."""
        disabled_button.set_dropdown_value("Enabled")
        assert disabled_button.is_enabled() is True

    def test_disable_via_dropdown(self, disabled_button):
        """Select "Disabled" from dropdown."""
        disabled_button.set_dropdown_value("Enabled")  # First enable
        disabled_button.set_dropdown_value("Disabled")  # Then disable
        assert disabled_button.is_enabled() is False

    def test_toggle_multiple_times(self, disabled_button):
        """Switch between Enabled/Disabled options."""
        disabled_button.set_dropdown_value("Enabled")
        assert disabled_button.is_enabled() is True
        disabled_button.set_dropdown_value("Disabled")
        assert disabled_button.is_enabled() is False
        disabled_button.set_dropdown_value("Enabled")
        assert disabled_button.is_enabled() is True

    def test_immediate_state_change(self, disabled_button):
        """Change dropdown selection."""
        disabled_button.set_dropdown_value("Enabled")
        assert disabled_button.is_enabled() is True  # Should update instantly

    def test_click_enabled_button(self, disabled_button):
        """Enable button and click it."""
        disabled_button.set_dropdown_value("Enabled")
        result = disabled_button.click()
        assert result is True
        assert disabled_button.get_confirmation_message() == "Button clicked 1 time(s)"

    def test_default_dropdown_value(self, disabled_button):
        """Load page and check dropdown."""
        assert disabled_button.get_dropdown_value() == "Disabled"


class TestDisabledButtonNegative:
    """Negative test cases for Disabled Button."""

    def test_click_disabled_button(self, disabled_button):
        """Try to click button while disabled."""
        result = disabled_button.click()
        assert result is False
        assert disabled_button.get_confirmation_message() == ""

    def test_bypassing_disabled_state(self, disabled_button):
        """Try to click before enabling."""
        result = disabled_button.click()
        assert result is False

    def test_keyboard_activation_of_disabled_button(self, disabled_button):
        """Tab to button and press Enter while disabled."""
        result = disabled_button.click()  # Mock keyboard press
        assert result is False

    def test_double_toggle(self, disabled_button):
        """Rapidly switch dropdown between states."""
        disabled_button.set_dropdown_value("Enabled")
        disabled_button.set_dropdown_value("Disabled")
        disabled_button.set_dropdown_value("Enabled")
        assert disabled_button.is_enabled() is True  # Final state
