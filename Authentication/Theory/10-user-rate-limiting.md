# 10 - User Rate Limiting

## Overview

User rate limiting restricts the number of requests that can be sent within a certain timeframe.

This helps slow automated attacks such as:

- Brute force
- Credential stuffing
- Password spraying

---

## How Rate Limiting Works

Applications may:

- Block excessive requests
- Introduce delays
- Trigger CAPTCHA
- Temporarily block IPs

Example:

```text
Maximum 5 login attempts per minute
```

---

## Common Weaknesses

Weak implementations may allow attackers to bypass restrictions.

---

## Common Bypass Techniques

| Technique | Purpose |
|---|---|
| VPN Rotation | Change IP address |
| Proxy Usage | Distribute requests |
| TOR Network | Hide attacker identity |
| Header Manipulation | Spoof client information |
| Distributed Attacks | Spread requests across systems |

---

## Single Request Multiple Guesses

Some applications process multiple credentials within one request.

Attackers may abuse this to bypass request-based limits.

---

## Testing Methodology

1. Send repeated login requests
2. Identify thresholds
3. Observe:
   - delays
   - IP blocks
   - CAPTCHA triggers
4. Attempt bypass techniques

---

## Real-World Risks

Weak rate limiting may allow:

- Automated account compromise
- Credential stuffing attacks
- Large-scale brute-force attacks

---

## Mitigation

Applications should:

- Enforce strict rate limiting
- Detect automation patterns
- Prevent IP spoofing
- Use CAPTCHA
- Monitor suspicious activity

---

## Key Takeaways

- Rate limiting significantly slows automated attacks.
- Weak implementations are commonly bypassed.
- IP-only protection is often insufficient.

> [!TIP]
> During testing, always analyze whether limits are account-based, IP-based, or session-based.