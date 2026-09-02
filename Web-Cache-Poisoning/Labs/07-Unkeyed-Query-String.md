# Lab 07 — Web Cache Poisoning via an Unkeyed Query String

## Objective

Poison the home page so it executes `alert(1)`.

## Steps

1. Load the home page.
2. Find the GET request in HTTP history.
3. Send it to Repeater.
4. Add arbitrary query parameters.
5. Observe that changing them can still produce a cache hit.
6. Use the `Origin` header as a cache buster.
7. On a cache miss, confirm the query parameter is reflected.
8. Use:

```text
GET /?evil='/><script>alert(1)</script>
```

9. Replay until the payload is reflected and `X-Cache: hit` appears.
10. Remove the query string while retaining the cache buster.
11. Confirm the poisoned response is still served.
12. Remove the cache-buster header.
13. Re-add the payload and poison the cache for normal users.
14. Load the home page and observe the popup.

The source notes that re-poisoning may be necessary because of the cache timing.
