# 11 - HTTP Basic Authentication

## Overview

HTTP Basic Authentication is a simple authentication mechanism where credentials are transmitted using the HTTP `Authorization` header.

The client combines:

```text
username:password
```

and encodes the value using Base64.

The encoded credentials are then sent in the request header.

---

## Example

```http
Authorization: Basic base64(username:password)
```

Example:

```http
Authorization: Basic Y2FybG9zOnBhc3N3b3JkMTIz
```

---

## How HTTP Basic Authentication Works

### Authentication Workflow

1. User requests a protected resource
2. Server responds with authentication challenge
3. Browser prompts user for credentials
4. Browser encodes credentials using Base64
5. Credentials are automatically included in future requests

---

## Security Risks

Although simple to implement, HTTP Basic Authentication is generally considered insecure.

---

## 1. Credentials Sent Repeatedly

The browser automatically sends credentials with every authenticated request.

This increases exposure risk significantly.

---

## 2. Base64 Is NOT Encryption

Base64 only encodes data.

Anyone intercepting traffic can easily decode credentials.

### Example

```text
carlos:password123
```

becomes:

```text
Y2FybG9zOnBhc3N3b3JkMTIz
```

This is easily reversible.

---

## 3. Vulnerable Without HTTPS

If HTTPS is not enforced, attackers may capture credentials using:

- Man-in-the-middle attacks
- Packet sniffing
- Network interception

---

## 4. Weak Brute-Force Protection

Many HTTP Basic Authentication implementations lack:

- Rate limiting
- Account lockout
- CAPTCHA
- MFA

This makes automated brute-force attacks easier.

---

## 5. Vulnerable to Session Attacks

HTTP Basic Authentication may also become vulnerable to:

- CSRF attacks
- Credential replay attacks
- Session hijacking

---

## Common Attack Methodology

### Typical Testing Workflow

1. Identify protected endpoints
2. Observe Authorization headers
3. Decode Base64 credentials
4. Test brute-force protections
5. Analyze response behavior

---

## Tools Commonly Used

| Tool | Purpose |
|---|---|
| Burp Suite | Intercept requests |
| Burp Intruder | Brute-force credentials |
| CyberChef | Decode Base64 |
| Hydra | Automated attacks |

---

## Prevention

Applications should:

- Enforce HTTPS
- Avoid Basic Authentication when possible
- Implement strong rate limiting
- Use MFA
- Prevent brute-force attacks

---

## Key Takeaways

- HTTP Basic Authentication is simple but insecure.
- Base64 encoding does not provide security.
- Credentials are repeatedly exposed in requests.
- HTTPS is mandatory when using Basic Authentication.

> [!WARNING]
> Base64 encoding should never be confused with encryption.

> [!IMPORTANT]
> HTTP Basic Authentication should only be used in secure environments with HTTPS enforcement.