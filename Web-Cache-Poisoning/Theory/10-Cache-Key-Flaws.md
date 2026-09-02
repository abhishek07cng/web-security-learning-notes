# Cache Key Flaws

## Core idea

The request path and query string are normally part of the cache key. Therefore, attackers historically could not easily poison a cache using keyed inputs because the malicious URL itself became a cache buster.

However, real cache implementations may transform keyed components.

The source identifies:

- excluding query strings
- filtering specific parameters
- normalizing keyed input

## The discrepancy

The key security concept is:

```text
Same client input
      ↓
Cache interprets it one way
      +
Application interprets it another way
      ↓
Different security meaning
```

A cache may store one representation in its key while passing another representation to the application.

This can turn apparently keyed inputs into usable poisoning vectors.
