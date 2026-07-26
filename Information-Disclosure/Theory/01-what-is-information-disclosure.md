# What is Information Disclosure?

## Definition

Information Disclosure, also known as **Information Leakage**, occurs when a web application unintentionally exposes sensitive information to users.

The leaked information may be directly valuable to an attacker or may provide useful clues that help identify additional vulnerabilities.

Unlike many other web vulnerabilities, Information Disclosure is often not an attack by itself. Instead, it frequently serves as a stepping stone for discovering and exploiting more serious security issues.

---

# Why is Information Disclosure Important?

Learning to identify Information Disclosure vulnerabilities is an essential skill for penetration testers and bug bounty hunters because:

- They are commonly encountered during web application testing.
- Leaked information can reveal hidden attack surfaces.
- Technical details may simplify exploitation of other vulnerabilities.
- Small pieces of leaked information can often be combined into a high-impact attack.

Even seemingly harmless disclosures may provide attackers with valuable intelligence.

---

# Types of Information That May Be Disclosed

A vulnerable application may unintentionally expose:

## User Data

Examples include:

- Usernames
- Email addresses
- Financial information
- Personal information

---

## Business Information

Examples include:

- Internal documentation
- Commercial data
- Company secrets
- Configuration details

---

## Technical Information

Examples include:

- Framework names
- Framework versions
- Database names
- Database table names
- Internal IP addresses
- Hidden directories
- API keys
- Source code
- Backup files
- Version control history

Although technical information may not appear dangerous on its own, it often helps attackers identify further weaknesses.

---

# How Information Disclosure Happens

Information may be exposed in two different ways.

## Passive Disclosure

Sensitive information is visible during normal browsing.

Examples:

- HTML comments
- robots.txt
- Directory listings

---

## Active Disclosure

The attacker deliberately interacts with the application in unexpected ways to trigger information leakage.

Examples:

- Invalid input
- Unexpected parameter values
- Fuzzing
- Malformed requests

The attacker carefully studies each response for useful information.

---

# Real-World Examples

Examples discussed in the PortSwigger material include:

- Hidden directories listed in robots.txt
- Directory listings
- Backup source code files
- Database table names in error messages
- Hard-coded API keys
- Database credentials
- Credit card information
- Differences in application responses
- Framework version disclosure

---

# Why Attackers Like Information Disclosure

Information Disclosure reduces the amount of guessing required during testing.

Instead of blindly attacking an application, attackers can:

- Learn the application's technology stack.
- Discover hidden functionality.
- Identify vulnerable software versions.
- Locate sensitive resources.
- Develop more targeted attacks.

---

# Example Attack Flow

```
Browse Application

↓

Collect Technical Information

↓

Identify Hidden Resources

↓

Discover Vulnerable Framework

↓

Research Public Exploit

↓

Exploit Application
```

---

# Key Takeaways

- Information Disclosure is the unintended exposure of sensitive information.
- Both technical and business information can be valuable to attackers.
- Small disclosures often become part of larger attack chains.
- Testing should always include searching for accidental information leaks.