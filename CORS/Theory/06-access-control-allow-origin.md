# Access-Control-Allow-Origin (ACAO)

## Overview

`Access-Control-Allow-Origin` (ACAO) is the most important CORS response header.

It tells the browser which origin is allowed to access the response.

---

# Example

Response:

```http
HTTP/1.1 200 OK

Access-Control-Allow-Origin:
https://shop.example.com
```

Only JavaScript from:

```
https://shop.example.com
```

may read the response.

---

# Wildcard

Some servers return:

```http
Access-Control-Allow-Origin: *
```

This allows any origin to read the response.

However,

this cannot be combined with:

```http
Access-Control-Allow-Credentials: true
```

Modern browsers reject this combination.

---

# Reflection

Some applications reflect the supplied Origin.

Example

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

If credentials are also allowed, this usually results in a serious CORS vulnerability.

---

# Whitelisting

Secure implementations maintain an allowlist.

Example

```
https://shop.example.com

https://admin.example.com
```

Requests from other origins are rejected.

---

# Browser Decision

```
Origin

↓

Matches ACAO

↓

JavaScript Can Read Response
```

Otherwise

```
Browser Blocks Response
```

---

# Common Misconfigurations

- Reflecting arbitrary origins
- Prefix matching
- Suffix matching
- Regex mistakes
- Trusting `null`
- Allowing insecure HTTP origins

---

# Burp Testing

Modify:

```http
Origin:
https://evil.com
```

Observe:

```http
Access-Control-Allow-Origin:
https://evil.com
```

If reflected, continue testing with:

- Credentials
- Sensitive endpoints
- Authentication

---

# Impact

Misconfigured ACAO may lead to:

- API Key Disclosure
- Personal Data Disclosure
- Account Information Leakage
- Authentication Bypass (in some scenarios)

---

# Key Learnings

`Access-Control-Allow-Origin` is the core CORS security control. Any weakness in its validation can expose authenticated responses to attacker-controlled websites.