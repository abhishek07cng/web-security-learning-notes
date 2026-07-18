# OAuth Service Vulnerabilities

## Overview

Not every OAuth issue originates from the client.

Sometimes the OAuth authorization server itself is misconfigured.

These flaws often impact every client application using that provider.

---

# Typical OAuth Service Issues

```text
Weak redirect_uri Validation

Scope Validation Errors

Token Leakage

Authorization Code Leakage

Improper Client Validation

Missing Redirect Verification
```

---

# High-Risk Endpoints

```text
/authorize

/token

/userinfo

/jwks

/openid-configuration
```

---

# Dangerous Misconfigurations

## Weak redirect_uri Validation

Allows attackers to receive:

```text
Authorization Codes

Access Tokens
```

---

## Missing Scope Validation

Server issues tokens with permissions never approved by the user.

---

## Weak Client Validation

Allows one client application to abuse another client's authorization.

---

## Authorization Code Leakage

Occurs when:

```text
redirect_uri

↓

Attacker Controlled
```

---

## Token Leakage

More common in:

```text
Implicit Flow
```

because access tokens travel through the browser.

---

# Bug Bounty Indicators

```text
OAuth Provider

Custom OAuth Server

Self-Hosted Identity Provider

Single Sign-On Platforms
```

---

# Questions To Ask

```text
Can redirect_uri Be Modified?

↓

Can Scopes Be Expanded?

↓

Can Tokens Leak?

↓

Can Codes Leak?
```

---

# Typical Impact

```text
Authentication Bypass

Account Takeover

Sensitive Data Disclosure

Privilege Escalation
```

---

# Key Learnings

OAuth service misconfigurations often affect multiple applications simultaneously, making them especially valuable bug bounty targets.