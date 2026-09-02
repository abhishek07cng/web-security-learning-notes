# Lab 08 — Web Cache Poisoning via an Unkeyed Query Parameter

## Objective

Poison the home page so the victim's browser executes `alert(1)`.

## Steps

1. Confirm the home page is a cache oracle.
2. Change the query string and observe cache misses, indicating the query string is generally keyed.
3. Add a cache buster.
4. Use Param Miner's **Guess GET parameters** feature.
5. Identify:

```text
utm_content
```

6. Confirm that adding it can still produce a cache hit.
7. Observe that it is reflected in the response.
8. Inject:

```text
GET /?utm_content='/><script>alert(1)</script>
```

9. Cache the response.
10. Remove `utm_content`.
11. Copy the normal URL and load it in the browser.
12. Confirm the alert.
13. Remove the cache buster.
14. Re-add the malicious parameter and poison the cache for normal users.
