# State Machine Abuse

## Normal State

```text
Login
↓
2FA
↓
Authenticated
```

---

## Broken State

```text
Login
↓
Session Created
↓
Authenticated
↓
2FA Pending
```

---

## Targets

```text
Authentication
Password Reset
Registration
Checkout
```

---

## Related Labs

```text
Lab09
Lab11
```

---

# Key Question

```text
When Is The Session Created?
```