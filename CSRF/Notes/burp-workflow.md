# Burp Workflow for CSRF Testing

## Standard Workflow

```text
Capture Legitimate Request
        ↓
Analyze Parameters
        ↓
Generate CSRF PoC
        ↓
Host Payload
        ↓
Deliver to Victim
        ↓
Verify Request Execution
```

---

# Step 1 - Capture Request

Use:

```text
Burp Proxy
```

to intercept legitimate state-changing requests.

---

# Common Target Requests

```http
POST /change-email
POST /transfer-funds
POST /change-password
```

---

# Step 2 - Analyze Request

Verify:

- request method
- parameters
- cookies
- CSRF tokens
- headers

---

# Step 3 - Generate CSRF PoC

## Burp Suite Professional

```text
Right Click Request
        ↓
Engagement Tools
        ↓
Generate CSRF PoC
```

---

# Step 4 - Enable Auto-Submit

Add:

```javascript
document.forms[0].submit();
```

for automatic execution.

---

# Step 5 - Host Payload

Use:

- exploit server
- local server
- attacker-controlled page

---

# Step 6 - Test the Attack

Verify:

- request sent successfully
- cookies attached automatically
- vulnerable action executed

---

# Common Verification Indicators

| Indicator | Meaning |
|---|---|
| Email Changed | Successful CSRF |
| HTTP 200 | Request accepted |
| State Change | Exploit worked |

---

# Useful Burp Tools

| Tool | Purpose |
|---|---|
| Proxy | Capture traffic |
| Repeater | Modify requests |
| Engagement Tools | Generate PoC |
| HTTP History | Verify requests |

---

# Related Theory

- `Theory/04-how-to-construct-a-csrf-attack.md`

---

# Related Labs

- `Labs/lab01-basic-csrf.md`

---

# Key Takeaways

- Burp Suite simplifies CSRF testing significantly.
- PoC generation dramatically speeds up exploitation.
- Always verify whether cookies attach automatically.

> [!TIP]
> Test CSRF PoCs in a separate browser session while authenticated to the target application.