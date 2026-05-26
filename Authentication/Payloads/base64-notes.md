# Base64 Notes

## Overview

Base64 is an encoding scheme used to represent binary data in ASCII text format.

It is commonly used in:

- HTTP Authentication
- Cookies
- JWTs
- API communication
- Email encoding

---

# Important Concept

```text
Base64 IS NOT encryption
```

It only encodes data.

Anyone can easily decode Base64 values.

---

# Example

## Plaintext

```text
carlos:password123
```

---

## Base64 Encoded

```text
Y2FybG9zOnBhc3N3b3JkMTIz
```

---

# Common Authentication Usage

Base64 is commonly used in:

## HTTP Basic Authentication

```http
Authorization: Basic Y2FybG9zOnBhc3N3b3JkMTIz
```

---

# Common Security Mistake

Developers sometimes incorrectly assume:

```text
Base64 = Security
```

This is FALSE.

---

# Common Attack Scenarios

| Scenario | Risk |
|---|---|
| Base64 Cookies | Information disclosure |
| Basic Auth | Credential exposure |
| JWT Analysis | Token inspection |
| Weak Token Storage | Easy decoding |

---

# Common Testing Workflow

```text
Capture Request
        ↓
Identify Encoded Value
        ↓
Decode Base64
        ↓
Analyze Sensitive Data
```

---

# Common Base64 Indicators

Base64 strings commonly:

- end with `=`
- contain letters/numbers
- contain `/` and `+`

Example:

```text
YWRtaW46cGFzc3dvcmQ=
```

---

# Common Tools

| Tool | Purpose |
|---|---|
| CyberChef | Encode/Decode |
| Burp Decoder | Decode values |
| Base64 CLI Tools | Quick decoding |

---

# Burp Decoder Workflow

```text
Copy Encoded Value
        ↓
Send to Decoder
        ↓
Decode as Base64
        ↓
Analyze Result
```

---

# Real-World Risks

Weak Base64 usage may expose:

- credentials
- tokens
- usernames
- hashes
- session identifiers

---

# Secure Practices

Applications should:

- never rely on Base64 for security
- use encryption where needed
- secure authentication properly
- protect sensitive tokens

---

# Key Takeaways

- Base64 is only encoding.
- Encoded data is easily reversible.
- Sensitive data should never rely on Base64 for protection.

> [!WARNING]
> Base64 encoding provides ZERO security.

> [!IMPORTANT]
> Always inspect Base64 values during authentication testing.