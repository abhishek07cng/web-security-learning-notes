# OAuth Bug Bounty Indicators

High-value targets:

- Social Login
- Account Linking
- SSO
- Enterprise Login
- OAuth API Integrations

---

Look for:

- Missing state
- Weak redirect_uri validation
- Open redirects
- Token leakage
- Authorization code leakage
- Weak scope validation
- Missing PKCE
- Insecure postMessage()
- OIDC validation flaws

---

Common Endpoints

```
/authorize
/token
/userinfo
/me
/oauth
/oauth2
/.well-known/openid-configuration
```