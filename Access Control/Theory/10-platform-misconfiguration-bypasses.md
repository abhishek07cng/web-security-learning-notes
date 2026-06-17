# Platform Misconfiguration Bypasses

## Overview

Some applications rely on platform-specific headers or middleware for access control.

Misconfigurations can create bypass opportunities.

---

# Example Architecture

```text
Internet
        ↓
Reverse Proxy
        ↓
Application Server
```

---

# Intended Protection

Proxy blocks:

```text
/admin
```

for normal users.

---

# Misconfiguration

Application trusts:

```http
X-Original-URL
```

or

```http
X-Rewrite-URL
```

headers.

---

# Example Request

```http
GET /
```

---

Added Header:

```http
X-Original-URL: /admin
```

---

# Result

Admin functionality accessible.

---

# Other Common Headers

```http
X-Forwarded-For
X-Original-URL
X-Rewrite-URL
X-Host
```

---

# Why It Happens

Different components:

```text
Proxy
Framework
Application
```

interpret requests differently.

---

# Bug Bounty Mental Model

Whenever access is denied:

```text
Try Header-Based Routing Tricks
```

---

# Testing Checklist

## Try

```http
X-Original-URL: /admin
```

---

## Try

```http
X-Rewrite-URL: /admin
```

---

## Try

```http
X-Forwarded-Host
```

---

# Related Labs

```text
Lab05
```

---

# Key Takeaways

- Security controls often fail at component boundaries.
- Reverse proxy misconfigurations are common.
- Header manipulation can bypass authorization.