# OAuth Client-Side Vulnerabilities

## Overview

OAuth vulnerabilities can originate from either:

```text
Client Application

↓

OAuth Provider
```

This file focuses on vulnerabilities introduced by the **client application's implementation**.

Even if the OAuth provider (Google, GitHub, Microsoft, etc.) is perfectly secure, mistakes in the client application can still result in complete account takeover.

---

# Why Client Applications Become Vulnerable

OAuth is intentionally flexible.

Developers decide how to:

- Handle callbacks
- Validate responses
- Store tokens
- Create user sessions
- Verify identities

Mistakes in any of these steps introduce vulnerabilities.

---

# Common Client-Side OAuth Vulnerabilities

```text
Improper Implicit Flow Validation

Missing State Validation

Login CSRF

Account Linking CSRF

Improper User Verification

Weak Token Validation
```

---

# Attack Surface

Typical endpoints:

```text
/authorize

/oauth/callback

/authenticate

/oauth-linking

/login/social
```

---

# Common Security Assumptions

Developers often assume:

```text
If OAuth Returned It

↓

It Must Be Trusted
```

This assumption is dangerous.

Every response must still be validated.

---

# High-Risk Parameters

```text
state

code

access_token

redirect_uri

email

username
```

---

# Bug Bounty Questions

Ask:

```text
Does The Client Verify
The Returned User?

↓

Does It Verify
The Access Token?

↓

Does It Validate state?

↓

Does It Trust Browser Data?
```

---

# Typical Impact

```text
Authentication Bypass

Account Takeover

Privilege Escalation

Login CSRF
```

---

# Key Learnings

Many OAuth vulnerabilities originate from the client application's incorrect assumptions about data returned by the OAuth provider.