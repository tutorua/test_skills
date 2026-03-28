# File Upload - Test Scenarios

Description: Single file upload control scenarios.

## Requirements
- Users must be able to select a file and upload it successfully.
- Allowed file types and max size must be enforced.
- Upload progress and success/failure messaging must be displayed.

## Positive tests
- Upload a valid file and verify success flow.
- Verify drag-and-drop upload works (if provided).
- Verify multiple file behavior is unsupported/disabled for single file mode.
- Verify canceling upload stops in-progress upload.
- Verify selected file details (name/size/type) appear correctly.

## Negative tests
- Attempt upload of disallowed file type and verify error.
- Attempt upload of a file larger than max size and verify error.
- Verify system handles network failure during upload gracefully.
- Verify uploading when required and empty triggers validation.

## Suggested missing tests
- Verify filename sanitization protections (special chars, path injection) in UI display.
- Verify resubmitting same file works as expected.
- Verify malware scan warning path (if part of requirements).
