# Access Control Observations

## Observation 1

Broken Access Control is often easier to find than XSS.

---

## Observation 2

Most critical findings are caused by:

```text
Missing Authorization Checks
```

not complex bypasses.

---

## Observation 3

GUIDs are identifiers.

They are not security controls.

---

## Observation 4

Many applications validate:

```text
Authentication
```

but forget:

```text
Authorization
```

---

## Observation 5

Security through obscurity always fails.

---

## Observation 6

Every request should verify:

```text
Authentication
Authorization
Ownership
```

---

## Observation 7

Workflow-based vulnerabilities are frequently overlooked.

---

## Observation 8

Headers should never be trusted.

Examples:

```http
Referer
Origin
X-Forwarded-For
```

---

# Personal Revision Formula

```text
Authentication
        ↓
Authorization
        ↓
Ownership
```