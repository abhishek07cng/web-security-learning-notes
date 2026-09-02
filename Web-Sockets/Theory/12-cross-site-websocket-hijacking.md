# Cross-Site WebSocket Hijacking

CSWSH is a CSRF vulnerability affecting a WebSocket handshake.

It arises when:
- The handshake relies solely on HTTP cookies for session handling.
- No CSRF token or other unpredictable value protects the handshake.

An attacker-controlled page can establish a WebSocket connection in the victim's session context.
