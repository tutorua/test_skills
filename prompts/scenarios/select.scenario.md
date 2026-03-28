# Select Input - Test Scenarios

Description: Single-select dropdown scenarios.

## Requirements
- Dropdown options should be selectable by click and keyboard.
- Disabled options should not be selectable.
- Required selection should trigger validation when missing.

## Positive tests
- Open dropdown and select an option; verify selected value.
- Select by keyboard (arrow keys + Enter) and verify selection.
- Verify default selected option (if any) is correct.
- Verify options render correctly and are readable.
- Submit form with selected option and verify correct value sent.

## Negative tests
- Verify selecting a disabled option is not possible.
- Verify empty selection when selection is required triggers validation.
- Verify unexpected option values are not accepted by the server.
- Verify dropdown closes without selection on outside click and state remains unchanged.

## Suggested missing tests
- Verify keyboard navigation wraps correctly when reaching first/last option.
- Verify the dropdown does not open on disabled control.
- Verify dependent fields update when option changes (if applicable).
