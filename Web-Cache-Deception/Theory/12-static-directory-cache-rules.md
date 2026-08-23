# Static Directory Cache Rules

## Overview

Web servers commonly store static resources inside dedicated directories.

Examples include:

```text
/static
/assets
/scripts
/images
```

Caches may use these path prefixes as cache rules.

---

# Basic Concept

```text
URL
 ↓
Static Directory Prefix
 ↓
Cache Rule
 ↓
Response Cached
```

---

# Example

Suppose the cache has a rule for:

```text
/static
```

A request such as:

```text
/static/app.js
```

may be cached.

---

# Web Cache Deception

A normalization discrepancy can allow a sensitive endpoint to appear to belong to a static directory to the cache.

Example:

```text
/static/..%2fprofile
```

An origin that decodes the slash and resolves the dot-segment may normalize this to:

```text
/profile
```

The origin therefore returns profile information.

A cache that does not decode the slash or resolve the dot-segment may interpret the path as:

```text
/static/..%2fprofile
```

Because it begins with:

```text
/static
```

the cache may store the response.

---

# Attack Flow

```text
/static/..%2fprofile
          ↓
      ┌───┴────┐
      ↓        ↓
   Origin     Cache
      ↓        ↓
 /profile   /static/..%2fprofile
      ↓        ↓
Profile     /static rule
Information     ↓
            Cached
```

---

# Path Traversal Knowledge

Understanding this technique requires knowledge of path traversal concepts.

The relevant sequence is:

```text
..
```

which represents the parent directory.

When encoded:

```text
%2f
```

represents:

```text
/
```

---

# Encoded Dot-Segments

The source material emphasizes that each dot-segment in the traversal sequence should be encoded when testing normalization discrepancies.

Example:

```text
/static/..%2fprofile
```

This helps prevent the victim's browser from resolving the path before it reaches the cache.

---

# Detecting Static Directory Rules

Identify likely static directories:

```text
/static
/assets
/scripts
/images
```

Then investigate whether requests under those prefixes are cached.

---

# Burp Workflow

```text
Find Sensitive Endpoint
        ↓
Identify Static Directory
        ↓
Test Encoded Path Traversal
        ↓
Observe Origin Response
        ↓
Observe Cache Behavior
        ↓
Confirm Cache Hit
```

---

# Important

A normalization discrepancy is required for this technique.

The attack depends on:

```text
Origin Interpretation
        ≠
Cache Interpretation
```

---

# Key Takeaways

- Static directory rules commonly target prefixes such as `/static` and `/assets`.
- Path normalization differences can cause WCD.
- Encoded path traversal can make the cache and origin interpret the same URL differently.
- Each dot-segment should be encoded during this style of testing.
- Confirm that the sensitive response is actually cached.