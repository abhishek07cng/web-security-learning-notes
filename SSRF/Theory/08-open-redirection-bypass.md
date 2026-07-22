# Bypassing SSRF Filters via Open Redirection

## Overview

Sometimes an application validates the supplied URL correctly but follows HTTP redirects automatically.

If an allowed domain contains an Open Redirect vulnerability, it can be used to bypass SSRF protections.

---

# What is an Open Redirect?

An Open Redirect allows attackers to control the destination of an HTTP redirect.

Example:

```
https://trusted-site.com/redirect?next=http://evil.com
```

The server responds:

```
302 Found

Location: http://evil.com
```

---

# SSRF Attack Flow

```
Attacker

↓

Allowed URL

↓

Open Redirect

↓

Internal Resource

↓

Sensitive Response
```

The application only validates the first request.

It then follows the redirect to the attacker-controlled destination.

---

# Example

Allowed request:

```
http://trusted-site.com/product
```

Attacker-controlled request:

```
http://trusted-site.com/redirect?next=http://192.168.0.68/admin
```

The validation succeeds because the hostname belongs to the trusted domain.

The backend HTTP client follows the redirect to the internal service.

---

# Why This Works

Validation occurs **before** following the redirect.

The backend HTTP client automatically processes the Location header.

The application never re-validates the redirected URL.

---

# Typical Targets

- Internal Admin Panels
- Private APIs
- Localhost Services
- Internal Monitoring Systems

---

# Testing Methodology

1. Identify SSRF functionality.
2. Find an Open Redirect on an allowed domain.
3. Create a redirect to an internal resource.
4. Supply the redirect URL.
5. Observe whether the backend follows the redirect.

---

# Bug Bounty Perspective

When SSRF appears blocked:

- Search the application for Open Redirects.
- Test whether redirects are followed.
- Verify whether redirected destinations are revalidated.

This combination frequently leads to SSRF bypasses.

---

# Key Learnings

Open Redirect vulnerabilities can bypass SSRF URL validation when the backend follows redirects without validating the final destination.