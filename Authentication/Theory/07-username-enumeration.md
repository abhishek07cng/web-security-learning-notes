# 07 - Username Enumeration

## Overview

Username enumeration occurs when an application reveals whether a username exists on the system.

This significantly reduces the difficulty of brute-force attacks because attackers can first identify valid usernames before attempting password attacks.

---

## How Username Enumeration Occurs

Applications may accidentally expose valid usernames through differences in:

- Error messages
- HTTP status codes
- Response length
- Response timing
- Redirect behavior

---

## Common Example

### Invalid Username

```text
Invalid username or password
```

### Valid Username + Invalid Password

```text
Incorrect password
```

These differences allow attackers to determine whether a username exists.

---

## Common Enumeration Indicators

Attackers compare:

| Indicator | Purpose |
|---|---|
| Response Length | Detect behavioral differences |
| HTTP Status Codes | Identify authentication changes |
| Error Messages | Reveal valid users |
| Response Timing | Detect additional backend checks |
| Redirect Behavior | Identify successful authentication stages |

---

## Response Timing Enumeration

Some applications only verify passwords after confirming that the username exists.

This can create measurable timing differences.

### Example

- Invalid username → immediate rejection
- Valid username → password hash verification → slightly slower response

Attackers may intentionally send extremely long passwords to amplify timing differences.

---

## Attack Methodology

### Typical Testing Workflow

1. Capture login request using Burp Suite
2. Send request to Burp Intruder
3. Set username field as payload position
4. Load candidate username wordlist
5. Launch attack
6. Analyze:
   - response length
   - status codes
   - response messages
   - timing differences
7. Identify valid usernames

---

## Common Tools Used

| Tool | Purpose |
|---|---|
| Burp Intruder | Automated enumeration |
| ffuf | Fast fuzzing |
| Turbo Intruder | High-speed testing |

---

## Real-World Risks

Username enumeration allows attackers to:

- Reduce brute-force complexity
- Target high-value accounts
- Conduct credential stuffing attacks
- Identify administrator accounts

---

## Prevention Techniques

Applications should:

- Use identical error messages
- Normalize response timing
- Return consistent HTTP status codes
- Prevent account discovery
- Avoid exposing usernames publicly

---

## Secure Error Message Example

### Insecure

```text
Username does not exist
```

### Secure

```text
Invalid username or password
```

---

## Key Takeaways

- Username enumeration is a common authentication weakness.
- Small response differences may reveal valid accounts.
- Consistent responses are critical for secure authentication systems.

> [!IMPORTANT]
> Even tiny behavioral differences can expose valid usernames.

> [!TIP]
> Always compare response length, timing, and status codes during authentication testing.