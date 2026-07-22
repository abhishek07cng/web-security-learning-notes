# SSRF with Whitelist-Based Input Filters

## Overview

Instead of blocking dangerous URLs, some applications only allow requests to a predefined list of trusted hosts.

This approach is generally more secure than blacklist filtering, but incorrect URL parsing or validation can still make it vulnerable to SSRF.

---

# How Whitelisting Works

Example:

```
Allowed Host

↓

stock.example.com

↓

Request Allowed
```

Any other hostname is rejected.

---

# Why It Can Be Bypassed

Applications often perform URL validation incorrectly.

Instead of parsing the URL according to the standard, they may simply check whether the input contains the trusted hostname.

Attackers can exploit inconsistencies in URL parsing.

---

# Common URL Parsing Tricks

## 1. Embedded Credentials

URLs support credentials before the hostname.

Example:

```text
https://trusted-site:password@evil.com
```

Everything before `@` is interpreted as user credentials.

The actual destination becomes:

```
evil.com
```

---

## 2. URL Fragments

The `#` character starts a URL fragment.

Example:

```text
https://evil.com#trusted-site.com
```

Some filters mistakenly validate the trusted hostname inside the fragment.

---

## 3. DNS Naming Hierarchy

Example:

```text
https://trusted-site.evil.com
```

A weak whitelist might only search for the string:

```
trusted-site
```

instead of validating the actual hostname.

---

## 4. URL Encoding

Attackers may encode special characters.

Examples:

```
%23

%40

%2F
```

Sometimes double encoding also works.

---

# Combining Techniques

Real attacks often combine multiple bypass methods.

Example:

```
http://localhost:80%2523@trusted-site.com/admin
```

This exploits inconsistencies between URL validation and backend URL parsing.

---

# Testing Checklist

Try:

- Embedded credentials
- URL fragments
- Encoded characters
- Double URL encoding
- Nested hostnames

---

# Bug Bounty Perspective

Whenever an application validates hostnames:

- Check how URLs are parsed.
- Compare frontend validation with backend behavior.
- Test different encoding techniques.
- Look for parser inconsistencies.

---

# Key Learnings

Whitelist-based filtering is stronger than blacklists but can still be bypassed when URL parsing is implemented incorrectly.