# Web Cache Poisoning Quick Revision

## Core formula

```text
Unkeyed/ambiguous input
+
Unsafe application behavior
+
Cacheable response
=
Web cache poisoning
```

## Classic flow

```text
Find input
  ↓
Observe reflection
  ↓
Determine key status
  ↓
Create harmful response
  ↓
Cache it
  ↓
Victim receives it
```

## Important terms

| Term | Meaning |
|---|---|
| Cache key | Inputs used to identify equivalent requests |
| Unkeyed input | Input ignored when constructing cache identity |
| Cache oracle | Feedback showing cache behavior |
| Gadget | Behavior chained with the cache flaw |
| Vary | Additional request headers affecting cache variants |
| Cache buster | Input used to force a fresh cache lookup |
| Parameter cloaking | Parser discrepancy used to hide attacker-controlled parameters |
| Fat GET | GET request with a body that may affect application behavior |
| Normalization | Transformation applied to cache-key input |
| Internal cache | Application/backend cache distinct from an external cache |

## High-value tests

```text
Headers
Cookies
Query strings
Query parameters
Host ports
Parameter delimiters
Normalization
GET bodies
Multiple caches
Dynamic resources
```
