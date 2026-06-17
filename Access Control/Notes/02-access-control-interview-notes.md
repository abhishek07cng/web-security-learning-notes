# Access Control Interview Notes

## What Is Access Control?

Determines:

```text
What Actions
A User Can Perform
```

---

## Difference Between Authentication And Authorization?

### Authentication

```text
Who Are You?
```

---

### Authorization

```text
What Can You Do?
```

---

## What Is Vertical Privilege Escalation?

```text
User
        ↓
Admin
```

---

## What Is Horizontal Privilege Escalation?

```text
User A
        ↓
User B Data
```

---

## What Is IDOR?

An access control vulnerability caused by:

```text
Missing Ownership Validation
```

---

## Are GUIDs Secure?

```text
No
```

GUIDs are identifiers, not authorization.

---

## What Is Security Through Obscurity?

Hiding functionality instead of protecting it.

---

## What Is The Best Access Control Strategy?

```text
Deny By Default
```

---

# Interview Takeaways

- Authentication ≠ Authorization.
- Every request needs authorization.
- Broken access control is often critical.