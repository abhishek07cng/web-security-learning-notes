# Path Mapping Discrepancies

## Overview

Web Cache Deception can occur when the cache server and origin server map URL paths to resources differently.

The key issue is:

```text
Same URL
   ↓
Different interpretation
   ↓
Different resource mapping
```

An attacker can potentially use this discrepancy to make the origin return sensitive dynamic content while causing the cache to treat the response as a cacheable resource.

---

# Basic Concept

```text
                 Same URL
                    │
          ┌─────────┴─────────┐
          │                   │
          ▼                   ▼
   Origin Server         Cache Server
          │                   │
          ▼                   ▼
   Dynamic Resource      Cacheable Resource
          │                   │
          └─────────┬─────────┘
                    ▼
             Response Cached
```

---

# Path Mapping

Path mapping refers to how the application interprets different parts of a URL path.

For example:

```text
/my-account/foo
```

may be interpreted by the origin server as:

```text
/my-account
```

with:

```text
foo
```

treated as an additional or insignificant path component.

The cache may instead treat the complete path literally:

```text
/my-account/foo
```

---

# REST-Style URL Mapping

Applications using REST-style URL structures may abstract paths into logical resources.

Example:

```text
/user/123/profile
```

represents:

```text
User 123
    ↓
Profile
```

The application may continue to return the profile even when an additional path segment is added:

```text
/user/123/profile/foo
```

If the origin still returns the profile response, this indicates that the additional path segment may not affect the resource mapping.

---

# Testing Path Mapping

Start with a sensitive endpoint:

```text
/my-account
```

Establish the normal response.

Then add an arbitrary path segment:

```text
/my-account/foo
```

Compare the responses.

If both return the same sensitive information:

```text
/my-account
        ↓
Sensitive Response

/my-account/foo
        ↓
Same Sensitive Response
```

the origin may be abstracting the path.

---

# Adding a Static Extension

After identifying this behavior, test whether a static extension changes cache behavior.

For example:

```text
/my-account/foo.js
```

The origin may continue to interpret this as:

```text
/my-account
```

while the cache may see:

```text
/my-account/foo.js
```

and apply a `.js` cache rule.

---

# Attack Flow

```text
Sensitive Endpoint
        ↓
Add Arbitrary Path Segment
        ↓
Origin Still Returns Sensitive Data
        ↓
Add Static Extension
        ↓
Cache Recognizes Static Extension
        ↓
Sensitive Response Gets Cached
```

---

# Example

Suppose:

```text
/api/orders/123
```

returns:

```text
Order Information
```

Test:

```text
/api/orders/123/foo
```

If the response remains:

```text
Order Information
```

test:

```text
/api/orders/123/foo.js
```

If the response is then cached:

```text
X-Cache: miss
```

followed by:

```text
X-Cache: hit
```

the behavior may indicate a path-mapping-based Web Cache Deception vulnerability.

---

# Origin vs Cache

```text
                 /api/orders/123/foo.js
                              │
               ┌──────────────┴──────────────┐
               │                             │
               ▼                             ▼
         Origin Server                  Cache Server
               │                             │
               ▼                             ▼
        /api/orders/123                 .js rule
               │                             │
               ▼                             ▼
       Order Information               Cached Response
```

The security issue arises because:

```text
Origin Interpretation
        ≠
Cache Interpretation
```

---

# Detecting the Discrepancy

Compare these requests:

```text
/api/orders/123
/api/orders/123/foo
/api/orders/123/foo.js
```

Record:

```text
Status Code
Response Body
Response Length
X-Cache
Cache-Control
Response Time
```

---

# Burp Suite Workflow

```text
Find Sensitive Endpoint
        ↓
Send to Repeater
        ↓
Send Baseline
        ↓
Add Arbitrary Segment
        ↓
Compare Response
        ↓
Add Static Extension
        ↓
Check X-Cache
        ↓
Repeat Request
        ↓
Confirm Cache Behavior
```

---

# Cachebuster

Use a unique cachebuster while investigating cache behavior:

```text
/api/orders/123/foo.js?cb=001
```

Then:

```text
/api/orders/123/foo.js?cb=002
```

This helps prevent an earlier cached response from interfering with the next test.

---

# Testing Multiple Endpoints

A path-mapping discrepancy may only affect specific endpoints.

For example:

```text
Endpoint A
   ↓
Additional path ignored

Endpoint B
   ↓
Additional path causes 404
```

Therefore:

```text
One affected endpoint
        ≠
Entire application affected
```

Test relevant sensitive endpoints individually.

---

# Testing Multiple Extensions

Once path mapping has been identified, test the cache's static extension rules.

Examples:

```text
/api/orders/123/foo.js
/api/orders/123/foo.css
/api/orders/123/foo.ico
```

Record which extensions result in cacheable behavior.

---

# Detection Conditions

A path-mapping WCD candidate generally requires:

```text
1. Sensitive dynamic endpoint
        +
2. Additional path segment does not change origin response
        +
3. Cache interprets the modified URL differently
        +
4. Cache rule treats the URL as cacheable
        +
5. Sensitive response is actually stored
```

---

# Important Distinction

A path-mapping discrepancy alone does not prove Web Cache Deception.

For example:

```text
/my-account/foo
```

returning the same response as:

```text
/my-account
```

only demonstrates unusual origin routing behavior.

You still need to establish:

```text
Cacheable Interpretation
        +
Actual Cached Response
        +
Security Impact
```

---

# Example Testing Table

| Request | Origin Response | Cached? | Notes |
|---|---|---|---|
| `/my-account` | Sensitive data | | Baseline |
| `/my-account/foo` | Sensitive data | | Path mapping |
| `/my-account/foo.js` | Sensitive data | | Static extension |
| `/my-account/foo.css` | Sensitive data | | Static extension |
| `/my-account/foo.ico` | Sensitive data | | Static extension |

---

# Complete Flow

```text
Identify Sensitive Endpoint
          ↓
Test Additional Path Segment
          ↓
Same Origin Response?
       /        \
     NO          YES
     │             │
     ▼             ▼
Move On       Test Static Extension
                    │
                    ▼
             Cache Rule Triggered?
                 /       \
               NO         YES
               │           │
               ▼           ▼
            Move On    Check Cache
                            │
                            ▼
                       Cache Hit?
                        /     \
                      NO       YES
                      │         │
                      ▼         ▼
                   Move On   Assess Impact
```

---

# Key Takeaways

- Path mapping discrepancies occur when the origin and cache interpret URL paths differently.
- REST-style applications may ignore or abstract additional path segments.
- Adding an arbitrary path segment is a useful way to test origin path mapping.
- Adding a static extension can test whether the cache interprets the URL as a static resource.
- A path-mapping discrepancy alone does not prove a vulnerability.
- Confirm that the sensitive response is actually cached.
- Test relevant endpoints individually because routing behavior can vary between endpoints.
- Use cachebusters during investigation to avoid interference from previous cache entries.