# JWT Bug Bounty Checklist

## JWT Discovery

- [ ] Cookie
- [ ] Authorization Header
- [ ] Local Storage
- [ ] Session Storage

---

## Header Review

- [ ] alg
- [ ] kid
- [ ] jwk
- [ ] jku

---

## Payload Review

- [ ] sub
- [ ] role
- [ ] isAdmin
- [ ] permissions

---

## Signature Verification

- [ ] Verified
- [ ] Rejects Invalid Tokens
- [ ] Rejects Unsigned Tokens

---

## Algorithm

- [ ] HS256
- [ ] RS256
- [ ] ES256

---

## Key Management

- [ ] Trusted Keys
- [ ] Remote Keys
- [ ] Embedded Keys
- [ ] Weak Secrets

---

## Impact

- [ ] Authentication Bypass
- [ ] JWT Forgery
- [ ] Privilege Escalation
- [ ] Account Takeover