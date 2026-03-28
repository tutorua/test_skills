# Text Input - Test Scenarios

## Text input

### Description: Simple text input field scenarios

### Requirements
- This is a required field
- User should be able to enter text into this field
- Text should be a valid string consisting of English letters, numbers, underscores or hyphens
- Text length limits:
  - Max: 25 characters
  - Min: 2 characters
- User can submit this one-field form by pressing Enter
- After submitting the form, the text entered by the user is displayed on the page

### Positive tests
- Enter valid text (2-25 characters, English letters, numbers, underscores, hyphens) and verify it's accepted.
- Enter minimum length text (2 characters) and verify it's accepted.
- Enter maximum length text (25 characters) and verify it's accepted.
- Submit form by pressing Enter key and verify form submission.
- Verify submitted text is displayed on the page after form submission.
- Enter text with allowed special characters (underscores, hyphens) and verify acceptance.
- Enter mixed alphanumeric text and verify it's accepted.

### Negative tests
- Leave field empty and verify required field validation error.
- Enter text shorter than 2 characters and verify validation error.
- Enter text longer than 25 characters and verify it's rejected or truncated.
- Enter text with prohibited characters (special symbols, spaces) and verify validation error.
- Try submitting empty form and verify validation prevents submission.

### Suggested missing tests
- Verify autocomplete and suggestions (if enabled) behave correctly.
- Verify input retains value on back/forward browser navigation (if expected).
- Verify invalid formatted text shows correct error messages (for email/number/etc.).

## Email Field

### Description
Email input field for collecting valid email addresses with specific validation rules.

### Requirements
- Entered text should be a valid email address
- "localhost" domain should be allowed
- User can submit this one-field form by pressing Enter
- After submitting the form, the text entered by the user is displayed on the page

### Positive tests
- Enter valid email addresses (e.g., user@example.com, test.email+tag@domain.org) and verify acceptance.
- Enter email with localhost domain (e.g., user@localhost) and verify it's accepted.
- Submit form by pressing Enter key and verify form submission.
- Verify submitted email is displayed on the page after form submission.
- Enter email with valid special characters in local part (dots, plus signs) and verify acceptance.
- Enter email with subdomain (e.g., user@sub.domain.com) and verify acceptance.

### Negative tests
- Enter invalid email formats (missing @, missing domain, spaces in domain) and verify validation error.
- Enter email with invalid domain (e.g., user@.com, user@domain.) and verify rejection.
- Enter email with consecutive dots in domain and verify validation error.
- Enter email without local part (e.g., @domain.com) and verify rejection.
- Try submitting empty form and verify validation prevents submission.

### Suggested missing tests
- Verify email validation handles international characters (UTF-8) correctly.
- Test very long email addresses (close to RFC limits) for acceptance.
- Verify case-insensitive domain handling.
- Test email addresses with IP addresses in domain part (e.g., user@[192.168.1.1]).
- Verify behavior with leading/trailing whitespace in email input.

## Password Field

### Description
Password input field with strong validation requirements for security.

### Requirements
- Has minimum 8 characters in length
- At least one uppercase English letter
- At least one lowercase English letter
- At least one digit
- At least one special character
- User can submit this one-field form by pressing Enter
- After submitting the form, the text entered by the user is displayed on the page

### Positive tests
- Enter password with minimum 8 characters including uppercase, lowercase, digit, and special character (e.g., "Passw0rd!") and verify acceptance.
- Enter password longer than 8 characters meeting all requirements and verify acceptance.
- Submit form by pressing Enter key and verify form submission.
- Verify submitted password is displayed on the page after form submission.
- Enter password with various special characters (!@#$%^&*) and verify acceptance.
- Enter password with numbers and letters in different positions and verify acceptance.

### Negative tests
- Enter password shorter than 8 characters and verify validation error.
- Enter password without uppercase letter and verify validation error.
- Enter password without lowercase letter and verify validation error.
- Enter password without digit and verify validation error.
- Enter password without special character and verify validation error.
- Try submitting empty form and verify validation prevents submission.

### Suggested missing tests
- Verify password masking/hiding functionality works correctly.
- Test password field autocomplete behavior (should typically be disabled).
- Verify copy/paste functionality in password field.
- Test password strength indicator (if present) updates correctly.
- Verify password field handles very long passwords (100+ characters).
- Test password validation with Unicode special characters.
