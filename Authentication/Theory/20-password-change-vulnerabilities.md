# 20 - Password Change Vulnerabilities

## Overview

Password change functionality allows authenticated users to update their credentials.

Although users are already authenticated, weak implementations may still introduce severe security vulnerabilities.

---

## Typical Password Change Workflow

Applications commonly require:

1. Current password
2. New password
3. Confirmation of new password

This helps verify that the legitimate user initiated the request.

---

## Common Weaknesses

| Weakness | Description |
|---|---|
| Missing Current Password Validation | Password changes without verification |
| Hidden Username Parameters | Username manipulation attacks |
| Weak Session Validation | Unauthorized password updates |
| Information Disclosure | Password enumeration via error messages |

---

## Hidden Parameter Vulnerabilities

Some applications include usernames as hidden form fields:

```html
<input type=\"hidden\" name=\"username\" value=\"carlos\">
```

Attackers may modify this value and target arbitrary accounts.

---

## Password Enumeration Through Error Messages

Applications sometimes reveal authentication state through inconsistent error messages.

Example:

### Invalid Current Password

```text
Current password incorrect
```

### Valid Current Password + Mismatched New Passwords

```text
New passwords do not match
```

Attackers can abuse these differences to identify valid passwords.

---

## Brute-Force Workflow

Attackers may:

1. Intercept password change request
2. Modify username parameter
3. Automate current-password guesses
4. Analyze response differences
5. Identify valid credentials

---

## Common Testing Methodology

During testing, analyze:

- hidden parameters
- session validation
- response messages
- brute-force protections
- authentication logic

---

## Real-World Risks

Weak password change functionality may allow attackers to:

- brute-force credentials
- compromise accounts
- reset arbitrary passwords
- bypass authentication protections

---

## Prevention

Applications should:

- Require current-password validation
- Prevent hidden parameter manipulation
- Normalize error messages
- Implement rate limiting
- Enforce secure session validation

---

## Best Practices

Applications should:

- invalidate sessions after password changes
- require re-authentication for sensitive actions
- monitor suspicious password modifications

---

## Key Takeaways

- Password change functionality can become an authentication attack surface.
- Error message inconsistencies may leak sensitive information.
- Hidden parameters should never be trusted.

> [!IMPORTANT]
> Sensitive account actions should always require strong server-side validation.

> [!TIP]
> During testing, carefully compare application behavior for valid and invalid password attempts.