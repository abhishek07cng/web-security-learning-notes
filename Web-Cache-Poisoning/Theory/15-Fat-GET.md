# Fat GET Requests

## Concept

Some systems accept GET requests with bodies.

If the cache key uses only the request line while the application reads a parameter from the body, the body can influence the response without changing the cache key.

Example structure:

```http
GET /?param=innocent HTTP/1.1
...

param=bad-stuff-here
```

## Why this matters

```text
Request line
    ↓
cache key = innocent

Request body
    ↓
application value = malicious
```

This creates a cache/application discrepancy.

## Possible workaround

The source describes HTTP method override behavior:

```http
GET /?param=innocent HTTP/1.1
X-HTTP-Method-Override: POST

param=bad-stuff-here
```

If the override header is unkeyed, this may create a pseudo-POST while preserving a GET-derived cache key.
