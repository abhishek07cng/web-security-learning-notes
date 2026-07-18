# OAuth Bug Bounty Checklist

## Recon

- [ ] Identify OAuth provider
- [ ] Capture authorization request
- [ ] Record parameters

---

## redirect_uri

- [ ] Exact match
- [ ] Prefix bypass
- [ ] Wildcards
- [ ] Open redirect
- [ ] Directory traversal

---

## state

- [ ] Present
- [ ] Random
- [ ] Session-bound
- [ ] Validated

---

## PKCE

- [ ] Used
- [ ] code_verifier checked
- [ ] code_challenge validated

---

## Tokens

- [ ] Access token leakage
- [ ] Authorization code replay
- [ ] ID Token validation

---

## Callback Pages

- [ ] XSS
- [ ] postMessage()
- [ ] HTML injection
- [ ] Open redirects

---

## Resource Server

- [ ] /userinfo
- [ ] /me
- [ ] Scope enforcement

---

## Reporting

- [ ] Impact
- [ ] Root cause
- [ ] Evidence
- [ ] Mitigation