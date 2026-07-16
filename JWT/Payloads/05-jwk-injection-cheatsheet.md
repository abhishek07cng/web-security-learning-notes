# JWK Injection Checklist

## Look For

```text
jwk
```

inside the JWT header.

---

## Questions

```text
Does The Server Accept Embedded Public Keys?

Does It Validate Trusted Keys?

Does It Ignore Unknown Keys?
```

---

## Indicators

```text
RS256

Embedded JWK

Custom Verification Logic
```

---

## Related Lab

```text
Lab04
```

---

# Key Learnings

The server should select the verification key, not the client.