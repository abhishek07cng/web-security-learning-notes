# 08 - Flawed Brute-Force Protection

## Overview

Applications often implement protections against brute-force attacks.

However, weak or flawed implementations can frequently be bypassed by attackers.

Poorly designed protections may create a false sense of security while still allowing automated attacks.

---

## Common Brute-Force Protection Mechanisms

| Protection Mechanism | Purpose |
|---|---|
| Account Locking | Prevent repeated login attempts |
| IP Blocking | Block abusive IP addresses |
| CAPTCHA | Slow automated attacks |
| MFA | Add additional verification |
| Rate Limiting | Restrict request frequency |

---

## Common Weaknesses

Applications may become vulnerable when:

- Counters reset incorrectly
- Protection relies only on IP addresses
- CAPTCHA is poorly implemented
- Lockout logic is predictable
- Session validation is weak

---

## Example: Counter Reset Weakness

Some applications reset failed-attempt counters after successful authentication.

### Attack Scenario

1. Attacker submits two invalid passwords
2. Logs into a valid personal account
3. Failed-attempt counter resets
4. Continues brute-forcing target account

This bypasses lockout protections entirely.

---

## IP-Based Protection Weaknesses

Applications that rely only on IP blocking can often be bypassed using:

- VPNs
- Proxies
- TOR
- Rotating IP infrastructure
- Header manipulation

---

## Common Testing Methodology

1. Identify login protection mechanisms
2. Trigger failed login attempts
3. Observe:
   - lockout behavior
   - timing delays
   - response changes
4. Attempt bypass techniques
5. Analyze reset conditions

---

## Typical Indicators

Attackers commonly monitor:

- Account lock messages
- Delayed responses
- Temporary IP bans
- CAPTCHA appearance
- Authentication resets

---

## Real-World Risks

Weak brute-force protection may allow attackers to:

- Compromise accounts
- Conduct credential stuffing
- Bypass rate limits
- Automate password attacks

---

## Mitigation

Applications should:

- Implement strong rate limiting
- Use MFA
- Detect automation behavior
- Monitor suspicious logins
- Prevent IP manipulation
- Enforce CAPTCHA after repeated failures

---

## Key Takeaways

- Weak brute-force protection is often bypassable.
- Authentication logic flaws are extremely dangerous.
- Protection mechanisms must be tested thoroughly.

> [!WARNING]
> Poorly implemented security controls may provide little real protection.

> [!TIP]
> During testing, always analyze how counters reset after successful authentication.