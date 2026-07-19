# CORS Quick Revision

## Definition

CORS allows servers to relax the Same-Origin Policy using HTTP headers.

---

## Important Headers

Request

- Origin

Response

- ACAO
- ACAC
- ACAH
- ACAM

---

## Dangerous Findings

- Origin Reflection
- Trusted `null`
- Trusted HTTP Origin
- Weak Validation
- XSS on Trusted Origin

---

## Testing

Change:

```http
Origin: https://evil.com
```

Observe:

```http
Access-Control-Allow-Origin
```

---

## High Severity

```
Origin Reflection

+

Credentials

+

Sensitive Data
```

---

## Prevention

- Exact allowlist
- HTTPS only
- No reflection
- No wildcard with credentials
- Audit trusted origins

---

## Remember

> CORS does **not** stop requests—it controls whether browser JavaScript can **read** cross-origin responses.

---

## One-Minute Interview Answer

- SOP blocks cross-origin reads.
- CORS relaxes SOP.
- Browser sends `Origin`.
- Server replies with `Access-Control-Allow-Origin`.
- Browser decides whether JavaScript can access the response.
- Poor origin validation leads to CORS vulnerabilities.