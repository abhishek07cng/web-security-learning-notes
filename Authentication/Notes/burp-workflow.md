# Burp Workflow Notes

## Standard Burp Testing Workflow

```text
Proxy
        ↓
Intercept Request
        ↓
Analyze Request
        ↓
Send to Repeater
        ↓
Modify Parameters
        ↓
Send to Intruder
        ↓
Automate Testing
        ↓
Analyze Responses
```

---

# 1. Proxy

## Purpose

Used for:

- intercepting traffic
- viewing requests
- modifying requests
- analyzing responses

---

# Common Proxy Actions

- intercept login requests
- inspect cookies
- analyze headers
- modify parameters

---

# 2. Repeater

## Purpose

Used for:

- manual testing
- logic testing
- parameter manipulation
- response comparison

---

# Common Repeater Uses

| Use Case | Example |
|---|---|
| Parameter Tampering | Change usernames |
| MFA Testing | Modify tokens |
| Session Testing | Replay cookies |
| IDOR Testing | Change IDs |

---

# 3. Intruder

## Purpose

Used for:

- brute-force attacks
- enumeration
- fuzzing
- payload automation

---

# Common Intruder Attacks

```text
Username Enumeration
Password Brute Force
MFA Brute Force
Token Testing
```

---

# 4. Decoder

## Purpose

Used for:

- Base64 decoding
- URL decoding
- hash analysis
- JWT inspection

---

# Common Decoder Usage

```text
Base64 → Plaintext
URL Encoding → Readable Text
```

---

# 5. Comparer

## Purpose

Compare:

- response differences
- redirects
- authentication behavior
- response lengths

---

# Why Comparer Is Useful

Very useful during:

- username enumeration
- brute-force testing
- access control testing

---

# Common Authentication Workflow

```text
Intercept Login
        ↓
Send to Repeater
        ↓
Analyze Parameters
        ↓
Send to Intruder
        ↓
Automate Enumeration
        ↓
Analyze Responses
```

---

# Common Burp Indicators

| Indicator | Meaning |
|---|---|
| HTTP 302 | Successful login |
| Set-Cookie | Session created |
| Response Length Change | Different behavior |
| Redirect Location | Authenticated access |

---

# Useful Burp Features

| Feature | Purpose |
|---|---|
| Grep Match | Detect success |
| Grep Extract | Extract tokens |
| Resource Pools | Slow attack speed |
| Logger | Observe traffic |

---

# Common Burp Mistakes

| Mistake | Problem |
|---|---|
| Ignoring Cookies | Missed sessions |
| No Response Analysis | Missed vulnerabilities |
| No Sorting by Length | Missed enumeration |
| Only Using Intruder | Weak methodology |

---

# Key Takeaways

- Burp Suite is the core tool for web application testing.
- Response analysis is critical.
- Repeater is extremely important for logic testing.

> [!TIP]
> Most vulnerabilities are discovered through careful response analysis, not random payloads.