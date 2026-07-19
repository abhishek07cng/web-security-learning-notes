# CORS Bug Bounty Checklist

## Reflection

- Arbitrary Origin Reflection
- Dynamic ACAO
- Origin copied directly

---

## Validation

- Prefix Matching
- Suffix Matching
- Regex Errors
- Username Injection
- Similar Domains

---

## Credentials

Check:

```http
Access-Control-Allow-Credentials: true
```

---

## Trusted Origins

Review:

- HTTP Origins
- Subdomains
- Development Servers
- Staging Servers
- Legacy Applications

---

## Special Cases

- Origin: null
- Localhost
- IP Addresses
- Internal Applications

---

## Sensitive APIs

- /me
- /account
- /profile
- /api/
- /settings
- /admin

---

## Impact Assessment

Can you access:

- API Keys
- Tokens
- Email
- Address
- Payment Information
- Internal APIs