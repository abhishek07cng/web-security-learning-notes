# Prevention Quick Reference

## Preferred

Avoid deserializing user input.

## If deserialization is unavoidable

1. Protect integrity with a digital signature.
2. Verify the signature **before** deserialization.
3. Prefer class-specific serialization.
4. Limit exposed fields.
5. Do not assume binary serialization is safe.
6. Do not rely on removing known gadget chains.

## Why signature timing matters

Bad:

```text
User input
   ↓
Deserialize
   ↓
Verify signature
```

Good:

```text
User input
   ↓
Verify signature
   ↓
Deserialize
```

The first approach can allow malicious behavior during deserialization before integrity is checked.
