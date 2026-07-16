# Algorithm Confusion Checklist

## Applicable Algorithms

```text
RS256

HS256
```

---

## Questions

```text
Does The Server Trust alg?

Can Algorithms Be Switched?

Is The Public Key Available?

Can Candidate Keys Be Derived?
```

---

## Indicators

```text
RS256

Public Keys

Algorithm Switching

Misconfigured JWT Libraries
```

---

## Related Labs

```text
Lab07

Lab08
```

---

# Key Learnings

The server must enforce the expected algorithm independently of the JWT.