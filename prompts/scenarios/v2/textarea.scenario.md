# Text Area - Test Scenarios

Description: Multi-line text area scenarios.

## Requirements
- Text area must preserve line breaks and be editable with keyboard actions.
- Maxlength must enforce limits and provide validation states.
- Required text area must reject empty submissions.

## Positive tests
- Enter multiple lines of text and verify newline preservation.
- Paste large text and verify it is accepted up to maxlength.
- Use keyboard shortcuts (Ctrl+A, Ctrl+V) and verify behavior.
- Verify autosize (if present) adjusts height appropriately.
- Submit form with text area content and verify submission includes content.

## Negative tests
- Enter text exceeding maxlength and verify truncation or validation.
- Verify required validation when left empty if applicable.
- Verify special characters do not break layout or submit unexpectedly.
- Verify large inputs do not crash the client or server.

## Suggested missing tests
- Verify soft wrap works as expected and line breaks are preserved.
- Verify keyboard shortcuts for undo/redo are supported.
- Verify native mobile keyboard behavior is correct on touch devices.
