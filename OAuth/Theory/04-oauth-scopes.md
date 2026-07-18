# OAuth Scopes

## Definition

A scope defines **what permissions** a client application is requesting from the user.

Instead of giving full account access, OAuth allows users to grant only specific permissions.

---

# Why Scopes Exist

Without scopes:

```text
Client
    │
    ▼
Full Account Access
```

With scopes:

```text
Client
    │
    ▼
Only Requested Permissions
```

This follows the **Principle of Least Privilege**.

---

# Authorization Request

Example:

```http
GET /authorization?
client_id=12345
&response_type=code
&scope=openid profile email
```

The OAuth provider displays these permissions to the user before consent.

---

# Common OAuth Scopes

Examples vary between providers.

```text
profile

email

contacts

calendar

photos

messages

repository
```

---

# OpenID Connect Scopes

Most authentication systems use standardized scopes.

```text
openid

profile

email

address

phone
```

Example:

```text
scope=openid profile email
```

---

# Example

Application requests:

```text
Read Email

Read Profile
```

User approves.

OAuth Provider issues a token with:

```text
scope:

openid profile email
```

The client **cannot** access resources outside the approved scope.

---

# Scope Principle

```text
Requested Scope

↓

User Approval

↓

Access Token

↓

Resource Server

↓

Allowed Resources Only
```

---

# Bug Bounty Perspective

Always inspect:

```text
scope
```

Questions:

```text
Can The Scope Be Modified?

Can Additional Scopes Be Requested?

Can Existing Tokens Be Upgraded?

Does The Resource Server Validate Scope?
```

---

# Common Issues

```text
Scope Upgrade

Missing Scope Validation

Over-Permissioned Tokens

Ignoring Scope Entirely
```

---

# Key Learnings

Scopes define **what** a token can access. Every API request should verify that the requested action matches the scope originally granted.