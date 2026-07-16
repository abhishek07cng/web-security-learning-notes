# JWT Claims Tampering

## Interesting Claims

```text
sub
role
isAdmin
permissions
groups
scope
userid
username
```

---

## Testing Methodology

Observe:

```text
Current User
```

↓

Identify:

```text
Identity Claims
```

↓

Modify:

```text
Role

Privileges

Identifiers
```

↓

Observe Server Response

---

## Indicators

```text
JWT Authentication

Authorization Decisions Based On Claims

Privilege Information Stored In JWT
```

---

# Key Learnings

Claims are attacker-controlled until the server successfully verifies the JWT.