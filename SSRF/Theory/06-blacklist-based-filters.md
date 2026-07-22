# SSRF with Blacklist-Based Input Filters

## Overview

Many applications attempt to prevent SSRF by blocking known dangerous values such as:

- `127.0.0.1`
- `localhost`
- `/admin`

These blacklist-based defenses are often incomplete and can usually be bypassed.

---

# How Blacklists Work

Example validation:

```
If URL contains:

127.0.0.1

↓

Reject Request
```

Although this blocks obvious payloads, attackers can often represent the same destination in alternative ways.

---

# Common Bypass Techniques

## Alternative IP Representations

Instead of:

```text
127.0.0.1
```

Use:

```text
127.1

2130706433

017700000001
```

These values resolve to the loopback address but may bypass simple string comparisons.

---

## Domain Name Resolution

Register or use a domain that resolves to `127.0.0.1`.

The application validates the hostname rather than its resolved IP address.

---

## URL Encoding

Encode blocked characters.

Example:

```text
/admin
```

↓

```text
/%2561dmin
```

If the server performs multiple decoding passes, the blocked path may still be reached.

---

## Redirect-Based Bypass

Supply an allowed URL that performs an HTTP redirect to the forbidden destination.

Example:

```
Allowed URL

↓

HTTP Redirect

↓

localhost/admin
```

If the HTTP client follows redirects automatically, the blacklist is bypassed.

---

# Testing Checklist

Try variations of:

```text
http://127.1/

http://2130706433/

http://017700000001/

http://localhost/

http://127.0.0.1/
```

Also test:

- URL encoding
- Double URL encoding
- Redirect chains

---

# Bug Bounty Perspective

Do not stop testing after a blocked response.

Instead, explore:

- Alternative IP formats
- Encoding tricks
- Redirect behavior
- DNS resolution

Many real-world SSRF vulnerabilities are exploitable despite blacklist-based protections.

---

# Key Learnings

Blacklist filtering is generally ineffective against SSRF because attackers can represent the same destination in multiple equivalent ways. Robust validation should rely on strict allowlists rather than blocklists.