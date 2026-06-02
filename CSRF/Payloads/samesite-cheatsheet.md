# SameSite Cheatsheet

## Purpose

Quick Revision Notes

Used for fast recall during:
- PortSwigger Labs
- Bug Bounty Testing
- Interviews
- Web Security Assessments

---

# What Is SameSite?

Browser security mechanism that controls:

```text
When Cookies Are Sent
```

during cross-site requests.

---

# Why SameSite Exists

Protects against:

- CSRF
- XS-Leaks
- Some CORS attacks

---

# SameSite Levels

## Strict

```text
Cross-Site Request
        ↓
Cookie Blocked
```

Most secure.

---

## Lax

Cookie sent only if:

```text
GET Request
+
Top-Level Navigation
```

---

## None

```text
Cookie Always Sent
```

Requires:

```http
Secure
```

---

# Chrome Default

```text
No SameSite Attribute
        ↓
SameSite=Lax
```

---

# Site vs Origin

## Origin

```text
Scheme + Host + Port
```

---

## Site

```text
Scheme + eTLD+1
```

---

# Memory Trick

```text
Origin = Exact Address

Site = Domain Family
```

---

# Common Bypasses

## Lax Bypass

```text
GET Navigation
+
Method Override
```

Lab07

---

## Strict Bypass

```text
Client-Side Redirect
```

Lab08

---

# Common Testing Questions

- Is SameSite explicitly set?
- Which level is used?
- Does endpoint accept GET?
- Is method override supported?
- Are client-side redirects present?

---

# Related Labs

- Lab07
- Lab08

---

# Key Takeaway

SameSite reduces CSRF risk but does not eliminate it.