# Interview Notes - Authentication Security

## Authentication vs Authorization

| Authentication | Authorization |
|---|---|
| Verifies identity | Verifies permissions |
| “Who are you?” | “What can you access?” |

---

# What Is Username Enumeration?

Username enumeration occurs when applications reveal whether usernames exist through:

- response differences
- timing behavior
- error messages
- lockout behavior

---

# Common Username Enumeration Indicators

- Different response lengths
- Different status codes
- Timing differences
- Account lock messages

---

# What Is Brute Force?

Brute force is an automated attack where attackers repeatedly try different credentials until valid authentication succeeds.

---

# What Is Credential Stuffing?

Credential stuffing uses leaked username-password pairs from previous breaches against other applications.

---

# Difference Between Brute Force and Credential Stuffing

| Brute Force | Credential Stuffing |
|---|---|
| Guess passwords | Reuse leaked credentials |
| Slower | Faster |
| Random guessing | Real credentials |

---

# What Is MFA?

Multi-Factor Authentication requires multiple authentication factors.

Example:

```text
Password + Authenticator App
```

---

# Common MFA Weaknesses

- Missing validation
- Weak session handling
- Short numeric tokens
- No rate limiting

---

# Why Is Base64 Insecure?

Base64 is:

```text
encoding
```

NOT encryption.

Anyone can decode it easily.

---

# Why Is MD5 Weak?

MD5 is vulnerable because:

- fast brute force
- rainbow tables
- collision attacks
- unsalted hashes

---

# What Is Password Reset Poisoning?

Password reset poisoning occurs when attackers manipulate headers such as:

```http
X-Forwarded-Host
```

to poison reset links.

---

# Common Authentication Cookies

```text
session
remember-me
stay-logged-in
auth-token
```

---

# Common Burp Suite Tools

| Tool | Purpose |
|---|---|
| Proxy | Intercept traffic |
| Repeater | Manual testing |
| Intruder | Automated attacks |
| Decoder | Decode values |

---

# Common Successful Login Indicators

- HTTP 302
- Set-Cookie
- Redirects
- Dashboard access

---

# Secure Authentication Best Practices

Applications should:

- enforce HTTPS
- implement MFA
- use rate limiting
- normalize responses
- secure session handling
- use strong password hashing

---

# Recommended Password Hashing Algorithms

- bcrypt
- Argon2
- PBKDF2

---

# Common Authentication Vulnerabilities

| Vulnerability | Risk |
|---|---|
| Username Enumeration | Valid user discovery |
| Brute Force | Credential compromise |
| Broken MFA | Authentication bypass |
| Weak Sessions | Session hijacking |
| Weak Reset Logic | Account takeover |

---

# Important Security Principles

- Never trust client-side validation
- Validate everything server-side
- Normalize authentication responses
- Protect reset workflows
- Monitor suspicious activity

---

# Common Interview Questions

## Q: Why is rate limiting important?

Prevents automated brute-force attacks.

---

## Q: Why is MFA important?

Provides additional protection even if passwords are compromised.

---

## Q: Why are generic error messages important?

They prevent username enumeration.

---

## Q: Why should MD5 not be used?

MD5 is fast and vulnerable to brute-force attacks.

---

# Key Takeaways

- Authentication security is one of the most important areas of web security.
- Small logic flaws can completely bypass authentication.
- Response analysis is a critical pentesting skill.

> [!TIP]
> During interviews, explain BOTH the vulnerability and the business impact.