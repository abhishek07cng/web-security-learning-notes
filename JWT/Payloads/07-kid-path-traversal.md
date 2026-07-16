# KID Header Checklist

## Look For

```text
kid
```

inside the JWT header.

---

## Questions

```text
How Does The Server Resolve kid?

Database?

Filesystem?

Key Store?
```

---

## Indicators

```text
Path Traversal

Filesystem Lookup

Unexpected Key Selection
```

---

## Related Lab

```text
Lab06
```

---

# Key Learnings

Key identifiers should never directly control filesystem access.