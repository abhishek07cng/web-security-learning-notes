# Authentication Wordlists Notes

## Overview

Wordlists are essential during authentication testing for:

- username enumeration
- password brute force
- credential stuffing
- MFA testing

Good wordlists significantly improve attack efficiency.

---

# Common Username Wordlists

## Typical Usernames

```text
admin
administrator
carlos
wiener
support
test
guest
root
manager
developer
```

---

# Common Password Wordlists

## Typical Weak Passwords

```text
password
password123
welcome123
admin123
qwerty
letmein
summer2024
```

---

# Credential Stuffing Lists

Credential stuffing uses:

```text
username:password
```

pairs from leaked breaches.

---

# Common Sources of Wordlists

| Source | Purpose |
|---|---|
| SecLists | General testing |
| RockYou | Password cracking |
| Assetnote | Targeted discovery |
| Custom Lists | Specific targets |

---

# Useful SecLists Paths

```text
SecLists/Usernames/
SecLists/Passwords/
SecLists/Fuzzing/
```

---

# Common MFA Wordlists

## 4-Digit MFA

```text
0000 → 9999
```

---

## 6-Digit MFA

```text
000000 → 999999
```

---

# Username Generation Patterns

Attackers commonly generate usernames using patterns:

```text
carlos
carlos1
carlos.admin
c.smith
admin
administrator
```

---

# Common Testing Workflow

```text
Enumerate Usernames
        ↓
Identify Valid Accounts
        ↓
Load Password Wordlist
        ↓
Perform Brute Force
```

---

# Common Wordlist Tips

- Smaller lists are faster
- Targeted lists are better
- Enumeration first improves efficiency
- Custom lists increase success rate

---

# Useful Tools

| Tool | Purpose |
|---|---|
| Burp Intruder | Automated attacks |
| Hydra | Login brute force |
| ffuf | Fuzzing |
| Hashcat | Password cracking |

---

# Common Mistakes

| Mistake | Problem |
|---|---|
| Huge Wordlists Immediately | Slow attacks |
| No Enumeration First | Inefficient brute force |
| No Customization | Lower success rate |

---

# Key Takeaways

- Good wordlists dramatically improve testing efficiency.
- Enumeration should happen before password attacks.
- Smaller targeted lists are often better than massive lists.

> [!TIP]
> Always start with smaller targeted wordlists before huge brute-force lists.