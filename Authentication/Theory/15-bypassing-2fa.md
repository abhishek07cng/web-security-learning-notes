# 15 - Bypassing 2FA

## Overview

Applications with flawed authentication logic may allow attackers to bypass Two-Factor Authentication (2FA) entirely.

Even when MFA is enabled, improper implementation can make the additional security layer ineffective.

---

## How 2FA Bypass Occurs

Many vulnerable applications incorrectly handle authentication state after validating the username and password.

In some cases:

1. Username and password are validated
2. Application creates a session
3. MFA page is displayed
4. Access control checks fail to verify MFA completion

This allows attackers to access authenticated functionality without completing the second authentication step.

---

## Common 2FA Bypass Scenarios

| Vulnerability | Description |
|---|---|
| Missing MFA Validation | Protected pages accessible before verification |
| Weak Session Handling | Session marked authenticated too early |
| Forced Browsing | Direct navigation to internal pages |
| Parameter Manipulation | Changing verification parameters |
| Broken Logic | Incomplete server-side checks |

---

## Example Vulnerable Workflow

### Intended Flow

```text
Login → MFA Verification → Authenticated Session
```

### Vulnerable Flow

```text
Login → Authenticated Session Created → MFA Page
```

In this case, attackers may skip MFA entirely.

---

## Real-World Example

Applications may use parameters such as:

```http
verify=carlos
```

to identify which account is undergoing verification.

If attackers can manipulate these parameters, they may generate or brute-force verification codes for other users.

---

## Common Testing Methodology

### Authentication State Testing

1. Log in using valid credentials
2. Intercept MFA requests
3. Attempt direct access to protected pages
4. Analyze session cookies
5. Check whether MFA completion is validated server-side

---

## Forced Browsing Testing

Attackers may directly request:

```text
/my-account
/admin
/dashboard
```

before completing MFA.

---

## Parameter Manipulation Testing

Inspect:

- hidden parameters
- verification identifiers
- session tokens
- user references

for insecure trust assumptions.

---

## Common Indicators

Attackers analyze:

- Redirect behavior
- Session cookie creation
- Access control enforcement
- Authentication state changes
- URL parameters

---

## Real-World Risks

Weak MFA logic may allow attackers to:

- Completely bypass 2FA
- Access sensitive accounts
- Escalate privileges
- Maintain unauthorized sessions

---

## Mitigation

Applications should:

- Fully validate MFA completion server-side
- Prevent session creation before MFA completion
- Enforce access control checks consistently
- Use secure session management
- Prevent parameter tampering

---

## Key Takeaways

- MFA is only as secure as its implementation.
- Broken authentication logic can completely bypass MFA.
- Session validation is critical during authentication workflows.

> [!WARNING]
> A flawed MFA implementation may provide almost no additional protection.

> [!IMPORTANT]
> Applications should never grant authenticated access before MFA verification is fully completed.