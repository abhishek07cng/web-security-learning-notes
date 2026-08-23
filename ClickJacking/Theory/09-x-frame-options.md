# X-Frame-Options

## Overview

`X-Frame-Options` is an HTTP response header used to control whether a page can be displayed inside a frame.

It is an important defense against clickjacking.

---

# Purpose

The header tells the browser whether the response can be loaded in:

```text
<iframe>
<frame>
<object>
```

The main goal is to prevent an attacker-controlled page from embedding a sensitive target page.

---

# Basic Protection

A server can return:

```http
X-Frame-Options: DENY
```

This prevents the page from being framed.

Conceptually:

```text
Attacker Page
      ↓
Attempts iframe
      ↓
Browser checks X-Frame-Options
      ↓
DENY
      ↓
Target cannot be framed
```

---

# SAMEORIGIN

Another commonly used value is:

```http
X-Frame-Options: SAMEORIGIN
```

This allows framing only when the framing page belongs to the same origin.

Conceptually:

```text
Same Origin
     ↓
Allowed
```

```text
Different Origin
     ↓
Blocked
```

---

# ALLOW-FROM

The material also discusses:

```http
X-Frame-Options: ALLOW-FROM https://normal-website.com
```

This was intended to allow framing from a specified origin.

However, browser support for `ALLOW-FROM` is inconsistent.

For modern applications, CSP `frame-ancestors` is generally the more flexible mechanism for specifying allowed framing origins.

---

# Checking X-Frame-Options

In Burp Suite:

```text
Proxy
  ↓
HTTP history
  ↓
Select target response
  ↓
Inspect response headers
```

Look for:

```http
X-Frame-Options:
```

Possible values include:

```text
DENY
SAMEORIGIN
ALLOW-FROM
```

---

# Clickjacking Testing

Before attempting to construct a clickjacking PoC:

```text
Check X-Frame-Options
        ↓
Determine whether framing is permitted
```

If:

```http
X-Frame-Options: DENY
```

is present, the browser should prevent the page from being framed.

---

# Example Response

```http
HTTP/1.1 200 OK
Content-Type: text/html
X-Frame-Options: DENY
```

This indicates that the page should not be rendered inside a frame.

---

# SAMEORIGIN Example

```http
HTTP/1.1 200 OK
Content-Type: text/html
X-Frame-Options: SAMEORIGIN
```

The browser permits framing only when the framing context satisfies the same-origin restriction.

---

# Header and Iframe

Attacker page:

```html
<iframe src="https://victim-website.com/my-account"></iframe>
```

Target response:

```http
X-Frame-Options: DENY
```

Result:

```text
Iframe Attempt
      ↓
Browser Checks Header
      ↓
DENY
      ↓
Framing Prevented
```

---

# Why This Prevents Basic Clickjacking

Basic clickjacking depends on:

```text
Target Page
      ↓
Loaded inside iframe
```

If the browser refuses to load the target page in the iframe:

```text
Target Page
      X
     iframe
```

the attacker cannot place the target controls underneath a decoy.

---

# Limitations

`X-Frame-Options` is useful but has limitations.

The supplied material highlights that:

```text
ALLOW-FROM
```

has inconsistent browser support.

For more flexible framing policies, CSP provides:

```text
frame-ancestors
```

---

# CSP Relationship

A modern application may use:

```http
Content-Security-Policy: frame-ancestors 'none';
```

or:

```http
Content-Security-Policy: frame-ancestors 'self';
```

This provides a more flexible framing policy.

---

# Testing Workflow

```text
Identify Sensitive Page
        ↓
Inspect Response Headers
        ↓
Find X-Frame-Options
        ↓
Determine Policy
        ↓
Check CSP frame-ancestors
        ↓
Attempt Authorized Frame Test
        ↓
Document Result
```

---

# Security Review Checklist

```text
☐ Check X-Frame-Options
☐ Check whether value is DENY
☐ Check whether value is SAMEORIGIN
☐ Check for ALLOW-FROM
☐ Check CSP
☐ Check frame-ancestors
☐ Test actual framing behavior
☐ Document browser behavior
```

---

# Recommended Defensive Patterns

For pages that should never be framed:

```http
X-Frame-Options: DENY
```

For pages that may only be framed by the same origin:

```http
X-Frame-Options: SAMEORIGIN
```

A CSP equivalent can be:

```http
Content-Security-Policy: frame-ancestors 'none';
```

or:

```http
Content-Security-Policy: frame-ancestors 'self';
```

---

# Key Takeaways

- `X-Frame-Options` is a response header used to control framing.
- `DENY` prevents framing.
- `SAMEORIGIN` restricts framing to the same origin.
- `ALLOW-FROM` exists but has inconsistent browser support.
- Check the response headers before testing clickjacking.
- CSP `frame-ancestors` provides more flexible framing control.
- Effective framing protection prevents the iframe required for basic clickjacking.