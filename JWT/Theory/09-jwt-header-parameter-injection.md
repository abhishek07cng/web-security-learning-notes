# JWT Header Parameter Injection

## Overview

JWT headers contain metadata used during verification.

If applications trust attacker-controlled header parameters, they may become vulnerable.

---

# Common Header Parameters

```text
alg
kid
jwk
jku
typ
```

---

# Why Dangerous?

Applications may use these values to decide:

```text
Which Key To Use
Where To Download Keys
How To Verify Tokens
```

Since headers are attacker-controlled, trusting them is risky.

---

# Attack Flow

```text
Modify Header
        ↓
Server Trusts Header
        ↓
Verification Manipulated
        ↓
Authentication Bypass
```

---

# Related Attacks

```text
JWK Injection
JKU Injection
kid Injection
Algorithm Confusion
```

---

# Related Labs

```text
Lab04
Lab05
Lab06
Lab07
```

---

# Key Takeaways

JWT headers should be treated as untrusted input.