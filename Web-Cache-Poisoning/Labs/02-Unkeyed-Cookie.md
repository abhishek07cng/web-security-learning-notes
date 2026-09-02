# Lab 02 — Web Cache Poisoning With an Unkeyed Cookie

## Objective

Poison the cache so the visitor's browser executes `alert(1)`.

## Step 1 — Observe the cookie

1. Load the home page.
2. Inspect the response.
3. Notice the `fehost=prod-cache-01` cookie.
4. Reload the page.
5. Observe that the cookie value is reflected inside a double-quoted JavaScript object.

## Step 2 — Confirm reflection

1. Send the request to Repeater.
2. Add a cache buster.
3. Change the cookie to an arbitrary value.
4. Confirm that the value is reflected.

## Step 3 — Inject the lab payload

Use the source's example:

```http
fehost=someString"-alert(1)-"someString
```

## Step 4 — Poison

Replay until the payload is reflected and:

```http
X-Cache: hit
```

appears.

## Step 5 — Verify

Load the URL in the browser and confirm the alert.

Remove the cache buster and continue re-poisoning until the lab's visitor receives the poisoned response.

## Key Learning

The cookie changes application output but is not included in the cache key.
