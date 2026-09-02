# Input-Based Vulnerabilities

Most input-based WebSocket vulnerabilities can be investigated by tampering with message contents.

Example:

```json
{"message":"Hello Carlos"}
```

If attacker-controlled content is later processed or rendered without adequate defenses, it may result in a vulnerability.
