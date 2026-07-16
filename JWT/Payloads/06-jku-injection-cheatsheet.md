# JKU Injection Checklist

## Look For

```text
jku
```

inside the JWT header.

---

## Questions

```text
Does The Server Download Remote Keys?

Are JWKS URLs Allowlisted?

Can External Domains Be Used?
```

---

## Indicators

```text
Remote JWKS

RS256

External Key Retrieval
```

---

## Related Lab

```text
Lab05
```

---

# Key Learnings

Verification keys should only come from trusted locations.