# CSP frame-ancestors

## Overview

The `frame-ancestors` directive is the Content Security Policy mechanism used to control which origins are allowed to embed a page.

It is particularly important when assessing and preventing clickjacking.

---

# Basic Concept

```text
Target Response
       ↓
Content-Security-Policy
       ↓
frame-ancestors
       ↓
Browser Checks Framing Origin
       ↓
Allow or Block
```

---

# Prevent All Framing

Use:

```http
Content-Security-Policy: frame-ancestors 'none';
```

This specifies that the page must not be embedded by another page.

Conceptually:

```text
Attacker Origin
      ↓
Attempts iframe
      ↓
frame-ancestors 'none'
      ↓
Blocked
```

---

# Allow Same-Origin Framing

Use:

```http
Content-Security-Policy: frame-ancestors 'self';
```

This permits framing by the same origin.

Conceptually:

```text
Same Origin
     ↓
Allowed
```

```text
Other Origin
     ↓
Blocked
```

---

# Allow Specific Origin

A site can explicitly allow a trusted origin.

Example:

```http
Content-Security-Policy: frame-ancestors normal-website.com;
```

The specified origin is permitted to frame the page.

---

# Multiple Allowed Origins

A framing policy can specify trusted origins as required by the application's design.

The important principle is:

```text
Only explicitly trusted framing origins
should be permitted.
```

---

# Clickjacking Relationship

Basic clickjacking requires:

```text
Attacker Page
      ↓
iframe
      ↓
Target Page
```

If the target uses:

```http
Content-Security-Policy: frame-ancestors 'none';
```

the browser prevents the target page from being embedded.

Therefore:

```text
No iframe
   ↓
No framed target interface
   ↓
Basic clickjacking prevented
```

---

# Checking frame-ancestors

In Burp Suite:

```text
Proxy
  ↓
HTTP history
  ↓
Target response
  ↓
Content-Security-Policy
```

Search for:

```text
frame-ancestors
```

---

# Example

```http
HTTP/1.1 200 OK
Content-Security-Policy: frame-ancestors 'none';
```

Interpretation:

```text
Target page
    ↓
Cannot be framed
```

---

# Same-Origin Example

```http
Content-Security-Policy: frame-ancestors 'self';
```

Interpretation:

```text
Same-origin framing
        ↓
Allowed
```

```text
Cross-origin framing
        ↓
Not allowed
```

---

# Specific-Origin Example

```http
Content-Security-Policy: frame-ancestors normal-website.com;
```

Interpretation:

```text
normal-website.com
        ↓
Allowed to frame
```

Other origins are not included in the allowed list.

---

# Security Testing Workflow

```text
Identify Sensitive Page
        ↓
Capture Response
        ↓
Inspect CSP
        ↓
Locate frame-ancestors
        ↓
Identify Allowed Origins
        ↓
Determine Whether Attacker Origin Is Allowed
        ↓
Test Actual Framing
```

---

# Comparison With X-Frame-Options

`X-Frame-Options` provides basic framing controls:

```http
X-Frame-Options: DENY
```

```http
X-Frame-Options: SAMEORIGIN
```

CSP provides the more flexible:

```text
frame-ancestors
```

mechanism.

The supplied material recommends CSP `frame-ancestors` as an important modern framing-control mechanism.

---

# Layered Protection

A site may use both:

```http
X-Frame-Options: DENY
```

and:

```http
Content-Security-Policy: frame-ancestors 'none';
```

This provides layered framing protection.

---

# Testing Checklist

```text
☐ Locate Content-Security-Policy
☐ Locate frame-ancestors
☐ Check for 'none'
☐ Check for 'self'
☐ Identify explicitly allowed origins
☐ Determine whether attacker origin is allowed
☐ Check X-Frame-Options
☐ Test actual iframe behavior
☐ Document the result
```

---

# Defensive Recommendations

If the page should never be framed:

```http
Content-Security-Policy: frame-ancestors 'none';
```

If only same-origin framing is required:

```http
Content-Security-Policy: frame-ancestors 'self';
```

If trusted external framing is required:

```http
Content-Security-Policy: frame-ancestors trusted-origin.example;
```

The policy should be restricted to the minimum set of origins required by the application.

---

# Key Takeaways

- `frame-ancestors` controls which origins can embed a page.
- `'none'` prevents framing.
- `'self'` permits same-origin framing.
- Specific trusted origins can be explicitly allowed.
- `frame-ancestors` is the key CSP directive for clickjacking protection.
- Always inspect it when assessing whether a target page can be framed.
- `X-Frame-Options` can be used alongside CSP for layered protection.