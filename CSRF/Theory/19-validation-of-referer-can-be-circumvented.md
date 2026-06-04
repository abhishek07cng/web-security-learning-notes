# Validation of Referer Can Be Circumvented

## Overview

Some applications attempt to validate the Referer header but implement the validation incorrectly.

Instead of validating the actual hostname, they perform weak string matching.

This allows attackers to craft Referer values that appear legitimate.

---

# Common Weak Validation

Example:

```php
if (strpos(
    $referer,
    "target.com"
) !== false)
{
    allow_request();
}
```

Problem:

```text
Any URL Containing
target.com
Will Pass
```

---

# Example Bypass

Expected:

```http
Referer:
https://target.com/profile
```

---

Attacker:

```http
Referer:
https://evil.com?target.com
```

---

Result:

```text
Validation Passed
```

because:

```text
target.com
```

exists somewhere in the string.

---

# Another Example

```http
Referer:
https://target.com.evil.com
```

---

Result:

```text
Validation Passed
```

even though:

```text
Actual Host
=
evil.com
```

---

# Why Developers Make This Mistake

Developers often validate:

```text
Entire URL String
```

instead of:

```text
Hostname Component
```

---

# Proper Validation

Incorrect:

```php
strpos(
$referer,
"target.com"
)
```

---

Correct:

```php
$host =
parse_url(
$referer,
PHP_URL_HOST
);

if(
$host === "target.com"
)
{
    allow_request();
}
```

---

# Modern Browser Challenge

Many browsers strip:

```text
Query Strings
```

from Referer values.

Example:

```http
Referer:
https://evil.com/
```

instead of:

```http
Referer:
https://evil.com/?target.com
```

---

# Why This Matters

Your bypass may work in Burp Repeater but fail inside a real browser.

---

# Solution

Use:

```html
<meta name="referrer"
content="unsafe-url">
```

or:

```http
Referrer-Policy:
unsafe-url
```

---

# Effect

Browser sends:

```http
Referer:
https://evil.com/?target.com
```

including the query string.

---

# Common Referer Bypasses

## Query String Injection

```http
https://evil.com?target.com
```

---

## Subdomain Injection

```http
https://target.com.evil.com
```

---

## Path Injection

```http
https://evil.com/target.com
```

---

## Fragment Injection

```http
https://evil.com/#target.com
```

---

# Testing Methodology

```text
Capture Request
        ↓
Replace Referer
        ↓
Observe Validation
        ↓
Try Substring Payloads
        ↓
Request Accepted?
        ↓
VULNERABLE
```

---

# Indicators Of Weak Validation

Accepted:

```http
Referer:
https://evil.com?target.com
```

Accepted:

```http
Referer:
https://target.com.evil.com
```

Accepted:

```http
Referer:
https://evil.com/target.com
```

---

# Attack Flow

```text
Weak Referer Validation
        ↓
Craft Malicious Referer
        ↓
Browser Sends Request
        ↓
Server Finds Expected String
        ↓
Validation Bypassed
```

---

# Related Lab

- `lab12-csrf-with-broken-referer-validation.md`

---

# Related Payloads

- `referer-bypass-techniques.md`
- `csrf-referer-cheatsheet.md`

---

# Key Takeaways

- String matching is not proper Referer validation.
- Hostname validation is required.
- Modern browsers may strip query strings.
- Referrer-Policy can affect exploit reliability.

> [!IMPORTANT]
> Always validate the hostname component of the Referer URL, not whether a string merely appears somewhere inside it.