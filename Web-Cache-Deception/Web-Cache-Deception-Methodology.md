# Web Cache Deception — Methodology

## Overview

Web Cache Deception testing focuses on identifying situations where the cache server and origin server interpret the same URL differently.

The objective is to determine whether this discrepancy can cause sensitive dynamic content to be stored in a cache and subsequently retrieved.

---

# Core Methodology

```text
Identify Sensitive Endpoint
        ↓
Understand Origin Server URL Mapping
        ↓
Understand Cache Rules
        ↓
Find Cache / Origin Discrepancy
        ↓
Construct Candidate URL
        ↓
Test Cache Behavior
        ↓
Confirm Sensitive Response Is Cached
        ↓
Verify Unauthorized Retrieval
```

---

# 1. Identify Sensitive Endpoints

Start by identifying endpoints that return sensitive, user-specific information.

Examples include:

```text
/my-account
/profile
/orders
/settings
```

Inspect the actual HTTP responses rather than relying only on the rendered page.

Look for:

```text
API Keys
Account Information
Personal Information
User-Specific Data
```

---

# 2. Establish a Baseline

Before modifying the URL, send the original request and record:

```text
URL
HTTP Method
Status Code
Response Body
Response Headers
X-Cache
Cache-Control
Response Time
```

Example:

```http
GET /my-account
```

This provides a reference for later comparisons.

---

# 3. Understand Origin URL Mapping

Test whether the origin server continues to return the same resource when the URL is modified.

Example:

```text
/my-account
```

then:

```text
/my-account/abc
```

If the same sensitive response is returned, the origin may be abstracting the additional path segment.

---

# 4. Test Static Extensions

Try extensions that may be associated with cache rules:

```text
.js
.css
.ico
```

Example:

```text
/my-account/abc.js
```

The objective is to determine whether:

```text
Origin
   ↓
Still returns sensitive dynamic content
```

while:

```text
Cache
   ↓
Treats URL as static
```

---

# 5. Test Delimiter Discrepancies

Identify characters that the origin treats as path delimiters.

Potential examples include:

```text
;
?
```

The exact behavior depends on the application.

A delimiter test can look like:

```text
/my-account;abc
```

or:

```text
/my-account?abc
```

Compare the response against the normal endpoint and a reference request.

---

# 6. Test Encoded Delimiters

If a delimiter behaves differently between the cache and origin, test its encoded representation.

Examples:

```text
%23
%3f
```

Other encoded characters may also be relevant depending on the parser behavior.

---

# 7. Test Normalization

Investigate how the cache and origin handle:

```text
Encoded slashes
Dot-segments
Encoded dot-segments
Path traversal sequences
```

Examples:

```text
%2f
%2e
..
```

A normalization discrepancy may allow a URL to represent one resource to the origin and another resource to the cache.

---

# 8. Test Static Directory Rules

Identify directories that appear to contain static resources.

Examples:

```text
/static
/assets
/scripts
/images
```

Test whether the cache uses the directory as a cache rule.

A normalization-based candidate may resemble:

```text
/static/..%2fprofile
```

where the cache and origin interpret the path differently.

---

# 9. Test File-Name Rules

Identify commonly cached file names.

Examples:

```text
index.html
robots.txt
favicon.ico
```

Determine whether the cache uses an exact-match rule.

Then investigate whether normalization can cause a malicious URL to resolve to that file name from the cache's perspective.

---

# 10. Confirm Cache Behavior

Use repeated requests and inspect cache indicators.

A useful sequence can be:

```http
X-Cache: miss
```

followed by:

```http
X-Cache: hit
```

Also inspect:

```text
Cache-Control
Response Time
Response Body
```

---

# 11. Use Cachebusters During Investigation

Use unique query parameters to avoid contamination from previous cache entries.

Example:

```text
?cb=001
?cb=002
?cb=003
```

Remember:

```text
Different Cachebuster
        ↓
Potentially Different Cache Key
```

Therefore, the final victim and attacker requests must use the same cache key when demonstrating the vulnerability.

---

# 12. Confirm Sensitive Content

Do not stop after identifying a cache hit.

Confirm that the cached response contains the sensitive information.

Example:

```text
X-Cache: miss
        ↓
Sensitive Response
        ↓
Response Cached
        ↓
X-Cache: hit
        ↓
Same Sensitive Response
```

---

# 13. Verify Unauthorized Retrieval

The final security impact should demonstrate that an attacker can retrieve information that belongs to another user.

Conceptually:

```text
Victim
   ↓
Requests Malicious URL
   ↓
Origin Generates Victim's Data
   ↓
Cache Stores Response
   ↓
Attacker Requests Same URL
   ↓
Cache Returns Victim's Data
```

---

# Main Discrepancy Categories

The Web Cache Deception techniques covered in this material can be organized into:

```text
Path Mapping Discrepancies
        ↓
Delimiter Discrepancies
        ↓
Delimiter Decoding Discrepancies
        ↓
Normalization Discrepancies
        ↓
Static Directory Cache Rules
        ↓
Exact File-Name Cache Rules
```

---

# Burp Suite Workflow

```text
Proxy
  ↓
Identify Sensitive Request
  ↓
Send to Repeater
  ↓
Establish Baseline
  ↓
Test Path Mapping
  ↓
Test Delimiters
  ↓
Test Encoded Delimiters
  ↓
Test Normalization
  ↓
Test Cache Rules
  ↓
Check X-Cache
  ↓
Confirm Cache Hit
  ↓
Verify Sensitive Content
```

---

# Testing Checklist

```text
☐ Identify sensitive GET endpoint
☐ Establish baseline response
☐ Inspect response headers
☐ Check X-Cache
☐ Test arbitrary path segments
☐ Test static extensions
☐ Test origin delimiters
☐ Test encoded delimiters
☐ Test normalization
☐ Identify static directory rules
☐ Identify exact file-name rules
☐ Use unique cachebusters
☐ Confirm cache miss
☐ Confirm cache hit
☐ Compare cached response body
☐ Verify sensitive information
☐ Verify unauthorized retrieval
☐ Document minimal reproduction
```

---

# Important Distinctions

## Cacheable

```text
Response is permitted to be cached
```

does not necessarily mean:

```text
Response was actually cached
```

---

## Cached

```text
Response was stored
```

does not necessarily mean:

```text
Application is vulnerable
```

---

## Vulnerable

A meaningful WCD vulnerability requires a combination of:

```text
Sensitive Dynamic Content
        +
Cache / Origin Discrepancy
        +
Cacheable Interpretation
        +
Actual Cached Response
        +
Unauthorized Retrieval
```

---

# Final Testing Flow

```text
START
  ↓
Sensitive Endpoint?
  │
  ├── NO → Find another endpoint
  │
  └── YES
       ↓
Origin URL Mapping Tested?
       │
       ├── NO → Test path mapping
       │
       └── YES
            ↓
Cache Rule Identified?
            │
            ├── NO → Test extensions/directories/file names
            │
            └── YES
                 ↓
Cache/Origin Discrepancy?
                 │
                 ├── NO → Test delimiters/normalization
                 │
                 └── YES
                      ↓
Sensitive Response Cached?
                      │
                      ├── NO → Continue testing
                      │
                      └── YES
                           ↓
Unauthorized Retrieval?
                           │
                           ├── NO → Assess further
                           │
                           └── YES
                                ↓
                         WCD Confirmed
```

---

# Key Takeaways

- Start with sensitive dynamic endpoints.
- Understand how the origin maps and normalizes URLs.
- Identify how the cache determines cacheability.
- Look specifically for differences between cache and origin interpretation.
- Test path mapping, delimiters, delimiter decoding, and normalization.
- Investigate static extensions, static directories, and exact file-name rules.
- Use Burp Repeater for controlled testing.
- Use cachebusters during investigation.
- Confirm actual caching rather than relying only on `Cache-Control`.
- Confirm that the cached response contains sensitive information.
- Demonstrate unauthorized retrieval to establish security impact.