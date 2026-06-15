# Content Security Policy (CSP)

## Overview

Content Security Policy (CSP) is a browser security mechanism designed to reduce the impact of:

```text
Cross-Site Scripting
Clickjacking
Data Injection Attacks
```

---

# How CSP Works

Server sends:

```http
Content-Security-Policy
```

response header.

---

Example:

```http
Content-Security-Policy:
script-src 'self'
```

---

Meaning:

```text
Only Scripts From Same Origin Allowed
```

---

# Common Directives

## script-src

Controls:

```text
JavaScript Sources
```

---

## img-src

Controls:

```text
Image Sources
```

---

## frame-src

Controls:

```text
Frames
```

---

## frame-ancestors

Controls:

```text
Who Can Embed The Page
```

---

## object-src

Controls:

```text
Plugins
```

---

# Strong CSP Example

```http
default-src 'self';
script-src 'self';
object-src 'none';
frame-src 'none';
base-uri 'none';
```

---

# Benefits

```text
Reduces XSS Impact
Blocks External Scripts
Protects Against Some Data Theft
```

---

# Limitations

```text
Misconfiguration
Whitelisted Third Parties
Policy Injection
```

can weaken CSP.

---

# Related Labs

- Lab29
- Lab30

---

# Key Takeaways

- CSP is a mitigation, not a replacement for secure coding.
- Poorly configured CSP can be bypassed.