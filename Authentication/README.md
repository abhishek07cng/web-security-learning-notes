# Authentication Vulnerabilities

## Overview

This section contains detailed theory notes, practical lab writeups, payloads, methodologies, and security concepts related to authentication vulnerabilities from PortSwigger Web Security Academy.

The focus of this module includes:

- Authentication flaws
- Brute-force attacks
- Username enumeration
- MFA vulnerabilities
- Password reset weaknesses
- Session persistence issues
- Broken authentication logic

---

# Theory Topics Covered

| Topic No | Topic |
|---|---|
| 01 | Authentication Basics |
| 02 | Authentication vs Authorization |
| 03 | Authentication Vulnerabilities |
| 04 | Impact of Authentication Vulnerabilities |
| 05 | Password-Based Authentication |
| 06 | Brute-Force Attacks |
| 07 | Username Enumeration |
| 08 | Flawed Brute-Force Protection |
| 09 | Account Locking |
| 10 | User Rate Limiting |
| 11 | HTTP Basic Authentication |
| 12 | Multi-Factor Authentication |
| 13 | 2FA Vulnerabilities |
| 14 | 2FA Token Security |
| 15 | Bypassing 2FA |
| 16 | Bruteforcing 2FA Codes |
| 17 | Other Authentication Mechanisms |
| 18 | Remember-Me Vulnerabilities |
| 19 | Password Reset Vulnerabilities |
| 20 | Password Change Vulnerabilities |
| 21 | Preventing Authentication Attacks |
| 22 | Authentication Best Practices |

---

# Lab Categories

## Username Enumeration

- Lab01 - Username Enumeration via Different Responses
- Lab02 - Username Enumeration via Subtle Response Differences
- Lab03 - Username Enumeration via Subtle Response Differences 2
- Lab06 - Username Enumeration via Account Lock

---

## Brute Force

- Lab05 - Broken Brute-Force Protection (IP Block)
- Lab13 - Password Brute-Force via Password Change

---

## Multi-Factor Authentication

- Lab08 - 2FA Broken Logic

---

## Stay Logged In Vulnerabilities

- Lab09 - Brute-Forcing Stay Logged In Cookie
- Lab10 - Offline Password Cracking

---

## Password Reset Vulnerabilities

- Lab11 - Password Reset Broken Logic
- Lab12 - Password Reset Poisoning via Middleware

---

# What This Module Includes

- Detailed theory notes
- Practical attack methodology
- Burp Suite workflows
- Payload explanations
- Vulnerability analysis
- Mitigation techniques
- Real-world attack logic

---

# Common Tools Used

| Tool | Purpose |
|---|---|
| Burp Suite | Request interception |
| Burp Intruder | Brute-force attacks |
| Burp Repeater | Manual testing |
| Turbo Intruder | MFA brute force |
| ffuf | Fuzzing |
| Hashcat | Password cracking |

---

# Skills Practiced

- Authentication testing
- Response analysis
- Enumeration techniques
- MFA testing
- Session analysis
- Cookie analysis
- Password reset testing
- Burp Suite automation

---

# Notes

These writeups are intended for:

- Educational purposes
- Ethical hacking practice
- Security research
- Personal learning documentation

All testing is performed in authorized lab environments.