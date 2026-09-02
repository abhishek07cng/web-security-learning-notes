# Normalized Cache Keys

## Problem

Browsers may URL-encode payloads, making some reflected XSS issues difficult to exploit directly.

A cache may normalize keyed input before generating its cache key.

Example:

```text
GET /example?param="><test>
GET /example?param=%22%3e%3ctest%3e
```

If these produce the same cache key, an attacker can potentially poison the cache using an unencoded representation while a victim requests the browser-encoded representation.

## Attack model

```text
Attacker sends unencoded payload
        ↓
cache normalizes key
        ↓
poisoned response stored

Victim browser sends encoded URL
        ↓
same normalized cache key
        ↓
poisoned response returned
```

The source uses this behavior to demonstrate how cache normalization can revive otherwise difficult reflected XSS.
