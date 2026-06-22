# Parameter Removal Techniques

## Remove

```text
csrf
coupon
discount
email
token
username
```

---

## Duplicate Parameters

```http
coupon=A
coupon=B
```

---

## Empty Values

```http
coupon=
email=
```

---

## Related Labs

```text
Lab06
Lab08
```

---

# Bug Bounty Reminder

Servers should safely handle missing parameters.