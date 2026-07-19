# Origin Header

## Overview

The `Origin` request header identifies the origin from which a cross-origin request originates.

Browsers automatically include this header in CORS requests.

Servers use it to determine whether the requesting origin should be trusted.

---

# Structure

```http
Origin: https://example.com
```

The value contains:

```
Protocol

+

Host

+

Port
```

Example:

```
https://shop.example.com
```

---

# Example Request

```http
GET /accountDetails HTTP/1.1
Host: api.example.com
Origin: https://shop.example.com
```

---

# Browser Workflow

```
Browser

↓

Origin Header

↓

Server

↓

Origin Validation

↓

CORS Decision
```

---

# Common Values

HTTPS

```http
Origin: https://example.com
```

HTTP

```http
Origin: http://example.com
```

Localhost

```http
Origin: http://localhost:3000
```

Null

```http
Origin: null
```

---

# Why Origin Matters

Many servers implement logic similar to:

```
If Origin Trusted

↓

Access-Control-Allow-Origin

↓

Origin
```

If this validation is weak, attackers may access sensitive information.

---

# Testing Origin

During CORS testing, modify:

```http
Origin:
https://evil.com
```

Observe whether the response reflects:

```http
Access-Control-Allow-Origin:
https://evil.com
```

If reflected, further investigation is required.

---

# Bug Bounty Perspective

Always test:

```
https://evil.com

https://trusted.com.evil.com

https://trusted.com@evil.com

null
```

Improper validation of the `Origin` header is one of the most common CORS vulnerabilities.

---

# Key Learnings

- Browsers automatically send the `Origin` header.
- Servers decide whether to trust it.
- Weak validation often results in CORS vulnerabilities.