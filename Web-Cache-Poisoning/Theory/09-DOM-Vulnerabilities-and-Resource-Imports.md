# Cache Poisoning and DOM-Based Vulnerabilities

Web cache poisoning can be used to manipulate imported data, not only HTML.

## Malicious JSON example

```json
{"someProperty" : "<svg onload=alert(1)>"}
```

If client-side JavaScript takes that value and passes it to a dangerous DOM sink, the payload can execute in the victim's browser.

## CORS

When malicious JSON is hosted on an attacker-controlled origin, the source notes that CORS may be required:

```http
Content-Type: application/json
Access-Control-Allow-Origin: *
```

## General chain

```text
Cache poisoning
      ↓
malicious resource URL
      ↓
victim imports attacker-controlled JSON
      ↓
DOM JavaScript processes JSON unsafely
      ↓
DOM-based vulnerability
```

This demonstrates why resource imports deserve the same attention as normal HTML responses.
