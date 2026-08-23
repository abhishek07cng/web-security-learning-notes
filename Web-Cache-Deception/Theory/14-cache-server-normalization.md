# Cache Server Normalization

## Overview

Cache servers may normalize URL paths before deciding whether a response matches a cache rule.

The exact behavior depends on the cache implementation.

Testing cache normalization can reveal whether encoded paths are transformed before cache rules are applied.

---

# Basic Concept

```text
Request
   ↓
Cache
   ↓
Normalize URL?
   ↓
Apply Cache Rule
   ↓
Store / Don't Store
```

---

# Testing Cache Normalization

Use a commonly cached file.

For example:

```text
/index.html
```

Then prepend an arbitrary directory and encoded traversal sequence:

```text
/profile%2f%2e%2e%2findex.html
```

---

# Possible Outcomes

## Cached Response

If the response is cached, this indicates that the cache may normalize:

```text
/profile%2f%2e%2e%2findex.html
```

to:

```text
/index.html
```

The exact-match file-name cache rule can then apply.

---

## Not Cached

If the response is not cached, the cache may interpret the path literally:

```text
/profile%2f%2e%2e%2findex.html
```

rather than normalizing it to:

```text
/index.html
```

---

# Example

```text
/profile%2f%2e%2e%2findex.html
```

Potential cache interpretation:

```text
/profile
      ↓
..
      ↓
/index.html
```

---

# Why This Matters

If the cache normalizes a path differently from the origin, an attacker may be able to construct a URL that:

```text
Origin
   ↓
Sensitive Dynamic Endpoint
```

while:

```text
Cache
   ↓
Known Cacheable Resource
```

---

# Exploitation Requirement

For an exact-match file-name rule, the source material states that the useful discrepancy is where:

```text
Cache
   ↓
Resolves encoded dot-segments

Origin
   ↓
Doesn't resolve them
```

This allows the cache to match the exact file name while the origin processes a different resource.

---

# Testing Workflow

```text
Identify Cached File
        ↓
Add Arbitrary Directory
        ↓
Add Encoded Traversal
        ↓
Append Cached File Name
        ↓
Send Request
        ↓
Check X-Cache
        ↓
Compare With Normal File Request
```

---

# Example

Normal:

```text
/index.html
```

Test:

```text
/profile%2f%2e%2e%2findex.html
```

If the test request produces the same cache behavior as:

```text
/index.html
```

the cache may be normalizing the encoded path.

---

# Burp Repeater

Use Repeater to compare:

```text
/index.html

/profile%2f%2e%2e%2findex.html
```

Inspect:

```text
Status Code
Response Body
X-Cache
Cache-Control
Response Time
```

---

# Key Takeaways

- Cache normalization can affect which cache rule matches.
- Encoded path traversal is useful for testing this behavior.
- A cached response can indicate that the cache normalized the path.
- Exact-match cache rules can be combined with normalization discrepancies.
- Always compare the test request against the normal cached resource.