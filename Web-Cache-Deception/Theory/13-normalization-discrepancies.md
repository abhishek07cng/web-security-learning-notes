# Normalization Discrepancies

## Overview

URL normalization involves converting different representations of a URL path into a standardized form.

This can include:

```text
Decoding encoded characters
Resolving dot-segments
```

Different parsers may normalize URLs differently.

---

# Basic Concept

```text
Original URL
      ↓
Cache normalization
      ↓
Origin normalization
      ↓
Potentially different results
```

---

# Dot-Segments

A common normalization operation is resolving:

```text
..
```

which represents the parent directory.

For example:

```text
/static/../profile
```

can normalize to:

```text
/profile
```

---

# Encoded Slash

The slash character can be represented as:

```text
%2f
```

Therefore:

```text
/static/..%2fprofile
```

can potentially be interpreted as:

```text
/profile
```

by a server that decodes `%2f` and resolves the dot-segment.

---

# Origin Normalization

To test origin normalization, use a non-cacheable resource.

The source material recommends using a resource associated with a non-idempotent method such as:

```text
POST
```

Then test a path such as:

```text
/aaa/..%2fprofile
```

---

# Origin Behavior

If the response matches:

```text
/profile
```

and returns profile information, this indicates that the origin:

```text
Decodes the slash
        +
Resolves the dot-segment
```

---

# Cache Normalization

To test cache normalization, send a path containing a traversal sequence and arbitrary directory before a commonly cached file.

Example:

```text
/profile%2f%2e%2e%2findex.html
```

If the response is cached, this can indicate that the cache normalizes the path to:

```text
/index.html
```

If it is not cached, the cache may be interpreting the encoded path literally.

---

# Exploitable Discrepancy

An exploitable normalization discrepancy can occur when:

```text
Cache
   ↓
Resolves encoded dot-segments

Origin
   ↓
Does not resolve them
```

or vice versa, depending on the cache rule and endpoint.

---

# Static Directory Example

```text
/static/..%2fprofile
```

Origin:

```text
/profile
```

Cache:

```text
/static/..%2fprofile
```

If the cache has a rule for:

```text
/static
```

it may store the profile response.

---

# Exact-Match File Example

For an exact-match cache rule:

```text
/profile%2f%2e%2e%2findex.html
```

the cache may normalize the path to:

```text
/index.html
```

and apply the exact file-name cache rule.

---

# Testing Workflow

```text
Identify Sensitive Endpoint
        ↓
Test Origin Normalization
        ↓
Test Cache Normalization
        ↓
Compare Results
        ↓
Identify Discrepancy
        ↓
Combine With Cache Rule
        ↓
Confirm Cached Response
```

---

# Important Browser Consideration

When using path traversal sequences in a URL, encoding the dot-segments is important.

Otherwise, the victim's browser may resolve the traversal sequence before forwarding the request to the cache.

---

# Key Takeaways

- Normalization converts different URL representations into standardized paths.
- Decoding and dot-segment resolution can vary between parsers.
- Encoded slashes such as `%2f` are important when testing normalization.
- Test origin and cache normalization separately.
- A normalization discrepancy becomes useful for WCD when combined with a cache rule.