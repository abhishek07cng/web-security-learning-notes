# alg=none Checklist

## Inspect Header

Look For:

```json
{
  "alg":"HS256"
}
```

---

## Questions

```text
Does The Server Reject Unsigned JWTs?

Does It Ignore Signature Errors?

Does It Return Different Responses?
```

---

## Indicators

```text
Older JWT Libraries

Custom JWT Implementations

Missing Signature Validation
```

---

# Related Lab

```text
Lab02
```

---

# Key Learnings

The application should define the accepted algorithm, not the client.