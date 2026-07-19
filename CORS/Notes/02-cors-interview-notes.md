# CORS Interview Notes

## What is CORS?

Cross-Origin Resource Sharing (CORS) is a browser security mechanism that allows servers to explicitly permit cross-origin access to resources.

---

## What is an Origin?

An origin consists of:

- Protocol
- Host
- Port

All three must match for two URLs to have the same origin.

---

## What is the Same-Origin Policy?

The Same-Origin Policy (SOP) prevents JavaScript from reading responses from different origins.

CORS provides a controlled mechanism to relax this restriction.

---

## Important CORS Headers

### Request

- Origin

### Response

- Access-Control-Allow-Origin
- Access-Control-Allow-Credentials
- Access-Control-Allow-Headers
- Access-Control-Allow-Methods
- Access-Control-Max-Age

---

## Common CORS Vulnerabilities

- Origin Reflection
- Wildcard ACAO
- Trusted `null`
- Weak Origin Validation
- Trusted HTTP Origins
- XSS on Trusted Origins

---

## Why is `Access-Control-Allow-Credentials: true` Dangerous?

When combined with weak origin validation, it allows attacker-controlled websites to read authenticated responses.

---

## What is Origin Reflection?

The server copies the supplied `Origin` value into the `Access-Control-Allow-Origin` response header without proper validation.

---

## What is the `null` Origin?

A browser-generated origin that can occur with sandboxed iframes, `file://` URLs, and `data:` URLs.

Trusting it is unsafe.

---

## Best Practices

- Exact origin matching
- HTTPS only
- No origin reflection
- No wildcard with credentials
- Audit trusted origins
- Minimize exposed data

---

## Interview Tip

When asked about CORS:

Explain:

1. Same-Origin Policy
2. Browser enforcement
3. Origin header
4. ACAO
5. Credentials
6. Common misconfigurations
7. Mitigation