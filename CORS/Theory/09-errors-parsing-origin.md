# Errors Parsing Origin Headers

## Overview

Some applications attempt to implement an allowlist of trusted origins.

Instead of performing exact comparisons, they use:

- Prefix matching
- Suffix matching
- Regular expressions

Implementation mistakes can allow attacker-controlled domains.

---

# Prefix Matching

Allowed

```
https://trusted.com
```

Validation

```
StartsWith("https://trusted.com")
```

Attacker

```
https://trusted.com.evil.com
```

The server incorrectly considers it trusted.

---

# Suffix Matching

Allowed

```
trusted.com
```

Validation

```
EndsWith("trusted.com")
```

Attacker registers

```
eviltrusted.com
```

or

```
hackerstrusted.com
```

The server mistakenly trusts the malicious domain.

---

# Username Injection

Example

```
https://trusted.com@evil.com
```

The browser connects to:

```
evil.com
```

Poor validation may incorrectly treat it as:

```
trusted.com
```

---

# Regex Mistakes

Example

```
.*trusted.com
```

Matches:

```
eviltrusted.com
```

A safer approach is exact origin matching rather than permissive regular expressions.

---

# Attack Flow

```
Attacker Registers Similar Domain

↓

Origin Header

↓

Weak Validation

↓

Origin Accepted

↓

Sensitive Data Exposed
```

---

# Testing Checklist

Try:

```
https://trusted.com.evil.com
```

```
https://trusted.com@evil.com
```

```
https://eviltrusted.com
```

```
https://trusted-com.evil.org
```

Observe:

```http
Access-Control-Allow-Origin
```

If reflected, the validation logic may be flawed.

---

# Bug Bounty Perspective

Always test:

- Prefix bypass
- Suffix bypass
- Username (`@`) tricks
- Similar domain names
- Regex edge cases

Many real-world CORS vulnerabilities result from incorrect origin parsing rather than outright reflection.

---

# Mitigation

- Use exact string comparison for trusted origins.
- Avoid prefix, suffix, or regex-based matching unless implemented very carefully.
- Maintain a strict allowlist of approved origins.

---

# Key Learnings

Weak origin parsing can unintentionally trust attacker-controlled domains, allowing cross-origin access to sensitive authenticated resources.