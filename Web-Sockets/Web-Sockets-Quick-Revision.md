# WebSockets Quick Revision

- WebSockets provide long-lived, two-way asynchronous communication.
- They start with an HTTP handshake.
- `wss://` uses TLS.
- `Sec-WebSocket-Key` is not authentication.
- Burp Proxy intercepts traffic.
- Repeater replays/modifies/generates messages.
- WebSocket input can lead to SQLi, XXE, XSS, or blind vulnerabilities.
- Handshake flaws can involve trusted headers and session handling.
- CSWSH is CSRF against a WebSocket handshake.
- Secure with `wss://`, CSRF protection, hard-coded endpoints, and safe handling of untrusted data.
