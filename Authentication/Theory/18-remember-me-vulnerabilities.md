# 18 - Remember-Me Vulnerabilities

## Overview

Many applications provide a:

```text
Remember Me
Keep Me Logged In
Stay Logged In
```

feature that allows users to remain authenticated after closing the browser.

This functionality is commonly implemented using persistent authentication cookies.

---

## How Remember-Me Functionality Works

Applications generate a persistent token and store it inside a cookie.

Example:

```http
Cookie: stay-logged-in=TOKEN
```

When the user revisits the application, the cookie automatically authenticates the session.

---

## Why Remember-Me Cookies Are Dangerous

Possession of the remember-me cookie may allow attackers to bypass the normal login process entirely.

Weak cookie generation mechanisms can make these tokens vulnerable to:

- brute-forcing
- prediction
- theft
- replay attacks

---

## Common Weak Implementations

Some applications generate cookies using predictable values such as:

```text
username:timestamp
username:password
username:md5(password)
```

Example:

```text
base64(username:md5(password))
```

---

## Base64 Weakness

Some developers incorrectly assume Base64 encoding provides security.

However:

```text
Base64 is NOT encryption.
```

Attackers can easily decode Base64-encoded cookies.

---

## Weak Hashing Risks

Applications sometimes use weak hashing algorithms such as:

```text
MD5
SHA1
```

without:

- salts
- randomization
- secure token generation

This may allow attackers to brute-force authentication cookies offline.

---

## Example Attack Workflow

1. Attacker logs into personal account
2. Examines remember-me cookie
3. Decodes Base64 data
4. Identifies hashing algorithm
5. Reconstructs cookie generation logic
6. Brute-forces victim cookie

---

## Cookie Theft Attacks

Attackers may also steal remember-me cookies using vulnerabilities such as:

- Cross-Site Scripting (XSS)
- Session hijacking
- Packet interception
- Malware

---

## Open-Source Framework Risks

If applications use publicly documented token structures, attackers may understand token construction without reverse engineering.

---

## Common Testing Methodology

During testing, analyze:

- cookie structure
- encoding methods
- hashing algorithms
- token predictability
- expiration behavior

---

## Indicators of Weakness

| Indicator | Risk |
|---|---|
| Base64 Encoding | Easily decoded |
| Static Values | Predictable tokens |
| MD5 Usage | Weak hashing |
| Long-Lived Tokens | Persistent compromise |
| No Expiration | Permanent access |

---

## Real-World Risks

Weak remember-me functionality may allow attackers to:

- bypass authentication
- persist access indefinitely
- compromise multiple accounts
- automate session hijacking

---

## Mitigation

Applications should:

- Use random high-entropy tokens
- Store tokens securely server-side
- Expire tokens appropriately
- Invalidate tokens after logout
- Prevent brute-force attacks
- Use secure cookie flags

---

## Secure Cookie Practices

Applications should use:

```http
HttpOnly
Secure
SameSite
```

cookie attributes whenever possible.

---

## Key Takeaways

- Remember-me cookies effectively function as authentication credentials.
- Weak token generation creates severe security risks.
- Base64 encoding alone provides no security.

> [!WARNING]
> Persistent authentication cookies can allow attackers to bypass the login process entirely.

> [!IMPORTANT]
> Remember-me tokens should always be random, unpredictable, and securely validated server-side.