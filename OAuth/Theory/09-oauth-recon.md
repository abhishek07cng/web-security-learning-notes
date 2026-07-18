# OAuth Recon Methodology

## Objective

Before attempting exploitation, map the complete OAuth implementation.

Understanding the flow is often more valuable than immediately testing payloads.

---

# Step 1 — Identify the Login Flow

Observe:

```text
Login with Google

Login with GitHub

Continue with Microsoft
```

Capture all requests in Burp Suite.

---

# Step 2 — Identify Endpoints

Locate:

```text
Authorization Endpoint

Token Endpoint

Callback Endpoint

UserInfo Endpoint
```

---

# Step 3 — Determine the Grant Type

Look at:

```text
response_type
```

Possible values:

```text
code

token
```

This determines whether the application uses:

```text
Authorization Code Flow

Implicit Flow
```

---

# Step 4 — Review Parameters

Inspect:

```text
client_id

redirect_uri

scope

state

nonce
```

Questions:

```text
Can Any Parameter Be Modified?

Is Validation Performed?
```

---

# Step 5 — Inspect Redirect Behavior

Observe:

```text
Initial Redirect

OAuth Redirect

Callback Redirect
```

Check whether any redirection can be manipulated.

---

# Step 6 — Analyze UserInfo Requests

Identify:

```http
GET /userinfo

GET /me
```

Determine:

```text
What User Data Is Returned?

How Does The Client Authenticate Users?
```

---

# Step 7 — Enumerate OAuth Configuration

Request:

```text
/.well-known/oauth-authorization-server

/.well-known/openid-configuration
```

Review:

```text
Supported Grant Types

Supported Scopes

JWKS URI

Issuer

Authorization Endpoint

Token Endpoint
```

---

# OAuth Recon Checklist

- [ ] Authorization endpoint identified
- [ ] Callback endpoint identified
- [ ] Grant type identified
- [ ] State parameter reviewed
- [ ] Redirect URI tested
- [ ] Scope analyzed
- [ ] UserInfo endpoint identified
- [ ] Well-known configuration reviewed

---

# Personal Workflow

```text
Identify Login

↓

Capture Requests

↓

Map Endpoints

↓

Understand Flow

↓

Review Parameters

↓

Test Validation

↓

Assess Attack Surface
```

---

# Key Learnings

Effective OAuth testing begins with thorough reconnaissance. Mapping endpoints, parameters, grant types, and validation behavior significantly increases the likelihood of discovering implementation flaws.