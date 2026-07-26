# Impact and Severity of Information Disclosure

## Overview

The impact of an Information Disclosure vulnerability depends on:

- What information is exposed.
- How sensitive that information is.
- Whether it can be used to perform further attacks.

Some disclosures have immediate consequences, while others become dangerous only when combined with additional vulnerabilities.

---

# Direct Impact

Some disclosures are sensitive by themselves.

Examples include:

- Credit card details
- API keys
- Database passwords
- Secret keys
- User credentials

If attackers obtain this information, the consequences can be severe.

---

# Indirect Impact

Many Information Disclosure vulnerabilities reveal technical details rather than confidential data.

Examples include:

- Framework versions
- Directory structure
- Hidden files
- Database names
- Error messages

Although these details may seem harmless, they often help attackers identify additional weaknesses.

---

# Example

If an error message reveals:

```
Apache Struts 2 2.3.31
```

An attacker can:

1. Search for known vulnerabilities affecting that version.
2. Locate publicly available exploits.
3. Attempt to compromise the application.

---

# Chained Attacks

Information Disclosure is frequently used as part of a larger attack chain.

Example:

```
Verbose Error

↓

Framework Version

↓

Known Vulnerability

↓

Remote Code Execution
```

---

# Assessing Severity

When evaluating an Information Disclosure finding, consider:

- Is the information confidential?
- Does it expose sensitive user data?
- Can it assist another attack?
- Does it reveal internal infrastructure?
- Can it lead to privilege escalation?

---

# Technical Information

Technical information is often low severity on its own.

However, it becomes much more significant if it enables another exploit.

Examples:

- Vulnerable software version
- Hidden directories
- Internal endpoints

---

# Business Information

Business information may expose:

- Internal operations
- Commercial secrets
- Sensitive documentation

The impact depends on the sensitivity of the exposed data.

---

# Key Takeaways

- Not all Information Disclosure vulnerabilities have the same impact.
- Direct disclosure of sensitive data is usually high severity.
- Technical disclosures become more serious when they facilitate additional attacks.