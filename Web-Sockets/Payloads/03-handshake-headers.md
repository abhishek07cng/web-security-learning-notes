# WebSocket Handshake Headers

```http
Sec-WebSocket-Version: 13
Sec-WebSocket-Key: RANDOM_BASE64_VALUE
Connection: keep-alive, Upgrade
Upgrade: websocket
Cookie: session=SESSION_VALUE
```

Successful response:

```http
HTTP/1.1 101 Switching Protocols
Connection: Upgrade
Upgrade: websocket
Sec-WebSocket-Accept: HASH_VALUE
```
