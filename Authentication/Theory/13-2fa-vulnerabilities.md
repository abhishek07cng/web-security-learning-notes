# 13 - 2FA Vulnerabilities

## Overview

Two-Factor Authentication (2FA) improves security, but weak implementations can still be bypassed.

Applications often introduce vulnerabilities through flawed verification logic or poor session management.

---

## Common 2FA Vulnerabilities

| Vulnerability | Description |
|---|---|
| Broken Verification Logic | Missing validation checks |
| Predictable Codes | Easily guessable tokens |
| Session Mismanagement | Premature authentication state |
| Weak Rate Limiting | Unlimited verification attempts |
| Token Reuse | Reusable verification codes |

---

## Broken Authentication State

Some applications place users into a partially authenticated session immediately after password validation.

If the application fails to enforce 2FA completion properly, attackers may bypass MFA entirely.

---

## Example Scenario

### Vulnerable Workflow

1. User enters valid username/password
2. Application creates authenticated session
3. Application requests MFA code
4. Attacker directly accesses authenticated pages
5. Application fails to validate MFA completion

---

## Common Testing Methodology

1. Authenticate using valid credentials
2. Intercept MFA requests
3. Attempt direct navigation to protected pages
4. Analyze session behavior
5. Test bypass scenarios

---

## Common Indicators

Attackers analyze:

- Session cookies
- Redirect behavior
- Access control enforcement
- Authentication state handling

---

## Real-World Risks

Weak MFA implementations may allow attackers to:

- Bypass MFA entirely
- Access protected accounts
- Escalate privileges
- Maintain persistent sessions

---

## Mitigation

Applications should:

- Validate MFA server-side
- Prevent premature authentication states
- Require complete MFA validation before granting access
- Use secure session management

---

## Key Takeaways

- MFA logic flaws can completely bypass additional security layers.
- Session validation is critical during authentication.
- Proper server-side verification is essential.

> [!WARNING]
> A broken MFA implementation may provide little additional security over password-only authentication.