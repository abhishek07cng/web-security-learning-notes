# Access Control Testing Checklist

## Vertical Access Control

### Admin Functionality

- [ ] Access admin URLs directly
- [ ] Check robots.txt
- [ ] Check sitemap.xml
- [ ] Check JavaScript files
- [ ] Check hidden endpoints

---

### Role Manipulation

- [ ] Cookies
- [ ] JWT Claims
- [ ] Hidden Fields
- [ ] JSON Parameters
- [ ] Profile Update Requests

Look For:

```text
role
roleid
admin
isAdmin
group
permission
accessLevel
```

---

### HTTP Methods

Test:

```http
GET
POST
PUT
PATCH
DELETE
OPTIONS
```

---

### Header-Based Bypass

Test:

```http
X-Original-URL
X-Rewrite-URL
X-Forwarded-For
X-Forwarded-Host
X-Host
```

---

## Horizontal Access Control

### User Identifiers

Test:

```text
id=
user=
uid=
account=
profile=
customer=
```

---

### Resource Enumeration

Check:

```text
Profiles
Invoices
Orders
Messages
Documents
API Keys
```

---

## Workflow Testing

- [ ] Capture complete workflow
- [ ] Replay final request
- [ ] Skip intermediate steps
- [ ] Modify sequence

---

## Authorization Testing Formula

```text
Can I Access?
        ↓
Can I Modify?
        ↓
Can I Escalate?
```