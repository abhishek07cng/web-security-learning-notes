# Internal Cache Poisoning

## Multiple cache layers

Modern systems may contain multiple caches:

```text
Client
  ↓
External cache
  ↓
Application
  ↓
Internal/application cache
```

Different layers may use different cache keys.

## Security risk

A value can be:

```text
keyed by external cache
but
unkeyed by internal cache
```

This creates a mismatch that can be exploited to poison a fragment inside the internal cache while bypassing the external cache with a cache buster.

## Testing

The supplied Lab 13 demonstrates:

1. Establish a cache oracle.
2. Use a dynamic external cache buster.
3. Identify an input such as X-Forwarded-Host.
4. Observe that a particular resource fragment becomes separately cached.
5. Determine that the internal cache ignores the query string.
6. Poison the internally cached resource.
7. Keep the relevant cache entries poisoned until the victim receives them.
