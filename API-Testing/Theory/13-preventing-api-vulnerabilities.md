# Preventing API Vulnerabilities

## Principle 1

Use Strong Authentication.

---

## Principle 2

Enforce Authorization Server-Side.

---

## Principle 3

Validate Inputs.

```text
Parameters
Types
Ranges
```

---

## Principle 4

Allowlist Object Properties.

Avoid:

```text
Mass Assignment
```

---

## Principle 5

Restrict Methods.

Allow only:

```text
GET
POST
PATCH
```

when necessary.

---

## Principle 6

Hide Documentation In Production.

---

## Principle 7

Rate Limit APIs.

---

## Principle 8

Log And Monitor.

---

# Defense Formula

```text
Authentication
+
Authorization
+
Validation
+
Least Privilege
```

---

# Key Takeaways

Defense-in-depth is essential.