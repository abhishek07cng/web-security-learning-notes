# CSWSH Handshake Tests

Check whether:
- Session handling relies on cookies.
- A CSRF token is present.
- Another unpredictable value protects the handshake.

Potentially vulnerable pattern:

```http
Cookie: session=SESSION_VALUE
Upgrade: websocket
Connection: keep-alive, Upgrade
```

`Sec-WebSocket-Key` is not used for authentication or session handling.
