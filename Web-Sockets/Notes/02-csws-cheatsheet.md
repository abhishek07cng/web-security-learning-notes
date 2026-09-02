# CSWSH Cheatsheet

## Vulnerable condition
Cookie-based session handling with no CSRF token or other unpredictable value.

## Impact
- Unauthorized actions.
- Sensitive-data retrieval.
- Reading server-generated messages.

## Key point
`Sec-WebSocket-Key` is not an authentication/session token.
