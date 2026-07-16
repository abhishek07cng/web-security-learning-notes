# JWT Attacks Overview

## Overview

JWT attacks exploit weaknesses in how applications process and verify JSON Web Tokens.

---

# Common Goals

```text
Authentication Bypass
Privilege Escalation
Account Takeover
Administrator Access
```

---

# Common Attack Types

```text
Unverified Signature
alg=none
Weak Secret Keys
JWK Injection
JKU Injection
kid Injection
Algorithm Confusion
```

---

# Root Cause

Most vulnerabilities arise because developers:

```text
Trust User-Controlled Headers
Skip Signature Verification
Use Weak Secrets
Misconfigure JWT Libraries
```

---

# Attack Flow

```text
Obtain JWT
        ↓
Modify Claims
        ↓
Exploit Verification Flaw
        ↓
Access Protected Resources
```

---

# Typical Target Claims

```text
sub
role
isAdmin
username
```

---

# Key Takeaways

JWT attacks usually target signature verification rather than token encoding.