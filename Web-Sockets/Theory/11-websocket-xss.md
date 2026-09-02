# WebSocket XSS

Attacker-controlled WebSocket data may reach another user's browser.

Example:

```json
{"message":"<img src=1 onerror='alert(1)'>"}
```

Testing:
1. Capture a WebSocket message.
2. Modify its content.
3. Insert a controlled XSS proof of concept.
4. Forward or replay it.
5. Observe the result.
