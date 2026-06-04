# What is the Referer Header?

## Overview

The Referer header is an HTTP request header that indicates the URL of the page that initiated the request.

Browsers automatically include this header in many situations.

---

# Example

```http
POST /change-email HTTP/1.1
Host: bank.com

Referer:
https://bank.com/profile
```

---

# Purpose

The Referer header allows servers to determine:

```text
Where A Request Came From
```

---

# Common Uses

- Analytics
- Logging
- Access control
- CSRF protection

---

# Referer-Based CSRF Protection

Applications may validate:

```http
Referer:
https://bank.com/profile
```

before processing sensitive requests.

---

# Typical Validation Logic

```python
if referer.startswith(
"https://bank.com"
):
    allow_request()
else:
    block_request()
```

---

# Why Applications Use Referer Validation

Goal:

```text
Block Requests
From External Websites
```

---

# Weakness 1 - Referer Is Optional

Browsers are not required to send it.

Reasons include:

- Privacy settings
- Browser extensions
- Security policies

---

# Example

```http
POST /change-email

Cookie: session=abc123

email=test@test.com
```

No Referer header present.

---

# Weakness 2 - Referrer Policy

Pages can explicitly suppress Referer.

HTML:

```html
<meta name="referrer"
content="no-referrer">
```

---

HTTP:

```http
Referrer-Policy:
no-referrer
```

---

# Browser Result

```text
Request Sent
        ↓
Referer Omitted
```

---

# Why Pentesters Test Referer

Questions:

```text
Is Referer Checked?
Is Referer Required?
Can Referer Be Manipulated?
```

---

# Related Theory

- `18-validation-of-referer-depends-on-header-being-present.md`
- `19-validation-of-referer-can-be-circumvented.md`

---

# Related Labs

- Lab11
- Lab12

---

# Key Takeaways

- Referer indicates where a request originated.
- Many applications use it as a CSRF defense.
- Browsers may omit Referer entirely.
- Referer validation alone is not reliable.

> [!IMPORTANT]
> Referer validation should be considered an additional defense, not a replacement for CSRF tokens.