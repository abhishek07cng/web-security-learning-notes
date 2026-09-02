# Lab 11 — URL Normalization

## Objective

Exploit cache normalization to execute reflected XSS that is otherwise neutralized by browser URL encoding.

## Steps

1. In Repeater, request a nonexistent path:

```text
GET /random
```

2. Observe that the path is reflected in the error response.
3. Inject:

```text
GET /random</p><script>alert(1)</script><p>foo
```

4. Request it directly in the browser.
5. Observe that the payload does not execute because the browser URL-encodes it.
6. In Repeater, poison the cache using the unencoded payload.
7. Immediately request the URL in the browser.
8. The cache normalizes the encoded request to the same key as the poisoned response.
9. Confirm `alert(1)`.
10. Re-poison the cache.
11. Deliver the malicious URL to the lab victim.

## Key Learning

Cache normalization can make two different URL representations share a cache key.
