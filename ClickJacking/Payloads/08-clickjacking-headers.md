# Clickjacking Security Headers

## Purpose

Quick reference for the HTTP response headers and CSP directives used to control whether a page can be embedded in a frame.

These headers are primarily useful when testing whether a target page is frameable and when documenting clickjacking defenses.

---

# X-Frame-Options

## Prevent Framing

```http
X-Frame-Options: DENY
```

Meaning:

```text
Page
 ↓
Cannot be framed
```

---

## Same-Origin Framing

```http
X-Frame-Options: SAMEORIGIN
```

Meaning:

```text
Same Origin
    ↓
Allowed

Other Origin
    ↓
Restricted
```

---

## ALLOW-FROM

The material also discusses:

```http
X-Frame-Options: ALLOW-FROM https://normal-website.com
```

This was intended to permit framing from a specified origin.

Browser support for `ALLOW-FROM` is inconsistent.

---

# Content Security Policy

## Prevent All Framing

```http
Content-Security-Policy: frame-ancestors 'none';
```

Meaning:

```text
No framing origins
        ↓
Page cannot be embedded
```

---

## Same-Origin Framing

```http
Content-Security-Policy: frame-ancestors 'self';
```

Meaning:

```text
Same Origin
    ↓
Allowed
```

---

## Specific Trusted Origin

```http
Content-Security-Policy: frame-ancestors normal-website.com;
```

This allows the specified origin to frame the page.

---

# Combined Protection

A site can use both mechanisms:

```http
X-Frame-Options: DENY
Content-Security-Policy: frame-ancestors 'none';
```

This provides layered framing protection.

---

# Header Inspection

In Burp Suite:

```text
Proxy
  ↓
HTTP history
  ↓
Select response
  ↓
Inspect response headers
```

Search for:

```text
X-Frame-Options
Content-Security-Policy
frame-ancestors
```

---

# Quick Reference

| Header / Directive | Purpose |
|---|---|
| `X-Frame-Options: DENY` | Prevent framing |
| `X-Frame-Options: SAMEORIGIN` | Restrict framing to same origin |
| `X-Frame-Options: ALLOW-FROM` | Specify an allowed framing origin; browser support is inconsistent |
| `frame-ancestors 'none'` | Prevent framing through CSP |
| `frame-ancestors 'self'` | Allow same-origin framing |
| `frame-ancestors example.com` | Allow specified origin |

---

# Testing Flow

```text
Capture Target Response
        ↓
Check X-Frame-Options
        ↓
Check Content-Security-Policy
        ↓
Locate frame-ancestors
        ↓
Determine Allowed Framing
        ↓
Test Actual iframe Behavior
        ↓
Document Result
```

---

# Clickjacking Assessment

A useful assessment should record:

```text
X-Frame-Options:
________________________

Content-Security-Policy:
________________________

frame-ancestors:
________________________

Frameable:
YES / NO

Observed Behavior:
________________________
```

---

# Key Learning

The important framing controls are:

```text
X-Frame-Options
        +
CSP frame-ancestors
```

When assessing clickjacking, inspect both the configured policy and the actual browser framing behavior.