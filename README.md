# email-validator

Built an Email Validator Engine which validates if the email address is correct and email to be sent is correct.

`validate_email_addr` validates following points:
- The email address length excluding starting and ending spaces should not be greater than 254 characters.
- There should not be mote than 1 '@' in the email address.
- The length of email address before '@' should not be more than 64 characters.
- The length of email address after '@' should not be more than 251 characters.
- The email address should only consist of small case and upper case alphabets, digits, '@', '-' and '.'.
- The email part before '@' must not have '-' or '.' as the first or last character.
- The email part after '@' should always end with either '.com', '.net' or '.org'.

`validate_email_payload` validates following points:
- Length of the sender name excluding starting and ending spaces should be greater than 5 characters and less than 30 characters.
- Length of the receiver name excluding starting and ending spaces should be greater than 5 characters and less than 60 characters.
- All the keys given in replacements key must be used in the html.
