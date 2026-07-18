# OAuth Authentication

## Overview

Although OAuth was originally designed for **authorization**, it is now widely used for **authentication** through social login.

Examples:

```text
Continue with Google

Sign in with GitHub

Login with Microsoft

Continue with Discord
```

In this scenario, the client application uses information returned by the OAuth provider to identify the user and create a local authenticated session.

---

# OAuth vs Authentication

OAuth answers:

```text
Can this application access this resource?
```

Authentication answers:

```text
Who is this user?
```

OAuth itself does **not** verify identity. Authentication is typically implemented using OAuth together with **OpenID Connect (OIDC)**.

---

# Authentication Flow

```text
User

↓

Clicks "Login with Google"

↓

OAuth Provider

↓

User Login

↓

User Grants Consent

↓

Access Token

↓

Client Requests User Info

↓

OAuth Provider Returns Profile

↓

Client Creates Session
```

---

# User Information

Most applications request data from:

```text
/ userinfo
```

Typical response:

```json
{
  "username":"carlos",
  "email":"carlos@example.com"
}
```

The application then identifies the user using this information.

---

# Why OAuth Authentication Is Popular

✔ No password storage

✔ Faster registration

✔ Single Sign-On (SSO)

✔ Reduced password reuse

---

# Security Assumption

The client assumes:

```text
The OAuth Provider Correctly Verified The User
```

If this assumption is broken, authentication can fail completely.

---

# Bug Bounty Perspective

Whenever OAuth is used for login, ask:

```text
How Does The Client Identify The User?

Email?

Username?

User ID?

Access Token?
```

---

# Common Risks

```text
Authentication Bypass

Account Takeover

Improper Identity Validation

Trusting User-Controlled Data
```

---

# Key Learnings

OAuth authentication relies on trusted identity information returned by the OAuth provider. Improper validation of this information can lead to complete authentication bypass.