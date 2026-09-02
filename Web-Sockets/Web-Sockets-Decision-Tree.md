# WebSockets Decision Tree

**WebSocket functionality?**
→ Identify endpoint and messages.

**Messages available?**
→ Intercept, modify, replay, and generate.

**Attacker-controlled input processed/rendered?**
→ Test input-based vulnerabilities.

**Handshake has security-sensitive logic?**
→ Inspect headers, session handling, and custom headers.

**Only cookie-based session + no CSRF protection?**
→ Investigate CSWSH.

**Blind behavior?**
→ Consider OAST.
