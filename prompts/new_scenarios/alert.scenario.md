# Alert/Dialog Testing Scenarios

## Element Overview
The Alert element has three variations: Alert Box, Confirmation Box, and Prompt Box.

## Requirements Summary

### Alert Box
- Page has a "Click" button
- Clicking button triggers alert dialog
- Alert displays: "I am an alert!"
- Alert has OK button
- Clicking OK closes alert

### Confirmation Box
- Page has a "Click" button  
- Clicking button triggers confirmation dialog
- Alert displays: "I am an alert!"
- Alert has OK and Cancel buttons
- Clicking OK or Cancel closes dialog
- User's choice (OK/Cancel) displayed on page

### Prompt Box
- Page has a "Click" button
- Clicking button triggers prompt dialog
- Alert displays: "I am an alert!"
- Alert has OK, Cancel buttons and text input field
- User can enter text in prompt
- Clicking OK or Cancel closes dialog
- User's input displayed on page

---

## Test Cases

### Alert Box - Positive Tests
1. **Click button to show alert**: Click "Click" button
   - Expected: Alert dialog appears with message "I am an alert!"

2. **Verify alert message**: Read alert message
   - Expected: Message displays exactly: "I am an alert!"

3. **Alert has OK button**: Check alert buttons
   - Expected: OK button present and visible

4. **Click OK to close**: Click OK button in alert
   - Expected: Alert closes and page returns to normal state

5. **Multiple alerts**: Click button again after closing first alert
   - Expected: New alert appears normally

6. **Verify page title/context**: Check page title
   - Expected: Alert is from correct page/context

### Alert Box - Negative Tests
1. **Alert appears on first click**: Click should trigger alert immediately
   - Expected: No additional action needed to show alert

2. **Extra buttons**: Check alert doesn't have unexpected buttons
   - Expected: Only OK button (no Cancel, No, Yes buttons)

3. **Change alert message**: Try to interact with alert text
   - Expected: Message cannot be edited, display only

4. **Alert background**: Check modal behavior
   - Expected: Page behind alert should be inaccessible until alert closed

### Alert Box - Omitted Tests (Suggested)
1. Browser alert styling and appearance
2. Keyboard shortcut (Enter) to confirm
3. Alert position on screen
4. Multiple alerts in rapid succession
5. Alert with very long message
6. Browser's native vs custom alert behavior
7. Alert timing/delay
8. Screen reader announcement

---

### Confirmation Box - Positive Tests
1. **Click button to show confirmation**: Click "Click" button
   - Expected: Confirmation dialog appears with message "I am an alert!"

2. **Dialog has both buttons**: Check confirmation dialog
   - Expected: Both OK and Cancel buttons present

3. **Click OK button**: Click OK in confirmation dialog
   - Expected: Dialog closes, choice displayed on page

4. **Click Cancel button**: Click Cancel in confirmation dialog
   - Expected: Dialog closes, choice displayed on page

5. **Verify OK choice displayed**: Click OK and check result
   - Expected: "OK" or user's choice displayed on page

6. **Verify Cancel choice displayed**: Click Cancel and check result
   - Expected: "Cancel" or user's choice displayed on page

7. **Multiple confirmations**: Show two confirmations with different choices
   - Expected: Each shows correct choice on page

8. **Message verification**: Verify confirmation message
   - Expected: Displays "I am an alert!"

### Confirmation Box - Negative Tests
1. **Verify modal behavior**: Try to click page behind dialog
   - Expected: Page elements not clickable until dialog resolved

2. **Dialog close without choice**: Try to close by X button (if present)
   - Expected: Behavior defined (counts as Cancel or disabled)

3. **Two confirmations in sequence**: Show first, make choice, show second
   - Expected: Second confirmation doesn't combine with first result

4. **Extra buttons check**: Verify only OK and Cancel exist
   - Expected: No Yes/No or other button variations

### Confirmation Box - Omitted Tests (Suggested)
1. Keyboard navigation (Tab between buttons)
2. Enter/Escape key handling
3. Button order (OK first or Cancel first)
4. Result display format/location
5. Multiple browsers' default button focus
6. Esc key to cancel
7. Result persistence after page operations
8. Accessibility (ARIA for choice)
9. Time-based auto-dismissal
10. Result clearing on page refresh

---

### Prompt Box - Positive Tests
1. **Click button to show prompt**: Click "Click" button
   - Expected: Prompt dialog appears with message "I am an alert!"

2. **Prompt has input field**: Check for text input in dialog
   - Expected: Text input field visible and focusable

3. **Prompt has both buttons**: Check buttons present
   - Expected: OK and Cancel buttons in dialog

4. **Enter text and OK**: Type "TestInput" in prompt and click OK
   - Expected: "TestInput" displayed on page

5. **Empty and click OK**: Leave prompt empty and click OK
   - Expected: Empty value handled (displayed or treated as empty)

6. **Enter special characters**: Type "Test@123!#" in prompt and click OK
   - Expected: Special characters preserved in display

7. **Multi-line text in prompt**: Enter text with line break (if supported)
   - Expected: Text with line breaks displayed

8. **Click Cancel with input**: Type text but click Cancel
   - Expected: Input discarded, "Cancel" displayed or empty result

9. **Very long input**: Paste long text in prompt input field
   - Expected: Handles long input gracefully

10. **Input field focus**: Check input field is focused on prompt load
    - Expected: Can type immediately without clicking field

### Prompt Box - Negative Tests
1. **Input field focus**: Field should be pre-focused
   - Expected: Typing immediately enters text (no click needed)

2. **Cancel discards input**: Enter text and click Cancel
   - Expected: Input not saved, not shown on page

3. **No default value edited**: Check if prompt has default text
   - Expected: Any pre-filled text handled correctly

4. **Modal blocking**: Try to click page during prompt
   - Expected: Page inaccessible until prompt resolved

5. **Input field is editable**: Type in the field
   - Expected: Text can be entered and edited

### Prompt Box - Omitted Tests (Suggested)
1. Input field character limit
2. Pre-filled default value in prompt
3. Input validation (email, numbers only, etc.)
4. Placeholder text in input field
5. Clear/reset input button
6. Copy-paste in prompt input
7. Keyboard shortcuts (Ctrl+A to select all)
8. Tab/Shift+Tab navigation in prompt
9. Result display format/location
10. Multiple prompts with different inputs
11. Esc key to cancel
12. Password masking if applicable
13. Input history/autocomplete
