# File Name Cache Rules

## Overview

Caches may use exact file names to determine which responses should be cached.

Common examples include:

```text
robots.txt
index.html
favicon.ico
```

These files are common on web servers and often change infrequently.

---

# Basic Concept

```text
Request
   ↓
Exact File Name Match
   ↓
Cache Rule
   ↓
Response Cached
```

---

# Examples

Common file-name cache rules may target:

```text
/robots.txt
/index.html
/favicon.ico
```

The cache can match the exact file name string.

---

# Detecting File Name Rules

Send a GET request for a possible commonly cached file.

Example:

```text
GET /robots.txt
```

Inspect:

```text
X-Cache
Cache-Control
Response Time
```

If the response is cached, this may indicate an exact-match file-name cache rule.

---

# Exact-Match Behavior

Unlike an extension rule:

```text
*.js
```

an exact-match rule may require a specific file name:

```text
robots.txt
```

Therefore:

```text
/robots.txt
```

may be cached while:

```text
/abcrobots.txt
```

is not.

---

# Normalization Testing

To investigate whether the cache normalizes paths, use an encoded traversal sequence before the file name.

Example:

```text
/profile%2f%2e%2e%2findex.html
```

If this receives cached behavior, the cache may normalize the path to:

```text
/index.html
```

---

# Origin Normalization

Test the origin separately using a non-cacheable resource.

For example:

```text
/aaa/..%2fprofile
```

If the response matches:

```text
/profile
```

the origin may be decoding the slash and resolving the dot-segment.

---

# Exploiting the Discrepancy

The source material describes an exploitable discrepancy where:

```text
Cache
   ↓
Resolves encoded dot-segments
   ↓
Matches exact file name

Origin
   ↓
Does not resolve them
   ↓
Processes another resource
```

This can potentially allow sensitive dynamic content to be stored under an exact-match cached file name.

---

# Example Concept

```text
/profile%2f%2e%2e%2findex.html
             │
       ┌─────┴─────┐
       ▼           ▼
    Origin       Cache
       │           │
       ▼           ▼
 Different      /index.html
 Resource       Cache Rule
                   │
                   ▼
              Cached Response
```

---

# Delimiter + Normalization

The source material also covers combining:

```text
Delimiter Discrepancy
        +
Normalization Discrepancy
```

This can be useful when an exact-match cache rule is otherwise difficult to exploit.

---

# Testing Workflow

```text
Identify Exact-Match Cached File
        ↓
Confirm Cache Rule
        ↓
Test Origin Normalization
        ↓
Test Cache Normalization
        ↓
Identify Discrepancy
        ↓
Construct URL
        ↓
Confirm Cache Hit
        ↓
Assess Impact
```

---

# Key Takeaways

- Exact-match cache rules target specific file names.
- Common examples include `robots.txt`, `index.html`, and `favicon.ico`.
- Send GET requests to identify whether a file-name response is cached.
- Cache normalization can allow encoded traversal sequences to resolve to an exact file name.
- The source material describes exploiting a discrepancy where the cache resolves encoded dot-segments but the origin does not.
- Confirm the actual cached response before considering the technique successful.