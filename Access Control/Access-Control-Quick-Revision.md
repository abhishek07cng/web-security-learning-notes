# Access Control Quick Revision

## Access Control Models

### Vertical

```text
User
        ↓
Admin
```

---

### Horizontal

```text
User A
        ↓
User B Data
```

---

### Context-Dependent

```text
Workflow
        ↓
Step Bypass
```

---

## Most Common Findings

### 1. IDOR

```text
id=
```

↓

```text
Change Identifier
```

---

### 2. Admin Access

```text
/admin
```

↓

```text
Direct Access
```

---

### 3. Role Manipulation

```text
roleid=1
```

↓

```text
roleid=2
```

---

### 4. Header Bypass

```http
X-Original-URL
```

---

### 5. Method Bypass

```http
POST
```

↓

```http
GET
```

---

### 6. Workflow Bypass

```text
Replay Final Request
```

---

## Most Important Bug Bounty Questions

### Question 1

```text
Should I Have Access?
```

---

### Question 2

```text
Can I Access Another User's Data?
```

---

### Question 3

```text
Can I Become Admin?
```

---

### Question 4

```text
Can I Skip Validation?
```

---

## Severity Ladder

```text
Information Disclosure
        ↓
Data Modification
        ↓
Account Takeover
        ↓
Privilege Escalation
        ↓
Admin Access
```

---

# Personal Access Control Formula

```text
Authentication
        ↓
Authorization
        ↓
Ownership
        ↓
Impact
```

---

# Top Lessons From PortSwigger

1. Authentication ≠ Authorization
2. Hidden URLs Are Not Security
3. GUIDs Are Not Authorization
4. Headers Cannot Be Trusted
5. Every Request Needs Authorization
6. IDOR Is Everywhere
7. Workflow Validation Matters