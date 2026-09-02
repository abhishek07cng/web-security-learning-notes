# Testing for CSWSH

1. Review the WebSocket handshake.
2. Check how the session is established.
3. Determine whether only cookies identify the session.
4. Check for CSRF tokens or other unpredictable values.
5. Determine what messages can be sent and received.

Important: `Sec-WebSocket-Key` is not an authentication or session token.
