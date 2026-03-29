# Checkbox Testing Scenarios

## Element Overview
The Checkbox element has two variations: Single Checkbox and Multiple Checkboxes.

## Requirements Summary

### Single Checkbox
- One checkbox labeled "Select me or not"
- User can select/deselect checkbox
- Submit button always enabled
- Unchecked: no result displayed
- Checked: checkbox name displayed in result

### Multiple Checkboxes
- Three checkboxes labeled: "One", "Two", "Three"
- User can select any combination
- Submit button always enabled
- No selection: no result displayed
- Selection: selected checkbox names displayed in result

---

## Test Cases

### Single Checkbox - Positive Tests
1. **Check checkbox**: Click unchecked checkbox
   - Expected: Checkbox becomes checked

2. **Uncheck checkbox**: Click checked checkbox
   - Expected: Checkbox becomes unchecked

3. **Submit when unchecked**: Leave unchecked and click Submit
   - Expected: No result displayed on page

4. **Submit when checked**: Check checkbox and click Submit
   - Expected: "Select me or not" displayed in result

5. **Toggle multiple times**: Check and uncheck repeatedly
   - Expected: Checkbox state toggles correctly each time

6. **Label click**: Click on label text "Select me or not"
   - Expected: Checkbox toggles

7. **Visual feedback**: Check checkbox
   - Expected: Checked state visually indicated (checkmark/filled box)

### Single Checkbox - Negative Tests
1. **Submit button state**: Verify Submit button is always enabled
   - Expected: Button never disabled (even when unchecked)

2. **Result appear when unchecked**: Leave unchecked and submit
   - Expected: Result section empty or hidden

3. **Incorrect content in result**: Submit checked checkbox
   - Expected: Only "Select me or not" shown, nothing extra

### Single Checkbox - Omitted Tests (Suggested)
1. Keyboard navigation (Tab to checkbox, Space to toggle)
2. Browser default checkbox appearance
3. Multiple submissions with same state
4. Result persistence/clearing between submissions
5. Accessibility (ARIA attributes)
6. Touch/mobile checkbox behavior
7. Focus states and keyboard accessibility

---

### Multiple Checkboxes - Positive Tests
1. **Check first checkbox**: Click "One" checkbox
   - Expected: "One" becomes checked

2. **Check multiple checkboxes**: Select "One" and "Two"
   - Expected: Both checkboxes checked

3. **Check all checkboxes**: Select all three
   - Expected: All checkboxes checked

4. **Submit with single selection**: Check only "Two" and submit
   - Expected: "Two" displayed in result

5. **Submit with multiple selections**: Check "One" and "Three" and submit
   - Expected: "One" and "Three" displayed in result

6. **Submit with all selected**: Check all three and submit
   - Expected: "One", "Two", "Three" all displayed in result

7. **Uncheck one of multiple**: Check all, then uncheck "Two", submit
   - Expected: "One" and "Three" displayed (missing "Two")

8. **Label text verification**: Verify checkbox labels
   - Expected: Labels show "One", "Two", "Three"

9. **Uncheck checkbox**: Click checked checkbox to uncheck
   - Expected: Checkbox becomes unchecked

### Multiple Checkboxes - Negative Tests
1. **Submit without selection**: Don't check any and click Submit
   - Expected: No result displayed (empty)

2. **No extra content in result**: Submit with selections
   - Expected: Only checked checkbox names in result, no duplicates

3. **Incorrect checkbox names**: Check and submit
   - Expected: Correct names displayed (not "1st", "2nd", "3rd" etc.)

4. **Submit button state**: Verify always enabled
   - Expected: Button never disabled regardless of selection

### Multiple Checkboxes - Omitted Tests (Suggested)
1. Keyboard navigation between checkboxes
2. Select/Unselect all functionality (if applicable)
3. Result display order (alphabetical or selection order)
4. Result formatting with multiple selections
5. Case sensitivity in result text
6. Maximum selections behavior
7. Holding Shift to select range
8. Browser native checkbox behavior
9. Focus management when checking
10. Accessibility labels
