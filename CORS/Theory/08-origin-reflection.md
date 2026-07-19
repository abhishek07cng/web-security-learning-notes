# Origin Reflection

## Overview

Origin Reflection is one of the most common CORS vulnerabilities.

Instead of validating trusted origins, the server simply copies the request's `Origin` header into the `Access-Control-Allow-Origin` response header.

---

# Vulnerable Flow

Request

```http
Origin: https://evil.com
```

↓

Response

```http
Access-Control-Allow-Origin:
https://evil.com
```

The attacker completely controls the trusted origin.

---

# Why Developers Do This

Maintaining an allowlist can be difficult.

Some developers choose the shortcut:

```
Read Origin

↓

Reflect Origin

↓

Done
```

This effectively trusts every website.

---

# Example

Request

```http
GET /accountDetails HTTP/1.1

Origin: https://evil.com
```

Response

```http
HTTP/1.1 200 OK

Access-Control-Allow-Origin:
https://evil.com

Access-Control-Allow-Credentials:
true
```

This allows JavaScript on `evil.com` to read authenticated responses.

---

# Attack Flow

```
Victim Visits Evil Site

↓

JavaScript Sends Request

↓

Browser Includes Cookies

↓

Server Reflects Origin

↓

Browser Accepts Response

↓

Sensitive Data Stolen
```

---

# Detection

Using Burp Repeater:

Original request:

```http
Origin: https://example.com
```

Modify:

```http
Origin: https://evil.com
```

If the response becomes:

```http
Access-Control-Allow-Origin:
https://evil.com
```

the application reflects arbitrary origins.

---

# Real-World Impact

Attackers may steal:

- API Keys
- User Information
- Personal Data
- Account Details

without requiring XSS.

---

# Bug Bounty Checklist

- Change Origin
- Observe ACAO
- Check Credentials
- Identify Sensitive Endpoints
- Verify Response Readability

---

# Key Learnings

Origin reflection is usually a high-severity CORS vulnerability when combined with:

- Credentialed requests
- Sensitive responses
- Authenticated users