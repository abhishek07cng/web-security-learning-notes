# Unkeyed Header Examples

Candidate headers discussed by the source include:

```http
X-Forwarded-Host
X-Forwarded-Scheme
X-Host
X-Original-URL
Origin
```

These are not inherently vulnerable. Test whether the target:

1. accepts the header;
2. processes it;
3. changes the response;
4. excludes it from the cache key;
5. allows the resulting response to be cached.
