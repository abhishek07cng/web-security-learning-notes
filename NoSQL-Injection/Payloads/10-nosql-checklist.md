# NoSQL Injection Testing Checklist

## Reconnaissance

☐ Identify user-controlled input.

☐ Determine whether MongoDB is being used.

☐ Intercept requests using Burp Suite.

---

## Syntax Injection

☐ Submit fuzz strings.

☐ Test individual special characters.

☐ Confirm valid syntax.

---

## Boolean Testing

☐ False condition

```text
' && 0 && 'x
```

☐ True condition

```text
' && 1 && 'x
```

☐ Always-true condition

```text
'||'1'=='1
```

---

## Operator Injection

☐ Test:

```text
$ne
```

☐ Test:

```text
$regex
```

☐ Test:

```text
$where
```

☐ Test:

```text
$in
```

---

## Data Extraction

☐ Determine field names.

☐ Determine field lengths.

☐ Extract values character by character.

---

## Timing-Based Testing

☐ Establish a response-time baseline.

☐ Inject timing payloads.

☐ Observe response delays.

---

## Prevention Review

☐ Input validation.

☐ Parameterized queries.

☐ Allowlists for accepted keys.

---

# One-Minute Workflow

```
Identify Input

↓

Syntax Injection

↓

Boolean Testing

↓

Operator Injection

↓

Authentication Bypass

↓

Data Extraction

↓

Field Enumeration

↓

Timing-Based Testing

↓

Report
```