# 09 - Account Locking

## Overview

Account locking is a protection mechanism that temporarily prevents login attempts after multiple failed authentication attempts.

This is designed to slow or stop brute-force attacks.

---

## How Account Locking Works

Applications typically:

1. Count failed login attempts
2. Trigger a lockout after a threshold
3. Prevent further authentication attempts

Example:

```text
5 failed attempts → account locked for 15 minutes
```

---

## Common Weaknesses

Despite improving security, account locking has several weaknesses.

---

## Username Enumeration

Lockout messages may reveal valid usernames.

### Example

### Invalid Username

```text
Invalid username or password
```

### Valid Username

```text
Too many login attempts
```

This difference confirms the username exists.

---

## Credential Stuffing Weakness

Credential stuffing attacks often bypass account locking because:

- each account is attempted only once
- lockout thresholds are never reached

---

## Counter Reset Weakness

Some applications reset lockout counters after successful authentication.

Attackers may abuse this by alternating between:

- valid logins
- brute-force attempts

---

## Denial of Service Risk

Attackers may intentionally lock legitimate users out of their accounts.

This creates a denial-of-service condition.

---

## Attack Methodology

Attackers commonly:

1. Enumerate usernames
2. Analyze lockout thresholds
3. Rotate usernames
4. Use credential stuffing
5. Automate login attempts

---

## Mitigation

Applications should:

- Combine lockout with rate limiting
- Monitor suspicious login behavior
- Use MFA
- Detect credential stuffing
- Prevent username enumeration

---

## Key Takeaways

- Account locking alone is insufficient.
- Lockout messages may expose valid users.
- Credential stuffing bypasses many lockout systems.

> [!IMPORTANT]
> Account locking should always be combined with additional protections such as MFA and rate limiting.