# Location-Based Access Control

## Overview

Some applications restrict access based on:

```text
Country
IP Address
Network Location
```

---

# Example

Admin Panel:

```text
Only Accessible
From Internal Network
```

---

# Intended Logic

```text
Internal IP
        ↓
Allow
```

---

```text
External IP
        ↓
Block
```

---

# Common Implementations

## IP Allowlisting

```text
10.0.0.0/8
```

---

## Corporate Networks

```text
VPN Required
```

---

## Country Restrictions

```text
Specific Regions Only
```

---

# Common Weaknesses

## Trusting Headers

Example:

```http
X-Forwarded-For
```

---

Attacker:

```http
X-Forwarded-For: 127.0.0.1
```

---

May bypass restrictions.

---

# Testing Methodology

## Try

```http
X-Forwarded-For: 127.0.0.1
```

---

## Try

```http
X-Forwarded-For: localhost
```

---

## Try

```http
X-Client-IP
```

---

## Try

```http
X-Real-IP
```

---

# Bug Bounty Mental Model

Whenever:

```text
IP Restriction Exists
```

ask:

```text
Can Headers Influence
Location Decisions?
```

---

# Key Takeaways

- Network location should be verified carefully.
- Never trust user-controlled IP headers.
- Reverse proxies frequently introduce bypasses.