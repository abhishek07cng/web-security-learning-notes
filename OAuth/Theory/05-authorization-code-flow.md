# Authorization Code Grant Flow

## Overview

The Authorization Code Flow is the most secure OAuth flow.

It is primarily used by:

```text
Traditional Web Applications

Backend Applications
```

Unlike the Implicit Flow, the access token is **never exposed directly to the browser**.

---

# Flow Overview

```text
User

↓

Client

↓

Authorization Server

↓

Authorization Code

↓

Client Backend

↓

Access Token

↓

Resource Server
```

---

# Step 1 — Authorization Request

The client redirects the user to:

```http
GET /authorization
```

Important parameters:

```text
client_id

redirect_uri

response_type=code

scope

state
```

---

# Step 2 — User Authentication

The OAuth provider authenticates the user.

Examples:

```text
Username

Password

MFA
```

---

# Step 3 — User Consent

The provider displays requested permissions.

Example:

```text
Read Profile

Read Email
```

---

# Step 4 — Authorization Code

After approval:

```text
Authorization Server

↓

redirect_uri

↓

code=xxxxxxxx
```

Example:

```http
GET /callback?code=abc123
```

---

# Step 5 — Code Exchange

The client backend sends:

```http
POST /token
```

Including:

```text
client_id

client_secret

authorization_code

redirect_uri
```

---

# Step 6 — Access Token

OAuth Provider returns:

```json
{
  "access_token":"...",
  "token_type":"Bearer",
  "scope":"openid profile"
}
```

---

# Step 7 — API Request

Client sends:

```http
Authorization: Bearer ACCESS_TOKEN
```

to:

```text
/userinfo
```

---

# Step 8 — User Data Returned

Example:

```json
{
  "username":"carlos",
  "email":"carlos@example.com"
}
```

---

# Advantages

✔ Access token never passes directly through the browser

✔ Backend validates everything

✔ Supports client authentication

✔ Most secure OAuth flow

---

# Bug Bounty Focus

Review:

```text
redirect_uri

authorization_code

client_secret

state

scope
```

---

# Common Vulnerabilities

```text
Authorization Code Leakage

Redirect URI Validation

CSRF

Code Reuse

Scope Upgrade
```

---

# Key Learnings

The Authorization Code Flow separates the authorization code from the access token, significantly reducing token exposure compared to the Implicit Flow.