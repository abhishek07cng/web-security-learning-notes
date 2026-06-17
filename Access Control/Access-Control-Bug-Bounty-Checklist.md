# Access Control Bug Bounty Checklist

## Vertical Access Control

- [ ] Hidden Admin Pages
- [ ] robots.txt
- [ ] sitemap.xml
- [ ] JavaScript Endpoints
- [ ] Admin APIs
- [ ] Admin Functions

---

## Role Manipulation

- [ ] role
- [ ] roleid
- [ ] admin
- [ ] isAdmin
- [ ] permission
- [ ] group

---

## Horizontal Access Control

- [ ] id=
- [ ] user=
- [ ] account=
- [ ] customer=
- [ ] profile=

---

## IDOR

- [ ] Numeric IDs
- [ ] GUIDs
- [ ] Usernames
- [ ] Filenames
- [ ] Document IDs

---

## Headers

- [ ] X-Original-URL
- [ ] X-Rewrite-URL
- [ ] X-Forwarded-For
- [ ] Referer
- [ ] Origin

---

## Methods

- [ ] GET
- [ ] POST
- [ ] PUT
- [ ] PATCH
- [ ] DELETE

---

## Workflow Testing

- [ ] Skip Step 1
- [ ] Skip Step 2
- [ ] Replay Final Request

---

## Impact

- [ ] Data Disclosure
- [ ] Data Modification
- [ ] Account Takeover
- [ ] Privilege Escalation
- [ ] Admin Access