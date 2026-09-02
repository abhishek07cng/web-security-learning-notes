# Fat GET and Normalization Reference

## Fat GET

```http
GET /?param=innocent HTTP/1.1

param=bad-stuff-here
```

## Method override

```http
GET /?param=innocent HTTP/1.1
X-HTTP-Method-Override: POST

param=bad-stuff-here
```

## Normalization example

```text
GET /example?param="><test>
GET /example?param=%22%3e%3ctest%3e
```

If the cache normalizes both to the same key, a poisoning discrepancy may exist.
