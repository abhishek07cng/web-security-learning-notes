# Unkeyed Port and Unkeyed Query String

## Unkeyed port

Some caching systems exclude the port from the Host portion of the cache key.

Example concept:

```text
Host: vulnerable-website.com:1337
```

If the application still uses the full Host value while the cache ignores the port, a response generated using the port may be served to requests without it.

The source describes possible escalation to:

- denial of service through redirects to a bad port;
- XSS when non-numeric ports are accepted.

## Unkeyed query string

A cache may exclude the entire query string from its key.

This means:

```text
/?a=1
/?a=2
/?a=3
```

may map to the same cache entry.

## Detecting it

If the page is a cache oracle, change parameters and observe whether the response remains a cache hit.

If query-string cache busting does not work, use a cache buster in a keyed header that does not interfere with application behavior.

Examples from the source include:

```http
Accept-Encoding: gzip, deflate, cachebuster
Accept: */*, text/cachebuster
Cookie: cachebuster=1
Origin: https://cachebuster.vulnerable-website.com
```
