# XSS and Resource Poisoning Reference

## JavaScript resource

```text
/resources/js/tracking.js
```

Example lab payload:

```javascript
alert(document.cookie)
```

## DOM JSON example

```json
{
  "country": "<img src=1 onerror=alert(document.cookie) />"
}
```

## CORS header used in the supplied labs

```http
Access-Control-Allow-Origin: *
```

These examples are for the supplied authorized training labs.
