# Lab 04 — Exploiting Normalization Discrepancies for Web Cache Deception

## Objective

Exploit a normalization discrepancy between the cache and origin server to retrieve sensitive information from a cached response.

---

# Core Concept

The vulnerability occurs when the cache and origin server normalize the same URL differently.

```text
Same URL
   ↓
┌──────────────────────┐
│                      │
▼                      ▼
Cache                Origin
│                      │
▼                      ▼
Normalizes            Does not normalize
the path              the path
│                      │
▼                      ▼
Matches cache rule    Processes another resource
```

---

# Required Knowledge

You should understand:

- Path normalization
- Encoded path traversal
- Static directory cache rules
- Cache behavior
- Origin server URL parsing

---

# Basic Testing

Start with a sensitive endpoint.

Example:

```text
/my-account
```

Test an encoded traversal sequence:

```text
/aaa/..%2fmy-account
```

Observe how the origin responds.

---

# Origin Server Behavior

If the origin does not decode `%2f` and resolve the dot-segment, it may interpret:

```text
/aaa/..%2fmy-account
```

literally.

This can result in:

```text
404 Not Found
```

rather than:

```text
/my-account
```

---

# Cache Behavior

Now investigate whether the cache normalizes the path.

A useful test is:

```text
/profile%2f%2e%2e%2findex.html
```

If the cache treats this as:

```text
/index.html
```

it may match an exact file-name cache rule.

---

# Exploitation Principle

The useful discrepancy is:

```text
Cache
   ↓
Decodes / resolves traversal
   ↓
Matches cache rule

Origin
   ↓
Does not perform the same normalization
   ↓
Processes the request differently
```

---

# Static Directory Variant

For a static directory cache rule, consider:

```text
/static/..%2fprofile
```

An origin that normalizes the path may process:

```text
/profile
```

while the cache may retain:

```text
/static/..%2fprofile
```

and apply the `/static` cache rule.

---

# Exact File-Name Variant

For an exact-match cache rule, the same concept can be applied using a known cached file.

Example:

```text
/profile%2f%2e%2e%2findex.html
```

The cache may normalize this to:

```text
/index.html
```

and therefore apply the exact-match cache rule.

---

# Burp Suite Workflow

```text
Identify Sensitive Endpoint
        ↓
Send Request to Repeater
        ↓
Test Origin Normalization
        ↓
Test Cache Normalization
        ↓
Identify Difference
        ↓
Combine With Cache Rule
        ↓
Send Request
        ↓
Check X-Cache
        ↓
Repeat Request
        ↓
Confirm Cache Hit
```

---

# Cachebuster

Use a unique cache key while testing.

Example:

```text
/profile%2f%2e%2e%2findex.html?wcd001
```

Then use a different value for another test:

```text
/profile%2f%2e%2e%2findex.html?wcd002
```

This helps prevent previously cached responses from affecting the results.

---

# Detection Conditions

A useful normalization-based WCD candidate has:

```text
1. Sensitive dynamic endpoint
        +
2. Origin and cache normalize differently
        +
3. Cache rule matches the normalized path
        +
4. Sensitive response is cached
```

---

# Important Limitation

A normalization discrepancy by itself does not prove Web Cache Deception.

You must establish:

```text
Normalization discrepancy
        +
Cache rule
        +
Sensitive response
        +
Actual cache hit
```

---

# Key Takeaways

- URL normalization can differ between cache and origin.
- Encoded slashes such as `%2f` are important when testing path normalization.
- Encoded dot-segments can expose parser differences.
- Static directory and exact file-name cache rules can both be relevant.
- Test origin and cache normalization separately.
- Use unique cachebusters during testing.
- Confirm the actual cached response before considering the technique successful.