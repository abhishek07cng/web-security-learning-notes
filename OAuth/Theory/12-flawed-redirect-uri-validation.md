# Flawed redirect_uri Validation

## Overview

One of the most dangerous OAuth vulnerabilities involves improper validation of the:

```text
redirect_uri
```

parameter.

If validation is weak, attackers may receive:

```text
Authorization Codes

Access Tokens
```

instead of the legitimate client.

---

# Why redirect_uri Matters

OAuth sends users back to:

```text
redirect_uri
```

after successful authorization.

Example:

```text
/oauth/callback
```

This location receives:

```text
Authorization Code

or

Access Token
```

---

# Secure Validation

Correct implementation:

```text
Exact Match

↓

Whitelisted URI

↓

Authorization Continues
```

---

# Weak Validation

Examples include:

```text
StartsWith()

EndsWith()

Substring Checks

Regex Mistakes

Wildcard Matching
```

These approaches can often be bypassed.

---

# Common Bypass Techniques

## Extra Paths

```text
/oauth/callback/anything
```

---

## Directory Traversal

```text
/oauth/callback/../post
```

---

## Duplicate Parameters

```text
redirect_uri=A

redirect_uri=B
```

---

## Localhost Abuse

```text
localhost.evil.com
```

---

## URL Parsing Tricks

```text
https://trusted.com@evil.com
```

or

```text
https://trusted.com#evil.com
```

Different components may interpret these URLs differently if validation is implemented incorrectly.

---

# Why Attackers Care

Successful bypasses may expose:

```text
Authorization Code

↓

Access Token

↓

Authenticated Session
```

---

# Bug Bounty Checklist

- Does the provider require an exact redirect URI match?
- Can paths be extended?
- Can directory traversal change the callback?
- Are duplicate `redirect_uri` parameters handled safely?
- Can fragments or query parameters alter the destination?
- Does the provider treat `localhost` specially?

---

# Typical Impact

```text
Authorization Code Theft

Access Token Theft

Authentication Bypass

Account Takeover
```

---

# Key Learnings

The `redirect_uri` parameter is one of the highest-value OAuth inputs. Validation should use strict allowlists and exact matching rather than flexible pattern checks.