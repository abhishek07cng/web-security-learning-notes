# Preventing CORS Vulnerabilities

## Overview

CORS vulnerabilities almost always result from incorrect server configuration rather than flaws in the CORS standard itself.

Following secure implementation practices greatly reduces the risk of exposing sensitive information.

---

# 1. Use a Strict Allowlist

Only trust known origins.

Good

```text
https://app.example.com
https://admin.example.com
```

Avoid:

```
*
```

or

```
Reflect Any Origin
```

---

# 2. Validate Origins Exactly

Compare origins using exact string matching.

Good

```
Origin == https://app.example.com
```

Avoid:

- StartsWith()
- EndsWith()
- Regex shortcuts
- Contains()

These often introduce bypasses.

---

# 3. Never Reflect User Input

Avoid logic such as:

```
Access-Control-Allow-Origin:
<Origin Header>
```

without proper validation.

Reflection is one of the most common CORS vulnerabilities.

---

# 4. Only Enable Credentials When Necessary

If cookies or HTTP authentication are not required:

Do **not** return:

```http
Access-Control-Allow-Credentials: true
```

Only enable credentials for trusted applications.

---

# 5. Never Trust `null`

Reject:

```http
Origin: null
```

unless there is a very specific, well-understood business requirement.

---

# 6. Trust HTTPS Origins Only

Do not whitelist:

```
http://example.com
```

Use:

```
https://example.com
```

Enforce HTTPS with HSTS whenever possible.

---

# 7. Regularly Audit Trusted Domains

Review:

- Legacy applications
- Development environments
- Staging servers
- Third-party services
- Subdomains

Ensure they remain secure and free of vulnerabilities such as XSS.

---

# 8. Protect Trusted Origins Against XSS

A trusted origin with an XSS vulnerability can abuse its CORS permissions.

Security measures include:

- Content Security Policy (CSP)
- Input validation
- Output encoding
- Secure coding practices

---

# 9. Minimize Exposed Data

Even trusted origins should receive only the information they genuinely require.

Apply the principle of least privilege to API responses.

---

# Secure Workflow

```
Browser

↓

Origin Header

↓

Exact Validation

↓

Trusted?

↓

Yes

↓

Return ACAO

↓

No

↓

Reject
```

---

# Bug Bounty Perspective

Common findings include:

- Reflected origins
- Wildcard ACAO
- Trusted `null`
- Weak origin validation
- Trusted HTTP subdomains
- XSS on trusted origins
- Sensitive API exposure

These issues are often high-impact because they allow attackers to access authenticated data.

---

# Best Practices Checklist

- Exact origin matching
- Explicit allowlist
- HTTPS only
- No wildcard with credentials
- No reflected origins
- No `null` origin
- Audit trusted domains regularly
- Minimize exposed data

---

# Key Learnings

Secure CORS is achieved through careful origin validation, least-privilege design, and continuous review of trusted applications. Most CORS vulnerabilities are preventable with straightforward configuration and validation practices.