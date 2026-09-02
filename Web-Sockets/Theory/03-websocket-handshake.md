# WebSocket Handshake

A WebSocket connection begins with an HTTP handshake.

```http
GET /chat HTTP/1.1
Host: normal-website.com
Sec-WebSocket-Version: 13
Sec-WebSocket-Key: RANDOM_BASE64_VALUE
Connection: keep-alive, Upgrade
Cookie: session=SESSION_VALUE
Upgrade: websocket
```

Successful response:

```http
HTTP/1.1 101 Switching Protocols
Connection: Upgrade
Upgrade: websocket
Sec-WebSocket-Accept: HASH_VALUE
```

`Sec-WebSocket-Key` is a Base64-encoded random value. `Sec-WebSocket-Accept` is derived from it according to the protocol.
