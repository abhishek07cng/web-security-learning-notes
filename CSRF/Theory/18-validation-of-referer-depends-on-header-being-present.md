# Validation of Referer Depends on Header Being Present

## Overview

Some applications attempt to use the Referer header as a CSRF defense.

However, a common implementation flaw occurs when the application validates the Referer only if the header exists and skips validation when it is absent.

---

# Vulnerable Logic

Example:

```python
if referer:
    validate(referer)
else:
    allow_request()
```

This means:

```text
Referer Present
        ↓
Validation Occurs

Referer Missing
        ↓
Request Allowed
```

---

# Why This Is Dangerous

An attacker can intentionally cause the victim's browser to omit the Referer header.

As a result:

```text
Validation Never Happens
        ↓
CSRF Attack Succeeds
```

---

# Identifying The Vulnerability

## Step 1

Capture a sensitive request.

Example:

```http
POST /my-account/change-email

email=test@test.com
```

---

## Step 2

Modify Referer:

```http
Referer: https://evil.com
```

---

## Result

```text
Request Rejected
```

Application validates Referer.

---

## Step 3

Delete Referer completely.

```http
POST /my-account/change-email

email=test@test.com
```

---

## Result

```text
Request Accepted
```

Vulnerability confirmed.

---

# Why It Happens

Developers often assume:

```text
Missing Referer
        ↓
Legitimate Browser Behavior
```

and therefore allow the request.

Attackers exploit this assumption.

---

# Suppressing Referer

Browsers can be instructed to remove the Referer header.

---

## HTML Method

```html
<meta name="referrer"
content="no-referrer">
```

---

## Browser Behavior

```text
Victim Visits Exploit Page
        ↓
CSRF Form Submitted
        ↓
Referer Omitted
        ↓
Validation Skipped
        ↓
Request Accepted
```

---

# Attack Flow

```text
Capture Sensitive Request
        ↓
Verify Referer Validation
        ↓
Delete Referer
        ↓
Request Accepted
        ↓
Create CSRF PoC
        ↓
Add no-referrer
        ↓
Deliver Exploit
```

---

# Why Traditional CSRF Defenses Are Better

Unlike Referer:

```text
CSRF Tokens
```

cannot simply be removed by browser behavior.

---

# Common Testing Methodology

```text
Change Referer
        ↓
Rejected?

YES
        ↓
Delete Referer
        ↓
Accepted?

YES
        ↓
VULNERABLE
```

---

# Related Lab

- `lab11-referer-validation-depends-on-header-being-present.md`

---

# Related Payloads

- `referer-bypass-techniques.md`
- `csrf-referer-cheatsheet.md`

---

# Key Takeaways

- Referer validation must not be optional.
- Missing Referer should never bypass security checks.
- Meta referrer policies can suppress Referer completely.

> [!WARNING]
> If removing the Referer header causes a protected action to succeed, the application is vulnerable to CSRF.