# Authorization Code Flow Checklist

## Authorization Request

Check:

```
client_id
redirect_uri
response_type=code
scope
state
```

---

## Callback

Expected

```
GET /callback?code=...
```

Questions

- Can code be replayed?
- Can callback be changed?
- Can code be stolen?

---

## Token Exchange

Inspect:

```
POST /token
```

Should include

```
grant_type=authorization_code
client_id
code
redirect_uri
```

---

## Security Checks

- Exact redirect_uri match
- Single-use authorization code
- Short expiration
- PKCE verification