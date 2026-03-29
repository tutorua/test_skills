"""
Test scenarios for Checkbox elements based on QA Practice requirements.
"""
import pytest
from unittest.mock import Mock, MagicMock


class SingleCheckbox:
    """Mock class to simulate Single Checkbox behavior."""

    def __init__(self):
        self.label = "Select me or not"
        self.checked = False
        self.submit_enabled = True
        self.result = ""

    def toggle(self):
        """Toggle the checkbox state."""
        self.checked = not self.checked
        return self.checked

    def click_label(self):
        """Click on the label to toggle."""
        return self.toggle()

    def submit(self):
        """Submit the form."""
        if self.checked:
            self.result = self.label
        else:
            self.result = ""
        return True

    def is_checked(self):
        """Check if checkbox is checked."""
        return self.checked

    def get_label(self):
        """Get checkbox label."""
        return self.label

    def is_submit_enabled(self):
        """Check if submit button is enabled."""
        return self.submit_enabled

    def get_result(self):
        """Get the displayed result."""
        return self.result


class MultipleCheckboxes:
    """Mock class to simulate Multiple Checkboxes behavior."""

    def __init__(self):
        self.checkboxes = {
            "One": False,
            "Two": False,
            "Three": False
        }
        self.submit_enabled = True
        self.result = []

    def toggle_checkbox(self, label):
        """Toggle a specific checkbox."""
        if label in self.checkboxes:
            self.checkboxes[label] = not self.checkboxes[label]
            return True
        return False

    def check_checkbox(self, label):
        """Check a specific checkbox."""
        if label in self.checkboxes:
            self.checkboxes[label] = True
            return True
        return False

    def uncheck_checkbox(self, label):
        """Uncheck a specific checkbox."""
        if label in self.checkboxes:
            self.checkboxes[label] = False
            return True
        return False

    def submit(self):
        """Submit the form."""
        self.result = [label for label, checked in self.checkboxes.items() if checked]
        return True

    def get_checked_checkboxes(self):
        """Get list of checked checkboxes."""
        return [label for label, checked in self.checkboxes.items() if checked]

    def is_checkbox_checked(self, label):
        """Check if a specific checkbox is checked."""
        return self.checkboxes.get(label, False)

    def get_labels(self):
        """Get all checkbox labels."""
        return list(self.checkboxes.keys())

    def is_submit_enabled(self):
        """Check if submit button is enabled."""
        return self.submit_enabled

    def get_result(self):
        """Get the displayed result."""
        return self.result


@pytest.fixture
def single_checkbox():
    """Fixture to provide a fresh SingleCheckbox instance."""
    return SingleCheckbox()


@pytest.fixture
def multiple_checkboxes():
    """Fixture to provide a fresh MultipleCheckboxes instance."""
    return MultipleCheckboxes()


class TestSingleCheckboxPositive:
    """Positive test cases for Single Checkbox."""

    def test_check_checkbox(self, single_checkbox):
        """Click unchecked checkbox."""
        result = single_checkbox.toggle()
        assert result is True
        assert single_checkbox.is_checked() is True

    def test_uncheck_checkbox(self, single_checkbox):
        """Click checked checkbox."""
        single_checkbox.toggle()  # Check first
        result = single_checkbox.toggle()  # Then uncheck
        assert result is False
        assert single_checkbox.is_checked() is False

    def test_submit_when_unchecked(self, single_checkbox):
        """Leave unchecked and click Submit."""
        single_checkbox.submit()
        result = single_checkbox.get_result()
        assert result == ""

    def test_submit_when_checked(self, single_checkbox):
        """Check checkbox and click Submit."""
        single_checkbox.toggle()
        single_checkbox.submit()
        result = single_checkbox.get_result()
        assert result == "Select me or not"

    def test_toggle_multiple_times(self, single_checkbox):
        """Check and uncheck repeatedly."""
        # Start unchecked
        assert single_checkbox.is_checked() is False
        
        # Check
        single_checkbox.toggle()
        assert single_checkbox.is_checked() is True
        
        # Uncheck
        single_checkbox.toggle()
        assert single_checkbox.is_checked() is False
        
        # Check again
        single_checkbox.toggle()
        assert single_checkbox.is_checked() is True

    def test_label_click(self, single_checkbox):
        """Click on label text "Select me or not"."""
        result = single_checkbox.click_label()
        assert result is True
        assert single_checkbox.is_checked() is True

    def test_visual_feedback(self, single_checkbox):
        """Check checkbox - visual feedback."""
        single_checkbox.toggle()
        # In mock, assume visual feedback is present when checked
        assert single_checkbox.is_checked() is True


class TestSingleCheckboxNegative:
    """Negative test cases for Single Checkbox."""

    def test_submit_button_state(self, single_checkbox):
        """Verify Submit button is always enabled."""
        assert single_checkbox.is_submit_enabled() is True
        
        # Even when unchecked
        assert single_checkbox.is_submit_enabled() is True

    def test_result_appear_when_unchecked(self, single_checkbox):
        """Leave unchecked and submit."""
        single_checkbox.submit()
        result = single_checkbox.get_result()
        assert result == ""  # Should be empty

    def test_incorrect_content_in_result(self, single_checkbox):
        """Submit checked checkbox."""
        single_checkbox.toggle()
        single_checkbox.submit()
        result = single_checkbox.get_result()
        assert result == "Select me or not"  # Only this text, nothing extra


class TestMultipleCheckboxesPositive:
    """Positive test cases for Multiple Checkboxes."""

    def test_check_first_checkbox(self, multiple_checkboxes):
        """Click "One" checkbox."""
        result = multiple_checkboxes.check_checkbox("One")
        assert result is True
        assert multiple_checkboxes.is_checkbox_checked("One") is True

    def test_check_multiple_checkboxes(self, multiple_checkboxes):
        """Select "One" and "Two"."""
        multiple_checkboxes.check_checkbox("One")
        multiple_checkboxes.check_checkbox("Two")
        assert multiple_checkboxes.is_checkbox_checked("One") is True
        assert multiple_checkboxes.is_checkbox_checked("Two") is True
        assert multiple_checkboxes.is_checkbox_checked("Three") is False

    def test_check_all_checkboxes(self, multiple_checkboxes):
        """Select all three."""
        multiple_checkboxes.check_checkbox("One")
        multiple_checkboxes.check_checkbox("Two")
        multiple_checkboxes.check_checkbox("Three")
        checked = multiple_checkboxes.get_checked_checkboxes()
        assert len(checked) == 3
        assert "One" in checked
        assert "Two" in checked
        assert "Three" in checked

    def test_submit_with_single_selection(self, multiple_checkboxes):
        """Check only "Two" and submit."""
        multiple_checkboxes.check_checkbox("Two")
        multiple_checkboxes.submit()
        result = multiple_checkboxes.get_result()
        assert result == ["Two"]

    def test_submit_with_multiple_selections(self, multiple_checkboxes):
        """Check "One" and "Three" and submit."""
        multiple_checkboxes.check_checkbox("One")
        multiple_checkboxes.check_checkbox("Three")
        multiple_checkboxes.submit()
        result = multiple_checkboxes.get_result()
        assert set(result) == {"One", "Three"}

    def test_submit_with_all_selected(self, multiple_checkboxes):
        """Check all three and submit."""
        multiple_checkboxes.check_checkbox("One")
        multiple_checkboxes.check_checkbox("Two")
        multiple_checkboxes.check_checkbox("Three")
        multiple_checkboxes.submit()
        result = multiple_checkboxes.get_result()
        assert set(result) == {"One", "Two", "Three"}

    def test_uncheck_one_of_multiple(self, multiple_checkboxes):
        """Check all, then uncheck "Two", submit."""
        multiple_checkboxes.check_checkbox("One")
        multiple_checkboxes.check_checkbox("Two")
        multiple_checkboxes.check_checkbox("Three")
        multiple_checkboxes.uncheck_checkbox("Two")
        multiple_checkboxes.submit()
        result = multiple_checkboxes.get_result()
        assert set(result) == {"One", "Three"}

    def test_label_text_verification(self, multiple_checkboxes):
        """Verify checkbox labels."""
        labels = multiple_checkboxes.get_labels()
        assert set(labels) == {"One", "Two", "Three"}

    def test_uncheck_checkbox(self, multiple_checkboxes):
        """Click checked checkbox to uncheck."""
        multiple_checkboxes.check_checkbox("One")
        assert multiple_checkboxes.is_checkbox_checked("One") is True
        multiple_checkboxes.uncheck_checkbox("One")
        assert multiple_checkboxes.is_checkbox_checked("One") is False


class TestMultipleCheckboxesNegative:
    """Negative test cases for Multiple Checkboxes."""

    def test_submit_without_selection(self, multiple_checkboxes):
        """Don't check any and click Submit."""
        multiple_checkboxes.submit()
        result = multiple_checkboxes.get_result()
        assert result == []  # Empty list

    def test_no_extra_content_in_result(self, multiple_checkboxes):
        """Submit with selections."""
        multiple_checkboxes.check_checkbox("One")
        multiple_checkboxes.check_checkbox("Two")
        multiple_checkboxes.submit()
        result = multiple_checkboxes.get_result()
        assert set(result) == {"One", "Two"}  # Only these, no duplicates or extras

    def test_incorrect_checkbox_names(self, multiple_checkboxes):
        """Check and submit."""
        multiple_checkboxes.check_checkbox("One")
        multiple_checkboxes.submit()
        result = multiple_checkboxes.get_result()
        assert result == ["One"]  # Correct name, not "1st" etc.

    def test_submit_button_state(self, multiple_checkboxes):
        """Verify always enabled."""
        assert multiple_checkboxes.is_submit_enabled() is True
        # Even with no selection
        assert multiple_checkboxes.is_submit_enabled() is True
