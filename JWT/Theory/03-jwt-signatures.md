# JWT Signatures

## Overview

JWT signatures ensure that the token has not been modified.

Without a valid signature, claims cannot be trusted.

---

# Signature Generation

The server signs:

```text
Header
+
Payload
```

using:

```text
Secret Key
```

or

```text
Private Key
```

depending on the algorithm.

---

# Symmetric Algorithms

Examples:

```text
HS256
HS384
HS512
```

Characteristics:

```text
One Secret Key
Sign
Verify
```

---

# Asymmetric Algorithms

Examples:

```text
RS256
ES256
```

Characteristics:

```text
Private Key → Sign

Public Key → Verify
```

---

# Why Signatures Matter

If signature verification fails:

```text
Reject Token
```

If verification is skipped:

```text
Arbitrary Claims Accepted
```

---

# Key Takeaways

JWT security depends on robust signature verification.