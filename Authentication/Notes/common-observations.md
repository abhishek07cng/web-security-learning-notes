# Common Observations Notes

## Authentication Testing Observations

---

# Username Enumeration

## Common Indicators

- Different response lengths
- Different error messages
- Timing differences
- Lockout behavior
- Redirect changes

---

# Successful Login Indicators

| Indicator | Meaning |
|---|---|
| HTTP 302 | Successful authentication |
| Set-Cookie | Session creation |
| /my-account | Account access |
| Logout Button | Authenticated state |

---

# Common MFA Observations

- MFA codes are usually numeric
- Weak MFA often trusts session state
- Some applications create sessions before MFA validation
- Forced browsing sometimes bypasses MFA

---

# Password Reset Observations

- Reset tokens often appear in URLs
- Host header trust may cause poisoning
- Weak tokens are guessable
- Tokens may not expire correctly

---

# Remember-Me Observations

- Base64 encoding is common
- Weak cookies often contain usernames
- MD5 hashes frequently appear
- Some cookies are predictable

---

# Response Analysis Observations

- Small differences matter
- Length anomalies often reveal vulnerabilities
- Cookies frequently reveal authentication state
- Redirects commonly indicate successful actions

---

# Burp Testing Observations

- Sorting by response length is extremely useful
- Grep Match saves time
- Repeater is better for logic flaws
- Intruder is better for automation

---

# Common Logic Flaw Observations

- Applications trust client-side parameters too much
- Hidden parameters are often vulnerable
- Authentication state handling is frequently weak
- Business logic flaws are extremely dangerous

---

# Common Security Mistakes by Developers

| Mistake | Risk |
|---|---|
| Generic Logic Errors | Authentication bypass |
| Weak Session Handling | Unauthorized access |
| Trusting Headers | Password reset poisoning |
| Weak Token Design | Token prediction |

---

# Common Pentesting Lessons

- Small observations reveal major flaws
- Logic testing is critical
- Authentication workflows are complex
- Session analysis is extremely important

---

# Key Takeaways

- Good testing relies heavily on observation.
- Small behavioral differences often expose vulnerabilities.
- Response analysis is one of the most important pentesting skills.

> [!IMPORTANT]
> Always pay attention to redirects, cookies, and response lengths during testing.