# Single UI Elements Test Plan

This document consolidates all test scenarios for the 10 sub-items under the "Single UI Elements" category from the QA Practice site. Each section covers one UI element with its requirements, positive tests, negative tests, and suggested missing tests.

## Table of Contents

1. [Simple Button](#simple-button)
2. [Single Checkbox](#single-checkbox)
3. [Text Input](#text-input)
4. [Select Input](#select-input)
5. [Text Area](#text-area)
6. [Radio Button](#radio-button)
7. [Toggle Switch](#toggle-switch)
8. [Date Picker](#date-picker)
9. [Slider Control](#slider-control)
10. [File Upload](#file-upload)

---

## Simple Button

Description: A basic clickable button.

### Requirements
- Button must be clickable by mouse and keyboard.
- Disabled button must not fire action.
- Visual states (normal/hover/active/disabled) must be distinguishable.

### Positive tests
- Click the button and verify the expected action occurs.
- Trigger the button via keyboard (Enter/Space) and verify action.
- Verify button state changes (pressed/active) while clicking.
- Verify button is focusable and receives focus outline.
- Verify button remains clickable after multiple rapid clicks.

### Negative tests
- Verify disabled button does not trigger the action.
- Verify clicking when network is unavailable shows appropriate message.
- Verify malformed requests are handled if the button triggers network calls.
- Verify button does not submit form unexpectedly when not intended.

### Suggested missing tests
- Verify button tooltip text is displayed and matches design.
- Verify button style and color are correct for each state (normal/hover/active/disabled).
- Verify button is not reachable via keyboard when disabled.

---

## Single Checkbox

Description: Single checkbox control scenarios.

### Requirements
- Checkbox must toggle checked state on click and Space key.
- Disabled checkbox must not toggle.
- Checked state must be submitted in form when required.

### Positive tests
- Check the checkbox and verify its checked state.
- Uncheck the checkbox and verify state changes accordingly.
- Toggle checkbox via keyboard (Space) and verify state.
- Verify checkbox value is submitted with the form when checked.
- Verify checkbox retains state after page refresh if designed to do so.

### Negative tests
- Verify clicking disabled checkbox does not change state.
- Verify unexpected values are not submitted when unchecked.
- Verify UI remains consistent when checkbox state changes rapidly.
- Verify accessibility: screen reader announces state correctly.

### Suggested missing tests
- Verify indeterminate state behavior (if supported) and overall reporting.
- Verify visual focus indicator is visible when checkbox is tab-focused.
- Verify error message appears for invalid combinations with other controls in the same form.

---

## Text Input

Description: Simple text input field scenarios.

### Requirements
- Input should accept text up to maxlength and offer validation for required fields.
- Unsupported characters must be rejected for strict patterns.
- Paste and keyboard input should be consistent.

### Positive tests
- Enter valid short text and verify value is accepted.
- Enter long text within maxlength and verify it's accepted.
- Paste text and verify clipboard content is inserted.
- Clear the field and verify placeholder appears (if applicable).
- Submit form with input filled and verify submission succeeds.
- Enter allowed special characters and verify they are accepted.

### Negative tests
- Enter text longer than maxlength and verify it is truncated or rejected.
- Enter prohibited characters (if specified) and verify validation error.
- Leave input empty when required and verify validation error.
- Try SQL/JS injection strings and verify they are not executed or accepted.

### Suggested missing tests
- Verify autocomplete and suggestions (if enabled) behave correctly.
- Verify input retains value on back/forward browser navigation (if expected).
- Verify invalid formatted text shows correct error messages (for email/number/etc.).

---

## Select Input

Description: Single-select dropdown scenarios.

### Requirements
- Dropdown options should be selectable by click and keyboard.
- Disabled options should not be selectable.
- Required selection should trigger validation when missing.

### Positive tests
- Open dropdown and select an option; verify selected value.
- Select by keyboard (arrow keys + Enter) and verify selection.
- Verify default selected option (if any) is correct.
- Verify options render correctly and are readable.
- Submit form with selected option and verify correct value sent.

### Negative tests
- Verify selecting a disabled option is not possible.
- Verify empty selection when selection is required triggers validation.
- Verify unexpected option values are not accepted by the server.
- Verify dropdown closes without selection on outside click and state remains unchanged.

### Suggested missing tests
- Verify keyboard navigation wraps correctly when reaching first/last option.
- Verify the dropdown does not open on disabled control.
- Verify dependent fields update when option changes (if applicable).

---

## Text Area

Description: Multi-line text area scenarios.

### Requirements
- Text area must preserve line breaks and be editable with keyboard actions.
- Maxlength must enforce limits and provide validation states.
- Required text area must reject empty submissions.

### Positive tests
- Enter multiple lines of text and verify newline preservation.
- Paste large text and verify it is accepted up to maxlength.
- Use keyboard shortcuts (Ctrl+A, Ctrl+V) and verify behavior.
- Verify autosize (if present) adjusts height appropriately.
- Submit form with text area content and verify submission includes content.

### Negative tests
- Enter text exceeding maxlength and verify truncation or validation.
- Verify required validation when left empty if applicable.
- Verify special characters do not break layout or submit unexpectedly.
- Verify large inputs do not crash the client or server.

### Suggested missing tests
- Verify soft wrap works as expected and line breaks are preserved.
- Verify keyboard shortcuts for undo/redo are supported.
- Verify native mobile keyboard behavior is correct on touch devices.

---

## Radio Button

Description: Single-select radio button group scenarios.

### Requirements
- Only one option may be selected at a time.
- Radio grouping must include accessible labels.
- Keyboard navigation (Arrow keys / Tab) must move selection.

### Positive tests
- Select one radio option and verify exclusive selection.
- Change selection to another option and verify previous is deselected.
- Use keyboard arrows to navigate and select options.
- Verify required radio group triggers validation when nothing selected.
- Verify initial selected value is preserved after refresh (if required).

### Negative tests
- Verify already selected option cannot be unselected directly.
- Verify clicking disabled option does not change state.
- Verify invalid value is not submitted by the form.
- Verify group behaves correctly when options are dynamically added/ removed.

### Suggested missing tests
- Verify screen reader announces selected state and group name.
- Verify focus ring appears on selected/active option.
- Verify visually hidden required marker is still available to accessibility API.

---

## Toggle Switch

Description: Single on/off toggle switch scenarios.

### Requirements
- Toggle must be switchable via click and keyboard (Space/Enter).
- Disabled toggles must remain unchanged.
- State should be reflected in submit payload or model.

### Positive tests
- Toggle ON and verify associated functionality activates.
- Toggle OFF and verify functionality deactivates.
- Verify keyboard interaction works (Space/Enter to toggle).
- Verify visual state changes between enabled/disabled clearly.
- Verify persistent state when the UI indicates saved state.

### Negative tests
- Verify toggling is blocked when component is disabled.
- Verify invalid state values (e.g., undefined) are handled gracefully.
- Verify rapid toggles don't cause race conditions in state updates.
- Verify API rejects invalid toggle state in payload.

### Suggested missing tests
- Verify focus ring and aria-checked attribute correctness.
- Verify alternate text or label is read by screen readers.
- Verify toggle works on mobile touch interactions.

---

## Date Picker

Description: Calendar date-picker selection scenarios.

### Requirements
- Users must be able to pick a date from the calendar UI.
- Input must validate date format and restrict invalid dates.
- Required date field must enforce selection.

### Positive tests
- Select a valid date and verify the value is set.
- Navigate between months and select dates in adjacent months.
- Enter a valid date manually and verify it's accepted.
- Verify keyboard navigation works for date selection.
- Verify date field clears when using clear control (if provided).

### Negative tests
- Enter an invalid date and verify validation message displayed.
- Try selecting a disabled/unavailable date (past or out of range).
- Verify empty required date submission triggers validation.
- Verify malformed date strings are rejected.

### Suggested missing tests
- Verify localization (date format and week start day) behavior.
- Verify leap year date selection works correctly (Feb 29).
- Verify component handles daylight savings and timezone-related display properly.

---

## Slider Control

Description: Slider (range input) scenarios.

### Requirements
- Slider must move via drag and keyboard arrows.
- Value must snap to configured steps.
- Slider must expose aria attributes for accessibility.

### Positive tests
- Drag the handle to a new value and verify the result.
- Use keyboard arrows/Home/End to adjust value.
- Verify value is correctly updated in real time.
- Verify min/max boundaries are enforced.
- Verify form submission includes slider value.

### Negative tests
- Attempt to set value outside min/max and verify it's clamped.
- Verify disabled slider does not change value.
- Verify invalid step values are rejected.
- Verify slider state preserves after page refresh if expected.

### Suggested missing tests
- Verify tooltip displays current value while dragging.
- Verify slider can be controlled via scripting (if API provided).
- Verify visual track updates for range segments (if applicable).

---

## File Upload

Description: Single file upload control scenarios.

### Requirements
- Users must be able to select a file and upload it successfully.
- Allowed file types and max size must be enforced.
- Upload progress and success/failure messaging must be displayed.

### Positive tests
- Upload a valid file and verify success flow.
- Verify drag-and-drop upload works (if provided).
- Verify multiple file behavior is unsupported/disabled for single file mode.
- Verify canceling upload stops in-progress upload.
- Verify selected file details (name/size/type) appear correctly.

### Negative tests
- Attempt upload of disallowed file type and verify error.
- Attempt upload of a file larger than max size and verify error.
- Verify system handles network failure during upload gracefully.
- Verify uploading when required and empty triggers validation.

### Suggested missing tests
- Verify filename sanitization protections (special chars, path injection) in UI display.
- Verify resubmitting same file works as expected.
- Verify malware scan warning path (if part of requirements).