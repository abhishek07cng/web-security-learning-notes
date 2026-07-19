# CORS Headers

## Overview

CORS relies on a set of HTTP request and response headers that allow browsers and servers to negotiate whether a cross-origin request should be permitted.

These headers determine:

- Which origins are allowed
- Whether credentials are permitted
- Which HTTP methods can be used
- Which custom headers are accepted

---

# Request Headers

## Origin

Every cross-origin request contains:

```http
Origin: https://example.com
```

This identifies the origin initiating the request.

Example:

```http
GET /api/profile HTTP/1.1
Host: api.example.com
Origin: https://shop.example.com
```

---

# Response Headers

## Access-Control-Allow-Origin

Specifies the allowed origin.

Example:

```http
Access-Control-Allow-Origin: https://shop.example.com
```

Or

```http
Access-Control-Allow-Origin: *
```

---

## Access-Control-Allow-Credentials

Allows browsers to include credentials such as:

- Cookies
- Authorization headers
- TLS client certificates

Example:

```http
Access-Control-Allow-Credentials: true
```

---

## Access-Control-Allow-Methods

Defines the allowed HTTP methods.

Example:

```http
Access-Control-Allow-Methods:
GET, POST, PUT, DELETE
```

---

## Access-Control-Allow-Headers

Defines which request headers may be sent.

Example:

```http
Access-Control-Allow-Headers:
Authorization, Content-Type
```

---

## Access-Control-Expose-Headers

Allows JavaScript to read non-standard response headers.

Example:

```http
Access-Control-Expose-Headers:
X-API-Key
```

---

## Access-Control-Max-Age

Specifies how long preflight responses may be cached.

Example:

```http
Access-Control-Max-Age: 3600
```

---

# Typical Exchange

Request

```http
Origin: https://shop.example.com
```

↓

Response

```http
Access-Control-Allow-Origin:
https://shop.example.com

Access-Control-Allow-Credentials:
true
```

↓

Browser

↓

JavaScript Can Read Response

---

# Bug Bounty Perspective

Always inspect:

- Origin
- ACAO
- ACAC
- ACAM
- ACAH

Look for:

- Reflection
- Wildcards
- Misconfigured credentials
- Overly permissive methods

---

# Key Learnings

CORS security depends almost entirely on the correct configuration of these headers. Misconfigured response headers frequently lead to sensitive data exposure.