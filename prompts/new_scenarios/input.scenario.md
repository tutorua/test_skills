# Input Field Testing Scenarios

## Element Overview
The Input Field element has three variations: Text Input, Email Field, and Password Field.

## Requirements Summary

### Text Input
- Required field with name "Text string"
- Must accept text containing English letters, numbers, underscores, or hyphens
- Character length constraints: Min 2, Max 25 characters
- Submit via Enter key or Submit button
- Page displays entered text after submission

### Email Field
- Accepts valid email addresses including localhost domain
- Submit via Enter key or Submit button
- Page displays entered email after submission

### Password Field
- Minimum 8 characters
- Must contain at least one uppercase letter
- Must contain at least one lowercase letter
- Must contain at least one digit
- Must contain at least one special character
- Submit via Enter key or Submit button
- Page displays entered password after submission

---

## Test Cases

### Text Input - Positive Tests
1. **Valid text with letters**: Enter 'TestName' and submit
   - Expected: Text displayed on page

2. **Valid text with numbers**: Enter 'Test123' and submit
   - Expected: Text displayed on page

3. **Valid text with underscores**: Enter 'Test_Name' and submit
   - Expected: Text displayed on page

4. **Valid text with hyphens**: Enter 'Test-Name' and submit
   - Expected: Text displayed on page

5. **Minimum length (2 chars)**: Enter 'AB' and submit
   - Expected: Text displayed on page

6. **Maximum length (25 chars)**: Enter 'ABCDEFGHIJKLMNOPQRSTUVWXY' and submit
   - Expected: Text displayed on page

7. **Submit via Enter key**: Enter 'TestName' and press Enter
   - Expected: Text displayed on page

8. **Submit via Submit button**: Enter 'TestName' and click Submit
   - Expected: Text displayed on page

### Text Input - Negative Tests
1. **Below minimum length (1 char)**: Enter 'A' and submit
   - Expected: Error or form rejection

2. **Above maximum length (26 chars)**: Enter 'ABCDEFGHIJKLMNOPQRSTUVWXYZA' and submit
   - Expected: Error or form rejection

3. **Invalid characters (spaces)**: Enter 'Test Name' and submit
   - Expected: Error or form rejection

4. **Invalid characters (special chars)**: Enter 'Test@Name#' and submit
   - Expected: Error or form rejection

5. **Empty field submission**: Submit without entering text
   - Expected: Error (required field)

### Text Input - Omitted Tests (Suggested)
1. Leading/trailing whitespace handling
2. Case sensitivity validation
3. Copy-paste and cut operations
4. Text field focus behavior
5. Field readonly/disabled states

---

### Email Field - Positive Tests
1. **Standard email format**: Enter 'user@example.com' and submit
   - Expected: Email displayed on page

2. **Email with numbers**: Enter 'user123@example.com' and submit
   - Expected: Email displayed on page

3. **Email with dots in local part**: Enter 'first.last@example.com' and submit
   - Expected: Email displayed on page

4. **Localhost domain**: Enter 'user@localhost' and submit
   - Expected: Email displayed on page

5. **Multiple subdomains**: Enter 'user@mail.example.co.uk' and submit
   - Expected: Email displayed on page

### Email Field - Negative Tests
1. **Missing @ symbol**: Enter 'userexample.com' and submit
   - Expected: Enter a valid email address.

2. **Missing local part**: Enter '@example.com' and submit
   - Expected: Enter a valid email address.

3. **Missing domain**: Enter 'user@' and submit
   - Expected: Enter a valid email address.

4. **Invalid characters**: Enter 'user#name@example.com' and submit
   - Expected: Enter a valid email address.

5. **Empty field submission**: Submit without entering email
   - Expected: Enter a valid email address.

6. **Space in email**: Enter 'user @example.com' and submit
   - Expected: Enter a valid email address.

### Email Field - Omitted Tests (Suggested)
1. Long email address handling (RFC 5321 limits)
2. Internationalized domain names (IDN)
3. Plus addressing (user+tag@domain)
4. Case sensitivity of email domains
5. Disposable email domain validation

---

### Password Field - Positive Tests
1. **All requirements met**: Enter 'StrongPass1!' and submit
   - Expected: Password displayed on page

2. **Minimum valid password**: Enter 'Aaa1@bbb' (8 chars) and submit
   - Expected: Password displayed on page

3. **Complex password**: Enter 'MySecureP@ss2024' and submit
   - Expected: Password displayed on page

4. **Multiple special characters**: Enter 'Pass@word!#$%' and submit
   - Expected: Password displayed on page

5. **All uppercase + digit + special**: Enter 'STRONG1!' and submit
   - Expected: Password displayed on page

### Password Field - Negative Tests
1. **Missing uppercase**: Enter 'lowercase1@pass' and submit
   - Expected: Low password complexity

2. **Missing lowercase**: Enter 'UPPERCASE1@PASS' and submit
   - Expected: Low password complexity

3. **Missing digit**: Enter 'NoDigit@Password' and submit
   - Expected: Low password complexity

4. **Missing special character**: Enter 'StrongPass123' and submit
   - Expected: Low password complexity

5. **Below minimum length (7 chars)**: Enter 'Short1@' and submit
   - Expected: Low password complexity

6. **Only special characters**: Enter '@#$%^&*!' and submit
   - Expected: Low password complexity

7. **Empty field submission**: Submit without entering password
   - Expected: Please fill out this field

### Password Field - Omitted Tests (Suggested)
1. Password strength meter display
2. Show/hide password toggle
3. Password confirmation field requirement
4. Common password blacklist validation
5. Password history/reuse prevention
6. Maximum length constraints
7. Consecutive character restrictions
