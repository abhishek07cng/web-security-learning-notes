# WebSocket Messages

After the handshake, messages can be sent asynchronously in either direction.

```javascript
ws.send("Peter Wiener");
```

Messages can contain different data formats. JSON is commonly used for structured data.

```json
{"user":"Hal Pline","content":"Hello"}
```
