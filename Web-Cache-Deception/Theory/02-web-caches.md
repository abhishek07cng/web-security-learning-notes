# Web Caches

## Overview

A web cache is a system that sits between the client and the origin server.

Its purpose is to store copies of responses so that future requests for the same resource can be served without contacting the origin server every time.

---

# Basic Architecture

```text
Client
  │
  ▼
Web Cache
  │
  ▼
Origin Server
```

The cache acts as an intermediary between the user and the application.

---

# Cache Miss

When a client requests a resource and the cache does not already have a stored response, this is called a:

```text
Cache Miss
```

The normal flow is:

```text
Client
  ↓
Cache
  ↓
Cache Miss
  ↓
Origin Server
  ↓
Origin Processes Request
  ↓
Response
  ↓
Cache
  ↓
Client
```

The cache may store the response according to its configured rules.

---

# Cache Hit

If the cache already contains a response matching the incoming request, this is called a:

```text
Cache Hit
```

The flow becomes:

```text
Client
  ↓
Cache
  ↓
Cache Hit
  ↓
Stored Response
  ↓
Client
```

The origin server does not need to generate the response again.

---

# Why Web Caches Are Used

Caching is an important part of modern web infrastructure.

It can improve:

```text
Performance
Response Time
Scalability
Origin Server Load
```

Caching is particularly common for resources that are requested repeatedly.

Examples include:

```text
Images
CSS
JavaScript
Static Files
```

---

# Content Delivery Networks

CDNs commonly use caching.

A CDN can store copies of resources on distributed servers.

The basic concept is:

```text
Origin Server
      ↓
     CDN
      ↓
Distributed Cache
      ↓
     Users
```

Users can receive cached content from a server geographically closer to them.

This can reduce:

```text
Latency
Network Distance
Origin Server Load
```

---

# Static Content

Caches commonly store static resources.

Examples:

```text
.css
.js
.png
.jpg
.ico
```

These resources are generally reused across multiple requests or pages.

---

# Dynamic Content

Dynamic content is generally less suitable for caching.

Examples include:

```text
Account Information
Profile Information
Order Information
Personalized Responses
```

Dynamic responses may contain information specific to the authenticated user.

Caching such responses incorrectly can therefore create security problems.

---

# Cache Decision Process

When the cache receives a request, it needs to determine:

```text
1. Is there already a matching cached response?
2. If yes, can it be served?
3. If no, should the request go to the origin?
4. Should the resulting response be stored?
```

Conceptually:

```text
Incoming Request
       ↓
Generate Cache Key
       ↓
Existing Cached Response?
      / \
    YES  NO
     │    │
     ▼    ▼
 Cache   Origin
  Hit    Server
     │    │
     │    ▼
     │  Response
     │    │
     │    ▼
     │  Cache Rules
     │    │
     └────┴─────► Client
```

---

# Cache Key

The cache uses a cache key to determine whether two requests should be treated as equivalent.

A cache key commonly includes:

```text
URL Path
Query Parameters
```

Depending on the implementation, it can also include:

```text
Headers
Content Type
Other Request Elements
```

---

# Example

Consider:

```text
GET /static/app.js
```

The cache may generate a key based on the URL.

A later request for the same resource can produce the same key:

```text
GET /static/app.js
        ↓
Same Cache Key
        ↓
Cached Response
```

---

# Cache Rules

Caches use predefined rules to determine what responses should be stored and for how long.

Common rules target static resources.

For example:

```text
*.css
*.js
*.ico
```

A cache may also use rules based on:

```text
Static directories
Specific file names
URL parameters
Other custom criteria
```

---

# Static File Extension Rules

A cache may recognize common extensions as static resources.

Example:

```text
.js
.css
.ico
```

If a URL ends with one of these extensions, the cache may consider it suitable for caching.

This behavior is important when testing Web Cache Deception.

---

# Static Directory Rules

A cache may consider everything under a specific directory to be static.

Examples:

```text
/static/
```

or:

```text
/assets/
```

A request such as:

```text
/static/app.js
```

may therefore be cached according to the directory rule.

---

# File Name Rules

A cache can also have rules targeting specific file names.

Examples:

```text
robots.txt
favicon.ico
```

These files are generally required for common web operations and are relatively stable.

---

# Cache-Control

The response may contain a:

```http
Cache-Control
```

header.

For example:

```http
Cache-Control: public, max-age=30
```

A directive such as:

```text
public
```

with a positive:

```text
max-age
```

can suggest that the resource is cacheable.

However, this does not always prove that the response was actually cached because cache behavior can override the header.

---

# Detecting Cache Behavior

During security testing, inspect response headers.

One useful header is:

```http
X-Cache
```

Possible values include:

```http
X-Cache: hit
X-Cache: miss
X-Cache: dynamic
X-Cache: refresh
```

---

# X-Cache: hit

```http
X-Cache: hit
```

Generally indicates that the response was served from the cache.

---

# X-Cache: miss

```http
X-Cache: miss
```

Indicates that the cache did not have a response for the request's cache key.

The request was therefore fetched from the origin server.

A subsequent identical request may return:

```http
X-Cache: hit
```

if the response was cached.

---

# X-Cache: dynamic

```http
X-Cache: dynamic
```

Generally indicates that the content was dynamically generated and is not considered suitable for caching.

---

# X-Cache: refresh

```http
X-Cache: refresh
```

Can indicate that cached content was outdated and needed to be refreshed or revalidated.

---

# Response Timing

Response time can also provide an indication of caching.

For example:

```text
Request 1 → slower
Request 2 → significantly faster
```

The faster response may have been served from the cache.

However, timing alone should not be treated as definitive proof.

Use headers and repeated requests where possible.

---

# Cache Busters

During testing, cached responses can interfere with results.

To avoid this, use a unique cache key for each test.

For example:

```text
/request?cb=001
/request?cb=002
/request?cb=003
```

This prevents an earlier cached response from affecting the next test.

Burp Suite's Param Miner extension can automate dynamic cachebusters.

---

# Web Cache Deception Relevance

Web Cache Deception relies on the way cache systems identify and store resources.

The attacker looks for a discrepancy between:

```text
Cache
  ↓
"Static / Cacheable Resource"

Origin
  ↓
"Dynamic / Sensitive Endpoint"
```

The cache may therefore store a response that should never have been cached.

---

# Example

Suppose the origin treats:

```text
/my-account/abc
```

as:

```text
/my-account
```

but the cache uses a static extension rule.

The attacker may test:

```text
/my-account/abc.js
```

The origin could return:

```text
Account Information
```

while the cache sees:

```text
JavaScript Resource
```

If the cache stores the response, the dynamic account information may become accessible through the cached URL.

---

# Important Distinction

A cache is not inherently vulnerable simply because it caches responses.

The security issue occurs when:

```text
Cache Interpretation
        ≠
Origin Interpretation
```

and that discrepancy causes sensitive content to become cached.

---

# Key Takeaways

- A web cache sits between the client and origin server.
- A cache miss causes the request to be forwarded to the origin.
- A cache hit allows the cache to return a stored response.
- Caches commonly store static resources.
- Dynamic personalized content is generally not intended to be cached.
- Cache keys determine whether requests are considered equivalent.
- Cache rules determine what can be stored.
- Static extensions, directories, and file names are common cache rules.
- `X-Cache` can help identify cache behavior.
- `Cache-Control` can provide clues about cacheability.
- Response timing can provide additional evidence.
- Cachebusters help prevent previous cached responses from interfering with testing.
- Web Cache Deception relies on discrepancies between cache and origin server behavior.