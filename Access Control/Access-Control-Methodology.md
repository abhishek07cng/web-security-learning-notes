# Access Control Methodology

## Step 1 - Identify Sensitive Functionality

Look for:

```text
Admin Panels
User Management
Role Changes
Billing
Orders
Documents
API Keys
Password Changes
```

---

## Step 2 - Test Vertical Access Control

Ask:

```text
Can A Lower Privileged User
Access Admin Functionality?
```

---

### Check

```text
Hidden URLs
JavaScript Files
robots.txt
sitemap.xml
```

---

### Modify

```text
role
roleid
admin
isAdmin
```

---

## Step 3 - Test Horizontal Access Control

Ask:

```text
Can I Access Another User's Data?
```

---

### Look For

```text
id=
user=
uid=
account=
profile=
```

---

### Replace

```text
wiener
```

↓

```text
carlos
```

---

## Step 4 - Test IDOR

Formula:

```text
Find Identifier
        ↓
Modify Identifier
        ↓
Observe Response
```

---

### Test

```text
Numeric IDs
GUIDs
Usernames
Filenames
Document IDs
```

---

## Step 5 - Test Headers

Try:

```http
X-Original-URL
X-Rewrite-URL
X-Forwarded-For
Referer
Origin
```

---

## Step 6 - Test HTTP Methods

Convert:

```http
POST
```

↓

```http
GET
```

---

Also test:

```http
PUT
PATCH
DELETE
OPTIONS
```

---

## Step 7 - Test Multi-Step Workflows

Ask:

```text
Can I Skip Earlier Steps?
```

---

Replay:

```text
Final Request Directly
```

---

## Step 8 - Assess Impact

Can attacker:

```text
Read Data?
Modify Data?
Delete Data?
Become Admin?
Take Over Account?
```

---

# Personal Formula

```text
URL
        ↓
Parameters
        ↓
Headers
        ↓
Methods
        ↓
Workflow
        ↓
Impact
```