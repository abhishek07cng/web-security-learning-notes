# How Web Caches Work

## Why Caching Exists

Without caching, a server may need to generate a new response for every request. Caching reduces duplicate back-end work and improves latency and scalability.

## Basic behavior

```text
Client
  ↓
Cache
  ↓
Back-end server
```

The cache stores responses for particular requests. When another request is considered equivalent, the cache can return the stored response without contacting the back-end.

## Cache keys

A cache determines equivalence using a predefined subset of request components called the **cache key**.

The source states that this commonly contains:

- request line
- Host header

Other components are **unkeyed**.

## Keyed vs unkeyed

```text
KEYED INPUT
    ↓
affects cache identity

UNKEYED INPUT
    ↓
ignored when deciding cache identity
    ↓
may still affect the back-end response
```

This discrepancy is central to classic web cache poisoning.

## Security significance

If an unkeyed value changes the generated response, an attacker may be able to inject data into a response while keeping the cache key unchanged.
