# Deriving Public Keys From Existing Tokens

## Overview

Algorithm confusion testing may require the server's RSA public key.

Sometimes the public key is not directly exposed.

However, it may be possible to derive candidate public keys from multiple signed JWTs.

---

# Requirements

```text
Two JWTs
        ↓
Signed By Same RSA Key
```

---

# Concept

RSA signatures contain mathematical relationships with the signing key.

Tools can analyze multiple signatures and calculate candidate public key values.

---

# Attack Flow

```text
Obtain Two JWTs
        ↓
Analyze RSA Signatures
        ↓
Calculate Candidate Keys
        ↓
Test Forged Tokens
        ↓
Identify Correct Key
```

---

# Tool Concept

PortSwigger provides a simplified utility:

```text
sig2n
```

It processes multiple JWTs and outputs candidate key material and test tokens.

---

# Identifying The Correct Key

```text
Candidate 1 → Rejected
Candidate 2 → Rejected
Candidate 3 → Accepted
```

The accepted candidate indicates the matching key representation.

---

# Related Lab

```text
Lab08
```

---

# Personal Testing Question

If I see:

```text
RS256
```

I ask:

```text
Is The Public Key Exposed?

If Not:

Can It Be Derived From Multiple Tokens?
```

---

# Key Takeaways

A public key does not always need to be directly exposed for algorithm confusion testing.