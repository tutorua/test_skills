# Slider Control - Test Scenarios

Description: Slider (range input) scenarios.

## Requirements
- Slider must move via drag and keyboard arrows.
- Value must snap to configured steps.
- Slider must expose aria attributes for accessibility.

## Positive tests
- Drag the handle to a new value and verify the result.
- Use keyboard arrows/Home/End to adjust value.
- Verify value is correctly updated in real time.
- Verify min/max boundaries are enforced.
- Verify form submission includes slider value.

## Negative tests
- Attempt to set value outside min/max and verify it’s clamped.
- Verify disabled slider does not change value.
- Verify invalid step values are rejected.
- Verify slider state preserves after page refresh if expected.

## Suggested missing tests
- Verify tooltip displays current value while dragging.
- Verify slider can be controlled via scripting (if API provided).
- Verify visual track updates for range segments (if applicable).
