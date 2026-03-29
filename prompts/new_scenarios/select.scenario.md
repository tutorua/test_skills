# Select/Dropdown Testing Scenarios

## Element Overview
The Select element has two variations: Single Select and Multiple Selects.

## Requirements Summary

### Single Select
- Required field: "Choose language"
- Options available to select from
- Submit button sends selection
- After submit: selected option displayed on page

### Multiple Selects
- Three required fields:
  1. "Choose the place you want to go"
  2. "Choose how you want to get there"
  3. "Choose when you want to go"
- User selects option from each dropdown
- Result phrase: "to go by <transport> to the <destination> <when>"
- All selections must be made before meaningful result

---

## Test Cases

### Single Select - Positive Tests
1. **Select first option**: Open dropdown and select first language option
   - Expected: Option selected and highlighted

2. **Select different options**: Select different languages sequentially
   - Expected: Previously selected option deselected, new one selected

3. **Submit with selection**: Select an option and click Submit
   - Expected: Selected language displayed on page

4. **Verify all options available**: Open dropdown
   - Expected: All language options visible and selectable

5. **Default state**: Load page
   - Expected: Dropdown shows placeholder/no selection state

6. **Reselect same option**: Select option, close dropdown, open and select same
   - Expected: Option remains selectable

7. **Submit multiple selections**: Select different options and submit multiple times
   - Expected: Each submission shows correct selection

### Single Select - Negative Tests
1. **Submit without selection**: Click Submit without selecting option
   - Expected: Error or validation message (required field)

2. **Attempt to leave empty**: Try to submit form without selection
   - Expected: Cannot proceed without selection

3. **Invalid option selection**: Try to select non-existent option
   - Expected: Cannot select invalid value

### Single Select - Omitted Tests (Suggested)
1. Keyboard navigation (arrow keys) in dropdown
2. Search/filter within dropdown options
3. Dropdown scroll if many options
4. Mobile/touch dropdown behavior
5. Dropdown appearance/styling consistency
6. Option hover states
7. keyboard Enter/Space to select
8. Label association with dropdown

---

### Multiple Selects - Positive Tests
1. **Select from first dropdown**: Open "destination" dropdown and select option
   - Expected: Option selected in first dropdown

2. **Select from all three dropdowns**: Make selections in all three fields
   - Expected: All three selections visible/active

3. **Submit with all selections**: Select options from all dropdowns and submit
   - Expected: Result phrase displays with all three values filled correctly

4. **Verify result format**: Select "Sea" destination, "Car" transport, "Today" time and submit
   - Expected: "to go by Car to the Sea Today" displays

5. **Different combination**: Select different options and submit
   - Expected: Result updates with new values

6. **Reselect and resubmit**: Change selections and submit again
   - Expected: Result updates to match new selections

7. **Verify all combinations work**: Test multiple valid combinations
   - Expected: All produce correctly formatted results

### Multiple Selects - Negative Tests
1. **Submit without all selections**: Select only one or two fields, skip others
   - Expected: Error or validation message (all required)

2. **Partial submission**: Fill destination only, leave transport and time empty
   - Expected: Cannot submit (required fields)

3. **Incorrect phrase format**: Submit with all selections
   - Expected: Result follows exact format "to go by <X> to the <Y> <Z>"

4. **Missing values in result**: Submit with selections
   - Expected: All three values present in result (no empty values)

### Multiple Selects - Omitted Tests (Suggested)
1. Order of selections (does order affect result?)
2. Result grammar/articles ("to the" vs "at")
3. Maximum length of composed result
4. Special characters in option values
5. Case sensitivity in result
6. Result field read-only status
7. Copy/paste result value
8. Browser dropdown performance with many options
9. Persistence of selections after navigation
10. Tab order through3 dropdowns
11. Accessibility labels for all three fields
