# Access Control Bypass CheatSheet

## Vertical Privilege Escalation

### Look For

```text
Admin URLs
Admin APIs
Admin Functions
```

---

### Test

```text
Direct Access
```

---

## Horizontal Privilege Escalation

### Look For

```text
Identifiers
```

---

### Test

```text
Change User Identifier
```

---

## IDOR

### Formula

```text
Find Identifier
        ↓
Modify Identifier
        ↓
Observe Response
```

---

## Header Bypass

### Test

```http
X-Original-URL
```

---

### Test

```http
X-Rewrite-URL
```

---

## Method Bypass

### Change

```http
POST
```

↓

```http
GET
```

---

## Workflow Bypass

### Skip

```text
Step 1
Step 2
```

---

### Execute

```text
Final Request Directly
```

---

## Authorization Testing Formula

```text
URL
        ↓
Method
        ↓
Headers
        ↓
Parameters
        ↓
Workflow
```