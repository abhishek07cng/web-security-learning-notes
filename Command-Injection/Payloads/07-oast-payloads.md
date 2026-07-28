# OAST Payloads

## Purpose

Use Out-of-Band interactions to confirm command execution.

---

## Example Payload

```text
nslookup BURP-COLLABORATOR-SUBDOMAIN
```

---

## Verification

1. Submit the request.
2. Poll Burp Collaborator.
3. Observe the DNS interaction.

---

# Expected Result

A recorded DNS lookup confirms successful command execution.

---

# Key Takeaways

Burp Collaborator is an effective mechanism for detecting Blind OS Command Injection.