# Preventing Business Logic Vulnerabilities

## Principle 1

Understand The Business Domain

Developers and testers should understand:

```text
Business Rules
Workflows
Security Requirements
```

---

## Principle 2

Avoid Assumptions

Never assume:

```text
Users Behave Normally
Clients Are Trusted
Parameters Always Exist
Steps Are Followed
```

---

## Principle 3

Perform Server-Side Validation

Validate:

```text
Input Values
Workflow State
Authorization
```

---

## Principle 4

Document Assumptions

Maintain:

```text
Design Documents
Workflow Diagrams
Data Flows
```

---

## Principle 5

Understand Dependencies

Ask:

```text
How Components Interact
What Side Effects Exist
```

---

## Principle 6

Write Clear Code

Clear code reduces:

```text
Complexity
Misunderstandings
Hidden Assumptions
```

---

# Defense Formula

```text
Understand Domain
        ↓
Document Assumptions
        ↓
Validate State
        ↓
Enforce Rules
```

---

# Key Takeaways

Most logic flaws originate during design rather than implementation.