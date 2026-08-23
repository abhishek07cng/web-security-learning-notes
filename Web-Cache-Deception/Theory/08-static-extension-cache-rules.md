# Static Extension Cache Rules

## Overview

Web caches often use static file extensions to determine which responses should be cached.

Common examples include:

- `.css`
- `.js`
- `.ico`

This behavior is particularly important for Web Cache Deception because an attacker may be able to append a static extension to a dynamic endpoint.

---

# Basic Concept

The attack relies on a discrepancy between:

```text
Origin Server
      ↓
Interprets URL as dynamic resource
```

and:

```text
Cache Server
      ↓
Interprets URL as static resource
```

The cache may therefore store the sensitive dynamic response.

---

# Attack Flow

```text
Dynamic Endpoint
       ↓
Add Arbitrary Path Segment
       ↓
Add Static Extension
       ↓
Origin Processes Dynamic Endpoint
       ↓
Cache Sees Static Extension
       ↓
Response Gets Cached
```

---

# Common Static Extensions

Common extensions that may be associated with static resources include:

```text
.js
.css
.ico
```

Other extensions may also be configured depending on the cache.

For testing, relevant extensions can include:

```text
.css
.ico
.exe
```

---

# Why Extensions Matter

Consider:

```text
/user/123/profile/wcd.css
```

An origin server using REST-style URL mapping may interpret this as:

```text
/user/123/profile
```

and treat:

```text
wcd.css
```

as an insignificant path parameter.

The origin therefore returns:

```text
Profile Information
```

The cache may instead interpret the URL as:

```text
/user/123/profile/wcd.css
```

and recognize:

```text
.css
```

as a static file extension.

If the cache has a rule for `.css`, it may store the profile response as though it were a CSS resource.

---

# Origin vs Cache

```text
                 /user/123/profile/wcd.css
                              │
               ┌──────────────┴──────────────┐
               │                             │
               ▼                             ▼
         Origin Server                  Cache Server
               │                             │
               ▼                             ▼
      /user/123/profile                 .css rule
               │                             │
               ▼                             ▼
      Profile Information              Cache Response
```

This difference creates the potential for Web Cache Deception.

---

# Testing Methodology

## Step 1 — Identify Sensitive Endpoint

Start with an endpoint that returns sensitive dynamic information.

Example:

```text
/api/orders/123
```

Establish a baseline response first.

---

# Step 2 — Add Arbitrary Path Segment

Modify the endpoint:

```text
/api/orders/123/foo
```

If the response still contains the same order information, this indicates that the origin server may be abstracting the URL path and ignoring the additional segment.

Conceptually:

```text
/api/orders/123
        ↓
Sensitive Order Data

/api/orders/123/foo
        ↓
Same Sensitive Order Data
```

---

# Step 3 — Add Static Extension

Now add a static extension:

```text
/api/orders/123/foo.js
```

The purpose is to test whether the cache recognizes the URL as a static resource.

---

# Step 4 — Observe Cache Behavior

Inspect:

```text
X-Cache
Cache-Control
Response Time
Response Body
```

A useful sequence may be:

```text
X-Cache: miss
```

followed by:

```text
X-Cache: hit
```

when the same cache key is requested again.

---

# What a Successful Test Indicates

If:

```text
/api/orders/123/foo
```

returns sensitive data,

and:

```text
/api/orders/123/foo.js
```

also returns the sensitive data and is cached, this can indicate:

```text
Origin
   ↓
Ignores additional path segment

Cache
   ↓
Recognizes .js

Result
   ↓
Dynamic response is cached
```

---

# Try Multiple Extensions

Do not assume that the cache only recognizes `.js`.

Test relevant extensions such as:

```text
.js
.css
.ico
.exe
```

Example:

```text
/api/orders/123/foo.js
/api/orders/123/foo.css
/api/orders/123/foo.ico
/api/orders/123/foo.exe
```

Record which extensions trigger caching behavior.

---

# Cache Rule Discovery

You are effectively trying to determine:

```text
Which extensions cause the cache
to treat a response as static?
```

Create a simple record:

| Extension | Cached? | Response |
|---|---|---|
| `.js` | | |
| `.css` | | |
| `.ico` | | |
| `.exe` | | |

---

# Cachebuster

Use a unique cachebuster during investigation:

```text
/api/orders/123/foo.js?cb=001
```

Then:

```text
/api/orders/123/foo.js?cb=002
```

This helps avoid contamination from previously cached responses.

---

# Important Limitation

A successful path-mapping technique may only work against the specific endpoint tested.

Different endpoints may have different URL abstraction and routing behavior.

Therefore:

```text
One vulnerable endpoint
        ≠
Entire application vulnerable
```

Test relevant endpoints individually.

---

# Burp Suite Workflow

```text
Find Sensitive Endpoint
        ↓
Send to Repeater
        ↓
Baseline
        ↓
Add Arbitrary Path Segment
        ↓
Compare Response
        ↓
Add .js
        ↓
Check Cache
        ↓
Add .css
        ↓
Check Cache
        ↓
Add .ico
        ↓
Check Cache
        ↓
Document Working Extension
```

---

# Example

## Baseline

```text
/api/orders/123
```

Response:

```text
Order Information
```

## Add Segment

```text
/api/orders/123/foo
```

Response:

```text
Same Order Information
```

## Add Extension

```text
/api/orders/123/foo.js
```

Possible response:

```text
X-Cache: miss
```

Repeat:

```text
X-Cache: hit
```

The response still contains:

```text
Order Information
```

This indicates that the cache may be storing the dynamic response under a URL that it interprets as a JavaScript resource.

---

# Detection Conditions

A useful path-mapping WCD candidate has:

```text
1. Sensitive dynamic endpoint
        +
2. Origin ignores arbitrary path segment
        +
3. Static extension triggers cache rule
        +
4. Sensitive response is actually cached
```

---

# Key Takeaways

- Static extension cache rules commonly target resources such as `.css` and `.js`.
- The origin and cache may interpret the same URL differently.
- REST-style URL mapping can abstract paths into logical resources.
- Adding an arbitrary path segment helps test how the origin maps URLs.
- Adding a static extension tests how the cache applies its static extension rules.
- A cached sensitive response demonstrates the security impact.
- Test multiple extensions because cache configurations vary.
- The behavior may be specific to the endpoint being tested.