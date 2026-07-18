# OAuth Quick Revision

## OAuth

Authorization framework.

---

## OIDC

Authentication layer built on OAuth.

---

## Main Flows

- Authorization Code
- Authorization Code + PKCE
- Implicit
- Client Credentials

---

## Important Parameters

- client_id
- redirect_uri
- response_type
- scope
- state
- nonce
- code_challenge

---

## Common Vulnerabilities

- Missing state
- Weak redirect_uri validation
- Token leakage
- Open redirects
- Missing PKCE
- postMessage()
- ID Token validation flaws

---

## Important Endpoints

```
/authorize
/token
/userinfo
/me
/.well-known/openid-configuration
```

---

## Bug Bounty Workflow

1. Identify OAuth.
2. Capture requests.
3. Analyze parameters.
4. Test callback.
5. Look for token leakage.
6. Validate PKCE.
7. Inspect callback pages.
8. Report impact.

---

## Best Practices

- Use Authorization Code Flow + PKCE.
- Validate redirect_uri exactly.
- Validate state and nonce.
- Protect callback pages.
- Never trust browser-supplied identity data.