# Textarea Testing Scenarios

## Element Overview
The Textarea element has two variations: Single Textarea and Multiple Textareas.

## Requirements Summary

### Single Textarea
- Required field named "Text area"
- Accepts any text input
- Submit via Submit button
- After submit: entered text displayed on page

### Multiple Textareas
- Three textarea fields:
  1. "First chapter" (required)
  2. "Second chapter" (optional)
  3. "Third chapter" (optional)
- Users enter text in any/all fields
- After submit: all entered text displayed on page

---

## Test Cases

### Single Textarea - Positive Tests
1. **Enter simple text**: Type "Hello World" in textarea and submit
   - Expected: "Hello World" displayed on page

2. **Enter multi-line text**: Enter text with line breaks and submit
   - Expected: Text displayed with line breaks preserved

3. **Enter long text**: Type substantial paragraph and submit
   - Expected: Full text displayed on page

4. **Enter special characters**: Type "Test@123!#$" and submit
   - Expected: Special characters preserved in display

5. **Enter whitespace**: Include leading/trailing spaces and submit
   - Expected: Whitespace preserved in result

6. **Empty field then fill**: Clear and retype text multiple times
   - Expected: Latest text is submitted correctly

7. **Copy-paste content**: Paste text from clipboard and submit
   - Expected: Pasted content displayed correctly

### Single Textarea - Negative Tests
1. **Submit empty field**: Leave empty and click Submit
   - Expected: Error or validation message (required field)

2. **Only whitespace**: Enter only spaces and submit
   - Expected: Depending on validation, either accepted or rejected

3. **Attempt to bypass required**: Try to submit without entering text
   - Expected: Form validation prevents submission

### Single Textarea - Omitted Tests (Suggested)
1. Maximum/minimum character limits
2. Text formatting options (if any)
3. Spell check suggestions
4. Character counter display
5. Auto-save functionality
6. Undo/Redo functionality
7. Drag and drop file support
8. Mobile keyboard behavior
9. Accessibility (screen reader support)
10. Tab behavior within textarea

---

### Multiple Textareas - Positive Tests
1. **Fill only required field**: Enter text only in "First chapter" and submit
   - Expected: First chapter text displayed

2. **Fill all three fields**: Enter text in all three textareas and submit
   - Expected: All three texts displayed on page

3. **Fill first and second**: Enter text in "First" and "Second" chapters, skip "Third"
   - Expected: First and Second displayed, Third empty or omitted

4. **Fill first and third**: Enter text in "First" and "Third", skip "Second"
   - Expected: First and Third displayed, Second empty or omitted

5. **Multi-line in each field**: Each textarea has text on multiple lines
   - Expected: All line breaks preserved in results

6. **Different content lengths**: First chapter short, others longer
   - Expected: Each displayed with correct length

7. **Special characters in each**: Each field has different special chars
   - Expected: All special characters preserved

8. **Unicode content**: Enter text with unicode characters (emoji, accents)
   - Expected: Unicode preserved in display

### Multiple Textareas - Negative Tests
1. **Skip required field (First chapter)**: Leave "First chapter" empty, fill "Second" and "Third"
   - Expected: Error or validation message

2. **All empty fields**: Leave all three empty and submit
   - Expected: Error (First chapter required)

3. **Whitespace in required field**: Enter only spaces in "First chapter"
   - Expected: Depending on validation, accepted or rejected

4. **Very long text in required field**: Paste huge amount of text in "First chapter"
   - Expected: Handled properly (no crash, truncation, or errors)

### Multiple Textareas - Omitted Tests (Suggested)
1. Maximum character limits per field
2. Field dependencies (do optional fields depend on first field)
3. Display order of submitted textareas
4. Format of submitted results (separate sections, concatenated, etc.)
5. Newline handling in results display
6. Character encoding for special content
7. Copy-paste between textareas
8. Tab navigation between textareas
9. Accessibility labels for each field
10. Mobile responsiveness of textarea sizing
11. Scroll behavior within textareas
12. Mixed RTL and LTR text
