# Date Picker - Test Scenarios

Description: Calendar date-picker selection scenarios.

## Requirements
- Users must be able to pick a date from the calendar UI.
- Input must validate date format and restrict invalid dates.
- Required date field must enforce selection.

## Positive tests
- Select a valid date and verify the value is set.
- Navigate between months and select dates in adjacent months.
- Enter a valid date manually and verify it’s accepted.
- Verify keyboard navigation works for date selection.
- Verify date field clears when using clear control (if provided).

## Negative tests
- Enter an invalid date and verify validation message displayed.
- Try selecting a disabled/unavailable date (past or out of range).
- Verify empty required date submission triggers validation.
- Verify malformed date strings are rejected.

## Suggested missing tests
- Verify localization (date format and week start day) behavior.
- Verify leap year date selection works correctly (Feb 29).
- Verify component handles daylight savings and timezone-related display properly.
