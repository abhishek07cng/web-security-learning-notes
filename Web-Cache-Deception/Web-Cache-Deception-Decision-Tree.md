# Web Cache Deception — Decision Tree

## Overview

This decision tree provides a structured workflow for testing Web Cache Deception.

The goal is to identify a situation where:

```text
Origin Server
      ↓
Returns Sensitive Dynamic Content

Cache Server
      ↓
Treats the Request as Cacheable
```

and the response can subsequently be retrieved from the cache.

---

# Start

```text
START
  ↓
Identify Sensitive Dynamic Endpoint
```

---

# 1. Is There Sensitive Dynamic Content?

```text
Sensitive Endpoint?
       │
   ┌───┴───┐
  NO      YES
  │         │
  ▼         ▼
Find     Establish
another   Baseline
endpoint
```

Examples:

```text
/my-account
/profile
/orders
/settings
```

---

# 2. Establish Baseline

Record:

```text
HTTP Method
Status Code
Response Body
Response Headers
X-Cache
Cache-Control
Response Time
```

Then continue:

```text
Baseline Established
        ↓
Test Origin Behavior
```

---

# 3. Test Path Mapping

Add an arbitrary path segment:

```text
/my-account/abc
```

Compare it with:

```text
/my-account
```

Ask:

```text
Does the origin still return the same sensitive response?
```

---

## If NO

```text
Additional Path Changes Response
        ↓
Path Mapping Technique May Not Work
        ↓
Try Delimiters
```

---

## If YES

```text
Additional Path Ignored
        ↓
Test Static Extension
```

Example:

```text
/my-account/abc.js
```

---

# 4. Does a Static Extension Trigger Caching?

Test:

```text
.js
.css
.ico
```

Ask:

```text
Does the modified URL become cacheable?
```

---

## If YES

```text
Origin
   ↓
Sensitive Response

Cache
   ↓
Static Extension Rule

        ↓

Test Actual Caching
```

---

## If NO

```text
Try Another Extension
        ↓
Try Delimiters
        ↓
Try Normalization
```

---

# 5. Test Delimiters

Identify possible origin delimiters.

Examples:

```text
;
?
```

Test:

```text
/my-account;abc
/my-account?abc
```

Compare each response with:

```text
/my-account
/my-accountabc
```

---

# 6. Is There a Delimiter Discrepancy?

```text
Delimiter interpreted differently?
             │
        ┌────┴────┐
       NO         YES
       │            │
       ▼            ▼
   Test        Add Static
Normalization  Extension
```

Example:

```text
/my-account;abc.js
```

Potential interpretation:

```text
Origin:
 /my-account

Cache:
 /my-account;abc.js
```

---

# 7. Test Encoded Delimiters

If delimiter behavior is interesting, test encoded representations.

Examples:

```text
%23
%3f
%00
%0A
%09
```

Ask:

```text
Does the cache decode the character differently from the origin?
```

---

# 8. Test Normalization

Investigate:

```text
Encoded slashes
Dot-segments
Encoded dot-segments
Path traversal
```

Examples:

```text
%2f
%2e
..
```

A useful candidate may look like:

```text
/static/..%2fprofile
```

---

# 9. Static Directory Rule

Identify possible static directories:

```text
/static
/assets
/scripts
/images
```

Ask:

```text
Does the cache treat this directory as cacheable?
```

---

## If YES

Test normalization discrepancies.

Example:

```text
/static/..%2fprofile
```

Potential interpretation:

```text
Cache:
 /static/..%2fprofile

Origin:
 /profile
```

---

# 10. Exact File-Name Rule

Identify commonly cached files:

```text
/index.html
/robots.txt
/favicon.ico
```

Confirm that the file is actually cached.

Then test normalization.

Example:

```text
/profile%2f%2e%2e%2findex.html
```

Ask:

```text
Does the cache normalize this to /index.html?
```

---

# 11. Confirm Cache Behavior

Inspect:

```text
X-Cache
Cache-Control
Response Time
Response Body
```

Useful sequence:

```text
First Request
      ↓
X-Cache: miss
      ↓
Origin Response
      ↓
Response Cached
      ↓
Same Request
      ↓
X-Cache: hit
```

---

# 12. Is the Sensitive Response Actually Cached?

```text
Sensitive response cached?
          │
      ┌───┴───┐
     NO      YES
     │         │
     ▼         ▼
 Continue   Verify
 Testing    Sensitive Data
```

Do not consider a cache rule alone sufficient evidence.

---

# 13. Does the Cached Response Contain Sensitive Information?

```text
Sensitive data present?
          │
      ┌───┴───┐
     NO      YES
     │         │
     ▼         ▼
Not WCD    Verify
Impact     Retrieval
```

---

# 14. Can the Cached Response Be Retrieved?

The final objective is:

```text
Victim
   ↓
Requests Crafted URL
   ↓
Origin Generates Sensitive Response
   ↓
Cache Stores Response
   ↓
Attacker Requests Same Cache Key
   ↓
Cache Returns Sensitive Response
```

---

# Final Decision

```text
Sensitive Endpoint?
       │
       └── YES
            ↓
Origin/Cache Discrepancy?
            │
       ┌────┴────┐
      NO        YES
      │           │
      ▼           ▼
 Continue     Cache Rule?
 Testing          │
             ┌────┴────┐
            NO        YES
            │           │
            ▼           ▼
         Continue   Actual Cache?
                     │
                ┌────┴────┐
               NO        YES
               │           │
               ▼           ▼
            Continue   Sensitive Data?
                            │
                       ┌────┴────┐
                      NO        YES
                      │           │
                      ▼           ▼
                   Continue   Unauthorized
                              Retrieval?
                                 │
                            ┌────┴────┐
                           NO        YES
                           │           │
                           ▼           ▼
                        Assess      WCD
                        Further    Confirmed
```

---

# Testing Priority

Use the following order:

```text
1. Sensitive Endpoints
        ↓
2. Baseline
        ↓
3. Path Mapping
        ↓
4. Static Extensions
        ↓
5. Delimiters
        ↓
6. Encoded Delimiters
        ↓
7. Normalization
        ↓
8. Static Directories
        ↓
9. Exact File Names
        ↓
10. Cache Confirmation
        ↓
11. Impact Verification
```

---

# Final Verification Checklist

```text
☐ Sensitive dynamic endpoint identified
☐ Baseline established
☐ Origin behavior understood
☐ Cache behavior understood
☐ Path mapping tested
☐ Static extensions tested
☐ Delimiters tested
☐ Encoded delimiters tested
☐ Normalization tested
☐ Static directory rules tested
☐ Exact file-name rules tested
☐ Cache miss observed
☐ Cache hit observed
☐ Sensitive response confirmed
☐ Same cache key verified
☐ Unauthorized retrieval demonstrated
```

---

# Key Takeaways

- Start with a sensitive dynamic endpoint.
- Establish a clean baseline before testing.
- Look for differences between cache and origin interpretation.
- Test path mapping first, followed by extensions, delimiters, and normalization.
- Investigate static directory and exact file-name cache rules.
- Confirm actual caching with repeated requests.
- Confirm that the cached response contains sensitive information.
- The final proof requires demonstrating that the cached sensitive response can be retrieved in an unauthorized context.