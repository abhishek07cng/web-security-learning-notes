# What is OAuth 2.0?

## Definition

OAuth 2.0 is an authorization framework that allows one application to obtain limited access to a user's resources on another application **without exposing the user's credentials**.

Instead of sharing usernames and passwords, OAuth issues **access tokens** that grant specific permissions.

---

# Why OAuth Exists

Without OAuth:

```text
User
   │
   ▼
Shares Password
   │
   ▼
Third-Party Application
```

Problems:

- Password exposure
- Full account access
- No granular permissions
- Difficult to revoke access

---

With OAuth:

```text
User
   │
   ▼
Authorizes Access
   │
   ▼
OAuth Provider
   │
   ▼
Access Token
   │
   ▼
Client Application
```

The client application never sees the user's password.

---

# Main Components

## Client Application

The application requesting access.

Examples:

```text
Travel Website

Calendar App

Blog Website

GitHub OAuth Login
```

---

## Resource Owner

The user who owns the protected data.

Example:

```text
You
```

---

## OAuth Provider

The authorization server that authenticates users and issues access tokens.

Examples:

```text
Google

GitHub

Microsoft

Facebook

Discord
```

---

## Resource Server

Stores protected resources.

Examples:

```text
User Profile

Email

Contacts

Repositories

Photos
```

---

# OAuth Is Authorization

OAuth answers:

```text
Can This Application
Access This Resource?
```

It does **not** answer:

```text
Who Is This User?
```

Authentication is commonly added using **OpenID Connect (OIDC)**.

---

# Common Use Cases

```text
Log in with Google

Log in with GitHub

Log in with Facebook

Allow Slack to access Google Calendar

Allow GitHub Actions to access repositories
```

---

# Benefits

✔ No password sharing

✔ Limited permissions

✔ Revocable access

✔ Better user privacy

✔ Fine-grained authorization

---

# Personal Understanding

Think of OAuth like a hotel key card.

Instead of giving someone the master key (your password), you issue a temporary card that only opens specific doors.

---

# Bug Bounty Importance

OAuth is one of the highest-value attack surfaces because implementation mistakes can lead to:

```text
Authentication Bypass

Account Takeover

Token Theft

Privilege Escalation

Sensitive Data Disclosure
```

---

# Key Learnings

OAuth is an **authorization framework**, not an authentication protocol. Authentication is typically achieved by combining OAuth with OpenID Connect.