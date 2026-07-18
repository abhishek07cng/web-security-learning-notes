# Lab 02 - Authentication Bypass via OAuth Implicit Flow

## Lab Information

**Difficulty:** Apprentice

---

# Objective

Authenticate as Carlos without knowing his credentials.

---

# Vulnerability

Improper validation of the OAuth implicit flow.

The application trusts:

```
Email

Access Token
```

without checking whether they belong together.

---

# Root Cause

```
Client

↓

POST /authenticate

↓

Server

↓

Trusts Email
```

instead of querying:

```
OAuth Provider

↓

/userinfo
```

---

# Exploitation Steps

## Step 1

Login using OAuth.

Credentials:

```
wiener

peter
```

---

## Step 2

Capture

```
POST /authenticate
```

---

## Step 3

Send to Repeater.

---

## Step 4

Replace

```
email=
```

with

```
carlos@carlos-montoya.net
```

---

## Step 5

Forward request.

---

## Step 6

Open request in browser.

You are now Carlos.

---

# Attack Diagram

```
OAuth Login

↓

Access Token

↓

POST /authenticate

↓

Modify Email

↓

Carlos
```

---

# Impact

```
Authentication Bypass

↓

Account Takeover
```

---

# Burp Workflow

```
Proxy

↓

History

↓

POST /authenticate

↓

Repeater

↓

Modify Email

↓

Request In Browser
```

---

# Detection Tips

Always inspect:

```
POST

/authenticate

/oauth-login

/login
```

Check whether:

```
Identity

↓

Derived From Browser
```

or

```
Derived From OAuth Provider
```

---

# Mitigation

Validate:

```
Access Token

↓

OAuth Provider

↓

UserInfo

↓

Create Session
```

Never trust browser-submitted identities.

---

# Personal Notes

This vulnerability appears whenever applications confuse:

```
Authentication

and

Authorization
```

---

# PortSwigger Skills Learned

- OAuth Login
- Burp Repeater
- Access Token Validation
- Authentication Bypass