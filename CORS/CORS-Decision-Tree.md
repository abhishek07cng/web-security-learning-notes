# CORS Decision Tree

```
Request

↓

Does response contain ACAO?

↓

No
    ↓
Probably Not CORS

Yes
↓

Can Origin be modified?

↓

No
    ↓
Review allowlist

Yes
↓

Does ACAO reflect Origin?

↓

No
    ↓
Check validation

Yes
↓

Is ACAC true?

↓

No
    ↓
Review exposed public data

Yes
↓

Sensitive response?

↓

No
    ↓
Low impact

Yes
↓

High Severity
```

---

## Quick Questions

- Does ACAO reflect Origin?
- Are credentials allowed?
- Is sensitive data returned?
- Is `null` trusted?
- Is HTTP trusted?
- Does a trusted origin have XSS?