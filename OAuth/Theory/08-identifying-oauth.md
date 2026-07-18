# Identifying OAuth Authentication

## Overview

Before testing OAuth vulnerabilities, you must first determine whether an application is using OAuth.

Fortunately, OAuth has several easily recognizable indicators.

---

# Visible Indicators

Look for login buttons such as:

```text
Continue with Google

Login with GitHub

Login with Facebook

Sign in with Microsoft

Continue with Discord
```

These are strong indicators that OAuth is being used.

---

# Burp Suite Recon

Proxy the login process and inspect the first authorization request.

Typical request:

```http
GET /authorization?
client_id=...
&redirect_uri=...
&response_type=...
&scope=...
&state=...
```

---

# Important Parameters

## client_id

Unique identifier of the client application.

---

## redirect_uri

Where the OAuth provider returns the user after authorization.

---

## response_type

Determines the grant type.

Examples:

```text
code

token
```

---

## scope

Permissions requested by the client.

---

## state

Used to protect against CSRF attacks.

---

# Common OAuth Endpoints

```text
/authorization

/auth

/token

/userinfo

/me

/oauth/callback
```

Different providers may use different endpoint names.

---

# Recon Checklist

Identify:

```text
Authorization Endpoint

Token Endpoint

Callback Endpoint

UserInfo Endpoint
```

---

# Well-Known Discovery Endpoints

If the authorization server is external, check:

```text
/.well-known/oauth-authorization-server

/.well-known/openid-configuration
```

These often reveal:

- Supported grant types
- Endpoints
- Scopes
- Response modes
- Signing algorithms

---

# Bug Bounty Perspective

During reconnaissance, document:

```text
Grant Type

Redirect URI

Scopes

State Parameter

Supported Features
```

This information guides later testing.

---

# Key Learnings

Most OAuth implementations can be identified by their authorization requests and OAuth-specific parameters such as `client_id`, `redirect_uri`, `response_type`, `scope`, and `state`.