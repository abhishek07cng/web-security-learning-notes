# Cache Rules

## Overview

Cache rules determine **what responses can be cached and for how long**.

Caches commonly use rules designed to identify static resources because these resources are generally reused across multiple pages and do not change frequently.

Dynamic content is generally not intended to be cached because it can contain sensitive, user-specific information.

---

# Basic Concept

```text
HTTP Request
     ↓
Cache
     ↓
Evaluate Cache Rules
     ↓
Is Response Cacheable?
   /              \
 YES              NO
  │                │
  ▼                ▼
Store Response   Don't Cache
```

---

# Why Cache Rules Matter

Web Cache Deception attacks exploit the way these rules are applied.

The attacker attempts to make:

```text
Dynamic Sensitive Content
```

look like:

```text
Static Cacheable Content
```

to the cache.

This can happen when the cache and origin server interpret the URL differently.

---

# Main Types of Cache Rules

The important cache-rule categories covered in this topic are:

```text
1. Static file extension rules
2. Static directory rules
3. File name rules
4. Custom rules
```

---

# 1. Static File Extension Rules

These rules match the file extension at the end of a requested path.

Common examples include:

```text
.css
.js
.ico
```

The cache may be configured to store responses for requests ending in these extensions.

---

## Example

Request:

```text
/static/app.js
```

The cache identifies:

```text
.js
```

and applies its static extension rule.

```text
Request
   ↓
Ends with .js
   ↓
Static Extension Rule
   ↓
Cache Response
```

---

# Web Cache Deception Using Extensions

An attacker may attempt to append a static extension to a sensitive endpoint.

Example:

```text
/my-account/wcd.js
```

The origin server might interpret this as:

```text
/my-account
```

while the cache interprets the complete path as:

```text
/my-account/wcd.js
```

The cache then recognizes:

```text
.js
```

and may store the sensitive response.

---

# Testing Extensions

When testing an endpoint, do not assume that `.js` is the only supported extension.

Try a range of common extensions, such as:

```text
.js
.css
.ico
.exe
```

The exact behavior depends on the cache configuration.

---

# 2. Static Directory Rules

A cache may use a URL prefix to identify static content.

For example:

```text
/static
```

or:

```text
/assets
```

The cache may therefore treat requests beginning with these prefixes as cacheable.

---

## Example

```text
/assets/js/app.js
```

The cache sees:

```text
/assets
```

and applies the static directory rule.

```text
Request
   ↓
/assets prefix
   ↓
Static Directory Rule
   ↓
Cache Response
```

---

# Web Cache Deception Using Directories

If the origin server normalizes paths differently from the cache, an attacker may be able to construct a URL where:

```text
Cache
   ↓
Sees static directory

Origin
   ↓
Sees sensitive dynamic endpoint
```

This is one of the normalization-based Web Cache Deception techniques.

---

# 3. File Name Rules

Caches can also have rules that match specific file names.

Common examples include:

```text
robots.txt
favicon.ico
```

These files are commonly required for web operations and tend to change infrequently.

---

## Example

```text
/robots.txt
```

The cache recognizes:

```text
robots.txt
```

and may apply a file-name cache rule.

---

# Web Cache Deception Using File Names

If the cache has an exact-match file-name rule, an attacker may attempt to construct a URL that:

```text
Origin
   ↓
Interprets as dynamic endpoint

Cache
   ↓
Interprets as a known cacheable file
```

This can result in sensitive dynamic content being stored.

---

# 4. Custom Cache Rules

Caches may also implement custom rules based on other criteria.

Examples can include:

```text
URL parameters
Dynamic analysis
Specific URL patterns
Other cache configuration
```

The exact rules depend on the implementation.

---

# Cache Rule vs Cache Key

These two concepts are closely related but different.

## Cache Key

Answers:

```text
Which requests are equivalent?
```

Example:

```text
/path/resource.js?x=1
```

---

## Cache Rule

Answers:

```text
Should the response for this request be cached?
```

Example:

```text
Requests ending in .js → Cache
```

---

# Combined Example

Consider:

```text
/my-account/wcd.js
```

The process may look like:

```text
                 Request
                    │
                    ▼
            Generate Cache Key
                    │
                    ▼
             Evaluate Rule
                    │
                    ▼
              *.js matched
                    │
                    ▼
             Forward to Origin
                    │
                    ▼
           Origin returns data
                    │
                    ▼
             Cache response
```

If the origin interpreted the request as a sensitive endpoint, the cache may now contain sensitive data.

---

# Detecting Cache Rules

During testing, compare responses for different URL patterns.

For example:

```text
/my-account/abc
/my-account/abc.js
/my-account/abc.css
/my-account/abc.ico
```

Observe:

```text
Status Code
Response Body
X-Cache
Cache-Control
Response Time
```

---

# X-Cache

The `X-Cache` response header can provide useful evidence.

Common values include:

```http
X-Cache: miss
```

and:

```http
X-Cache: hit
```

A typical sequence is:

```text
First Request
     ↓
X-Cache: miss
     ↓
Response potentially cached
     ↓
Second Request
     ↓
X-Cache: hit
```

This can indicate that the response is being served from the cache.

---

# Cache-Control

The response may contain:

```http
Cache-Control: public, max-age=30
```

A positive `max-age` can suggest that the response is cacheable.

However:

```text
Cache-Control ≠ Proof of Actual Caching
```

The cache may override or otherwise handle the directive differently.

---

# Response Timing

A significant difference in response time can provide additional evidence.

Example:

```text
Request 1 → 500 ms
Request 2 → 50 ms
```

The faster response may have been served from the cache.

Timing should be treated as supporting evidence rather than definitive proof.

---

# Testing Static Extension Rules

```text
Sensitive Endpoint
       ↓
Add Arbitrary Path
       ↓
Add .js
       ↓
Send Request
       ↓
Check Cache Behavior
       ↓
Add .css
       ↓
Repeat
       ↓
Add .ico
       ↓
Repeat
```

---

# Testing Static Directory Rules

First identify paths that appear to belong to static directories:

```text
/static
/assets
```

Then investigate how the cache handles paths involving those prefixes.

The objective is to determine whether the cache recognizes the directory independently from how the origin interprets the path.

---

# Testing File Name Rules

Look for commonly cached file names:

```text
robots.txt
favicon.ico
```

Determine whether the cache uses an exact file-name rule.

---

# Cachebuster During Testing

Always consider cache state when testing.

Use a unique query parameter:

```text
?cb=001
?cb=002
?cb=003
```

This helps ensure that earlier cached responses do not interfere with subsequent tests.

Burp Param Miner can automate dynamic cachebusters.

---

# Web Cache Deception Relationship

The fundamental condition is:

```text
Origin Server
      ↓
Returns Sensitive Dynamic Content

        +

Cache
      ↓
Recognizes Request as Cacheable

        +

Different URL Interpretation
      ↓
Sensitive Response Gets Cached
```

---

# Key Takeaways

- Cache rules determine what responses are stored and for how long.
- Static file extension rules commonly target `.js`, `.css`, and `.ico`.
- Static directory rules can target prefixes such as `/static` or `/assets`.
- File-name rules can target resources such as `robots.txt` and `favicon.ico`.
- Caches may also implement custom rules.
- Web Cache Deception exploits discrepancies that cause dynamic content to match a cache rule.
- `X-Cache`, `Cache-Control`, and response timing can help identify cache behavior.
- Testing should use unique cachebusters to avoid interference from previous cached responses.