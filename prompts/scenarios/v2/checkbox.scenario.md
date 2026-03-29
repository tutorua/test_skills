# Single Checkbox - Test Scenarios

Description: Single checkbox control scenarios.

## Requirements
- Checkbox must toggle checked state on click and Space key.
- Disabled checkbox must not toggle.
- Checked state must be submitted in form when required.

## Positive tests
- Check the checkbox and verify its checked state.
- Uncheck the checkbox and verify state changes accordingly.
- Toggle checkbox via keyboard (Space) and verify state.
- Verify checkbox value is submitted with the form when checked.
- Verify checkbox retains state after page refresh if designed to do so.

## Negative tests
- Verify clicking disabled checkbox does not change state.
- Verify unexpected values are not submitted when unchecked.
- Verify UI remains consistent when checkbox state changes rapidly.
- Verify accessibility: screen reader announces state correctly.

## Suggested missing tests
- Verify indeterminate state behavior (if supported) and overall reporting.
- Verify visual focus indicator is visible when checkbox is tab-focused.
- Verify error message appears for invalid combinations with other controls in the same form.
