# Radio Button - Test Scenarios

Description: Single-select radio button group scenarios.

## Requirements
- Only one option may be selected at a time.
- Radio grouping must include accessible labels.
- Keyboard navigation (Arrow keys / Tab) must move selection.

## Positive tests
- Select one radio option and verify exclusive selection.
- Change selection to another option and verify previous is deselected.
- Use keyboard arrows to navigate and select options.
- Verify required radio group triggers validation when nothing selected.
- Verify initial selected value is preserved after refresh (if required).

## Negative tests
- Verify already selected option cannot be unselected directly.
- Verify clicking disabled option does not change state.
- Verify invalid value is not submitted by the form.
- Verify group behaves correctly when options are dynamically added/ removed.

## Suggested missing tests
- Verify screen reader announces selected state and group name.
- Verify focus ring appears on selected/active option.
- Verify visually hidden required marker is still available to accessibility API.
