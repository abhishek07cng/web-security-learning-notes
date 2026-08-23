# X-Frame-Options Payloads

## Purpose

Quick reference for testing and documenting `X-Frame-Options` clickjacking protection.

---

# DENY

```http
X-Frame-Options: DENY
```

## Meaning

The target page should not be rendered inside a frame.

```text
Attacker Page
      ↓
iframe
      ↓
Target Page
      X
```

---

# SAMEORIGIN

```http
X-Frame-Options: SAMEORIGIN
```

## Meaning

The page can be framed only when the framing context satisfies the same-origin restriction.

```text
Same Origin
     ↓
Allowed

Different Origin
     ↓
Blocked
```

---

# ALLOW-FROM

```http
X-Frame-Options: ALLOW-FROM https://normal-website.com
```

## Meaning

This value was intended to allow framing from a specified origin.

Browser support for `ALLOW-FROM` is inconsistent.

---

# Header Inspection

Use Burp Suite:

```text
Proxy
  ↓
HTTP History
  ↓
Select Target Response
  ↓
Inspect Response Headers
```

Search for:

```text
X-Frame-Options
```

---

# Basic Framing Test

Create a simple iframe in an authorized environment:

```html
<iframe
    src="https://TARGET">
</iframe>
```

Observe whether the target page can actually be rendered.

---

# Testing Flow

```text
Identify Target
      ↓
Capture Response
      ↓
Inspect X-Frame-Options
      ↓
Identify Configured Value
      ↓
Attempt Authorized iframe Test
      ↓
Observe Browser Behavior
      ↓
Document Result
```

---

# Testing Record

```text
Target:
____________________________

X-Frame-Options:
____________________________

Expected Behavior:
____________________________

Observed Behavior:
____________________________

Frameable:
YES / NO
```

---

# Comparison

| Value | Intended Behavior |
|---|---|
| `DENY` | Prevent framing |
| `SAMEORIGIN` | Allow same-origin framing |
| `ALLOW-FROM` | Allow specified origin; browser support is inconsistent |

---

# Relationship With CSP

Also inspect:

```http
Content-Security-Policy
```

especially:

```text
frame-ancestors
```

For example:

```http
Content-Security-Policy: frame-ancestors 'none';
```

or:

```http
Content-Security-Policy: frame-ancestors 'self';
```

---

# Security Review Checklist

```text
☐ X-Frame-Options present
☐ Value identified
☐ CSP present
☐ frame-ancestors identified
☐ Actual iframe behavior tested
☐ Browser behavior documented
☐ Sensitive pages reviewed
```

---

# Key Learning

`X-Frame-Options` is a framing-control mechanism that can prevent the iframe required for basic clickjacking.

The main values to remember are:

```http
X-Frame-Options: DENY
```

```http
X-Frame-Options: SAMEORIGIN
```

and the historically supported but inconsistently implemented:

```http
X-Frame-Options: ALLOW-FROM ...
```