# XSS CSRF Bypass CheatSheet

## Important Concept

CSRF Tokens Do Not Stop XSS.

---

# Traditional CSRF

Can:

```text
Send Requests
```

Cannot:

```text
Read Responses
```

---

# XSS

Can:

```text
Send Requests
Read Responses
Read Tokens
```

---

# Attack Flow

```text
Stored XSS
        ↓
GET Protected Page
        ↓
Extract Token
        ↓
POST Request
        ↓
Action Completed
```

---

# Token Extraction

```javascript
var token =
responseText.match(
/name="csrf" value="(\w+)"/
)[1];
```

---

# Email Change Example

```javascript
POST
/my-account/change-email
```

---

# Simplified Workflow

```javascript
GET Account Page
        ↓
Extract Token
        ↓
Send Authenticated Request
```

---

# Related Lab

```text
Lab28
```

---

# Bug Bounty Reminder

If you find:

```text
Stored XSS
```

always check for:

```text
Email Change
Password Change
API Keys
Billing Changes
```

because XSS often bypasses CSRF defenses.