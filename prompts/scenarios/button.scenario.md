# Simple Button - Test Scenarios

Description: A basic clickable button.

## Requirements
- Button must be clickable by mouse and keyboard.
- Disabled button must not fire action.
- Visual states (normal/hover/active/disabled) must be distinguishable.

## Positive tests
- Click the button and verify the expected action occurs.
- Trigger the button via keyboard (Enter/Space) and verify action.
- Verify button state changes (pressed/active) while clicking.
- Verify button is focusable and receives focus outline.
- Verify button remains clickable after multiple rapid clicks.

## Negative tests
- Verify disabled button does not trigger the action.
- Verify clicking when network is unavailable shows appropriate message.
- Verify malformed requests are handled if the button triggers network calls.
- Verify button does not submit form unexpectedly when not intended.

## Suggested missing tests
- Verify button tooltip text is displayed and matches design.
- Verify button style and color are correct for each state (normal/hover/active/disabled).
- Verify button is not reachable via keyboard when disabled.
