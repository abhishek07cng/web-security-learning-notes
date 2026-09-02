# Core Cache Testing Reference

## Cache indicators

Look for:

```text
X-Cache: hit
X-Cache: miss
Cache-Status
Age
Via
Cache-Control
Vary
```

## Common cache-buster examples

```http
Accept-Encoding: gzip, deflate, cachebuster
Accept: */*, text/cachebuster
Cookie: cachebuster=1
Origin: https://cachebuster.vulnerable-website.com
```

Use cache busters carefully on authorized targets.
