# Web Cache Deception

## Overview

Web Cache Deception is a vulnerability that enables an attacker to trick a web cache into storing sensitive, dynamic content.

The vulnerability occurs because the **cache server and origin server interpret the requested URL differently**.

---

# Basic Concept

A typical Web Cache Deception attack works like this:

```text
Attacker
   ↓
Crafts Malicious URL
   ↓
Victim Visits URL
   ↓
Origin Server Returns Sensitive Dynamic Content
   ↓
Cache Misinterprets Request as Static
   ↓
Sensitive Response Gets Cached
   ↓
Attacker Requests Same URL
   ↓
Cached Sensitive Content Returned
```

---

# Example Scenario

Suppose an application has an endpoint:

```text
/my-account
```

The endpoint returns sensitive information belonging to the currently authenticated user.

Normally:

```text
GET /my-account
```

returns:

```text
User Account Information
API Key
Personal Information
```

The response is dynamic and should not be cached.

---

## Adding an Extra Path Segment

An attacker may test:

```text
/my-account/abc
```

If the origin server still returns the account information, this indicates that the origin abstracts or ignores the additional path segment.

For example:

```text
/my-account/abc
        ↓
Origin interprets as:
/my-account
```

---

# Cache Interpretation

The cache may interpret the same URL differently.

For example:

```text
/my-account/abc.js
```

The origin may interpret:

```text
/my-account/abc.js
        ↓
/my-account
```

while the cache may interpret:

```text
/my-account/abc.js
        ↓
Static JavaScript file
```

If the cache has a rule that caches `.js` resources, the sensitive response may be stored.

---

# Complete Attack

```text
                    /my-account/abc.js
                            │
             ┌──────────────┴──────────────┐
             │                             │
             ▼                             ▼
       Origin Server                  Cache Server
             │                             │
             ▼                             ▼
       /my-account                    *.js rule
             │                             │
             ▼                             ▼
      Sensitive Data                 Cache Response
             │                             │
             └──────────────┬──────────────┘
                            ▼
                    Sensitive Data
                       is cached
                            │
                            ▼
                    Attacker retrieves it
```

---

# Web Cache Deception vs Web Cache Poisoning

These vulnerabilities both involve caching but have different goals.

## Web Cache Deception

The attacker tricks the cache into storing:

```text
Sensitive Dynamic Content
```

The attacker then retrieves the cached sensitive information.

```text
Dynamic Response
      ↓
Incorrectly Cached
      ↓
Attacker Retrieves
```

---

## Web Cache Poisoning

The attacker manipulates a cached response so that malicious content is stored and subsequently served to other users.

```text
Malicious Input
      ↓
Cache Response Manipulation
      ↓
Malicious Content Cached
      ↓
Other Users Receive It
```

---

# Web Cache

A web cache sits between the client and the origin server.

```text
Client
  ↓
Cache
  ↓
Origin Server
```

When the cache does not have a stored response, this is called a:

```text
Cache Miss
```

The request is forwarded to the origin server.

The origin response can then be stored by the cache if it satisfies the cache rules.

---

# Cache Hit

If a matching cached response already exists:

```text
Client
  ↓
Cache
  ↓
Cached Response
```

The cache can return the stored response without contacting the origin server.

This is called a:

```text
Cache Hit
```

---

# Why Caching Exists

Caching is commonly used to improve web performance.

It is particularly common with:

```text
CDNs
Static Resources
Images
CSS
JavaScript
```

Instead of retrieving the same resource repeatedly from the origin server, a cache can serve a stored copy.

---

# Dynamic vs Static Content

## Static Content

Examples:

```text
.css
.js
.png
.jpg
.ico
```

Static content is commonly cached because it is generally reused and does not contain user-specific information.

---

## Dynamic Content

Examples:

```text
/my-account
/profile
/orders
/settings
```

Dynamic responses may contain sensitive, user-specific information and are generally not intended to be cached.

---

# Cache Keys

When a cache receives an HTTP request, it generates a **cache key**.

The cache key is used to determine whether a matching cached response already exists.

Common components include:

```text
URL Path
Query Parameters
Headers
Content Type
```

The exact cache key depends on the cache implementation.

---

# Cache Rules

Cache rules determine:

```text
What gets cached
How long it is cached
```

Common cache rules include:

### Static File Extension Rules

Match extensions such as:

```text
.js
.css
.ico
```

---

### Static Directory Rules

Match paths beginning with a specific directory:

```text
/static
/assets
```

---

### File Name Rules

Match specific file names such as:

```text
robots.txt
favicon.ico
```

---

# Why Cache Rules Matter

Web Cache Deception relies on the attacker finding a mismatch between:

```text
Cache Interpretation
        vs
Origin Interpretation
```

The attacker wants:

```text
Origin:
Dynamic Sensitive Endpoint
```

while the cache sees:

```text
Cache:
Static Cacheable Resource
```

---

# Common Sources of Discrepancy

The source material identifies three important categories:

```text
Path Mapping
Delimiter Processing
Path Normalization
```

These differences can cause the cache and origin server to interpret the same URL differently.

---

# Basic Testing Methodology

## Step 1 — Find a Sensitive Endpoint

Look for an endpoint that returns dynamic, user-specific information.

Examples:

```text
/my-account
/profile
/account
/orders
```

---

## Step 2 — Test Path Mapping

Add an arbitrary path segment:

```text
/my-account/abc
```

If the response still contains the same sensitive information, the origin may be ignoring the additional segment.

---

## Step 3 — Test Cache Rules

Add a static extension:

```text
/my-account/abc.js
```

Then observe the response.

---

## Step 4 — Determine Whether It Is Cached

Look for cache-related indicators such as:

```text
X-Cache
Cache-Control
Response Time
```

For example:

```http
X-Cache: miss
```

followed by:

```http
X-Cache: hit
```

can indicate that the response was cached.

---

# Cache Busters

During testing, make sure every test request has a unique cache key.

Otherwise, an earlier cached response may affect your results.

Example:

```text
/my-account/abc.js?cb=1
/my-account/abc.js?cb=2
/my-account/abc.js?cb=3
```

Burp Suite's Param Miner extension can be used to add dynamic cachebusters.

---

# Burp Suite Workflow

```text
Find Sensitive Endpoint
        ↓
Send Request to Repeater
        ↓
Establish Baseline
        ↓
Add Arbitrary Path Segment
        ↓
Check Origin Behavior
        ↓
Add Static Extension
        ↓
Check Cache Behavior
        ↓
Use Unique Cachebuster
        ↓
Confirm Cache Hit
        ↓
Construct Exploit
```

---

# Important Testing Principle

Do not assume that a URL is cacheable simply because it contains a static extension.

You need to confirm both sides:

```text
Origin Server
    ↓
Returns Sensitive Content

Cache Server
    ↓
Treats URL as Cacheable
```

Only when these behaviors combine does a Web Cache Deception vulnerability emerge.

---

# Key Takeaways

- Web Cache Deception tricks a cache into storing sensitive dynamic content.
- The vulnerability relies on discrepancies between cache and origin server behavior.
- Cache rules commonly target static resources.
- Path mapping, delimiters, and normalization can create useful discrepancies.
- A cache key determines whether a cached response can be reused.
- `X-Cache` and response timing can help identify cached responses.
- Unique cachebusters are important during testing.
- Web Cache Deception is different from Web Cache Poisoning.
- The ultimate goal is to demonstrate unauthorized access to cached sensitive information.