# Lab 12 — Cache Key Injection

## Objective

Combine multiple vulnerabilities and use `Pragma: x-get-cache-key` to execute `alert(1)`.

## Vulnerability chain

The source identifies four behaviors:

1. `utm_content` is excluded from the cache key through flawed parsing.
2. The login page uses raw `lang` data in a JavaScript import URL.
3. `/js/localize.js` can reflect an injected Origin header when `cors=1`.
4. The cache key uses an unescaped `$$` delimiter.

## Step 1 — Parameter cloaking

The source demonstrates:

```text
/login?lang=en?utm_content=anything
```

The sloppy exclusion logic lets attacker-controlled content travel through `lang`.

## Step 2 — Client-side parameter pollution

The login page creates a script import using the raw `lang` value and appends its own `&cors=0`.

## Step 3 — Header injection

When `cors=1` is used, `/js/localize.js` reflects the Origin header.

The source demonstrates CRLF-based response manipulation using an injected Origin value.

## Step 4 — Cache-key injection

Use:

```http
Pragma: x-get-cache-key
```

to inspect the cache key behavior.

The source explains that the unescaped `$$` delimiter allows a crafted value to forge the apparent key.

## Lab requests

The supplied source gives these two requests:

```http
GET /js/localize.js?lang=en?utm_content=z&cors=1&x=1 HTTP/2
Origin: x%0d%0aContent-Length:%208%0d%0a%0d%0aalert(1)$$$$
```

and:

```http
GET /login?lang=en?utm_content=x%26cors=1%26x=1$$origin=x%250d%250aContent-Length:%208%250d%250a%250d%250aalert(1)$$%23 HTTP/2
```

The source notes that the injected origin is lowercase for HTTP/2 compliance.

## Result

The combined behavior poisons `/login?lang=en` so it redirects to a login page whose localization import executes the payload.

## Key Learning

A complex cache attack can emerge from several individually subtle parsing and injection bugs.
