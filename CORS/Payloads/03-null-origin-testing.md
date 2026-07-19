# Null Origin Testing

## Goal

Determine whether the application incorrectly trusts the special `null` origin.

---

## Request

Replace:

```http
Origin: https://example.com
```

with:

```http
Origin: null
```

---

## Vulnerable Response

```http
Access-Control-Allow-Origin: null

Access-Control-Allow-Credentials: true
```

---

## Verify

If both headers are present:

- Browser allows response
- JavaScript can read authenticated data
- High-impact CORS issue

---

## Exploitation Indicators

- Sandboxed iframes
- `file://`
- `data:`
- Browser-generated null origin

---

## Severity

High when:

- Credentials are enabled
- Sensitive data is returned
- Victim is authenticated