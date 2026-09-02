# Securing WebSockets

- Use `wss://`.
- Hard-code the WebSocket endpoint URL.
- Do not place user-controllable data in the endpoint URL.
- Protect the handshake against CSRF.
- Treat WebSocket data as untrusted in both directions.
- Safely handle data on server and client.
- Prevent input-based issues such as SQL injection and XSS.
