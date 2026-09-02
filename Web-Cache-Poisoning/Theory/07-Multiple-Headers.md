# Using Multiple Headers

Some cache poisoning vulnerabilities require more than one manipulated input.

## Example pattern

A site may redirect HTTP requests to HTTPS:

```http
GET /random HTTP/1.1
Host: innocent-site.com
X-Forwarded-Proto: http
```

Response:

```http
HTTP/1.1 301 moved permanently
Location: https://innocent-site.com/random
```

The redirect alone is not necessarily vulnerable.

The problem can arise when it is combined with another input that lets the attacker influence the generated URL.

## General attack structure

```text
Header A
  ↓
changes application behavior

Header B
  ↓
changes generated URL

Both together
  ↓
cacheable malicious response
```

This is an important reminder to test interactions between headers rather than testing each header only in isolation.
