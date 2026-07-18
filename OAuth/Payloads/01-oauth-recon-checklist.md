# OAuth Recon Checklist

## 1. Identify OAuth Usage

Look for:

- Login with Google
- Login with GitHub
- Login with Facebook
- Login with Microsoft
- Login with X (Twitter)
- Sign in with Apple
- Connect Account
- Link Social Account

---

## 2. Capture OAuth Requests

Intercept requests containing:

```
/authorize
/auth
/oauth
/oauth2
/connect
/login/oauth
```

---

## 3. Record Parameters

```
client_id
redirect_uri
response_type
scope
state
nonce
code_challenge
code_challenge_method
```

---

## 4. Determine OAuth Flow

Authorization Code Flow

```
response_type=code
```

Implicit Flow

```
response_type=token
```

Hybrid Flow

```
response_type=code token
```

OIDC

```
scope=openid
```

---

## 5. Inspect Callback

Common paths:

```
/oauth/callback
/auth/callback
/login/oauth
/oauth-linking
/connect/callback
```

---

## 6. Inspect Resource Server

Look for:

```
/userinfo
/me
/profile
/api/user
```

---

## 7. Burp Checklist

- Proxy
- Repeater
- Comparer
- Logger
- Decoder

---

## 8. Questions

- Is state present?
- Is PKCE used?
- Is redirect_uri validated?
- Can callback be manipulated?
- Can tokens leak?