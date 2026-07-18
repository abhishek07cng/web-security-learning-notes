# How OAuth Works

OAuth enables applications to access resources on behalf of a user using access tokens instead of passwords.

---

# Three Main Parties

```text
Resource Owner (User)

↓

Client Application

↓

OAuth Provider
```

---

# High-Level Flow

```text
User

↓

Client Requests Access

↓

OAuth Provider

↓

User Authenticates

↓

User Grants Permission

↓

OAuth Provider Issues Token

↓

Client Uses Token

↓

Resource Server Returns Data
```

---

# Step 1 — Client Requests Authorization

The client redirects the user to the OAuth provider.

Example:

```text
Log in with Google
```

---

# Step 2 — User Authenticates

The OAuth provider verifies:

```text
Username

Password

MFA
```

---

# Step 3 — User Grants Consent

The user approves requested permissions.

Example:

```text
Read Email

Read Profile

Read Contacts
```

---

# Step 4 — Authorization Granted

Depending on the grant type, the provider issues:

```text
Authorization Code

or

Access Token
```

---

# Step 5 — Access Token Obtained

The client receives an access token.

Example:

```text
Bearer eyJhb...
```

---

# Step 6 — Resource Request

The client sends:

```http
Authorization: Bearer ACCESS_TOKEN
```

to the resource server.

---

# Step 7 — Resource Returned

If the token is valid, the resource server returns:

```text
User Profile

Email

Avatar

Repositories
```

---

# OAuth Flow Diagram

```text
User
 │
 ▼
Client
 │
 ▼
Authorization Server
 │
 ▼
User Login
 │
 ▼
Consent
 │
 ▼
Access Token
 │
 ▼
Resource Server
```

---

# Why Tokens?

Tokens are:

- Temporary
- Revocable
- Scoped
- Limited

Unlike passwords, they can expire and be restricted.

---

# Bug Bounty Perspective

Always identify:

```text
Where Is The Token Generated?

Where Is It Sent?

Where Is It Stored?

How Is It Validated?
```

---

# Key Learnings

OAuth replaces password sharing with temporary access tokens that grant limited access to protected resources.