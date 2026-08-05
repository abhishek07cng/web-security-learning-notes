# NoSQL Injection Testing Methodology

## Objective

Determine whether user-controlled input can manipulate NoSQL database queries and ultimately extract sensitive information or bypass application security controls.

---

# Phase 1 – Identify User Input

Locate application functionality that interacts with the database.

Common targets include:

- Login forms
- Search functionality
- Category filters
- User lookup endpoints

---

# Phase 2 – Test Syntax Injection

Submit fuzz strings and special characters.

Example:

```text
'"`{
;$Foo}
$Foo \xYZ
```

Observe whether the application:

- Returns errors
- Behaves differently
- Generates unexpected responses

---

# Phase 3 – Confirm Injection

Compare boolean conditions.

False:

```text
' && 0 && 'x
```

True:

```text
' && 1 && 'x
```

Different responses indicate successful query manipulation.

---

# Phase 4 – Override Existing Conditions

Inject an always-true condition.

```text
'||'1'=='1
```

Determine whether hidden or restricted data becomes visible.

---

# Phase 5 – Test Operator Injection

Attempt MongoDB operators such as:

```text
$where
```

```text
$ne
```

```text
$regex
```

```text
$in
```

Observe whether the application processes them.

---

# Phase 6 – Extract Data

If JavaScript execution is available:

- Identify field names.
- Determine field lengths.
- Extract values character by character.

---

# Phase 7 – Timing-Based Testing

If no visible responses exist:

- Establish a response-time baseline.
- Inject timing payloads.
- Observe measurable delays.

---

# Workflow

```
Identify Input

↓

Syntax Injection

↓

Boolean Testing

↓

Override Conditions

↓

Operator Injection

↓

Data Extraction

↓

Timing Testing

↓

Assess Impact
```

---

# Key Takeaways

- Progress from simple testing to advanced extraction.
- Confirm every stage before moving to the next.
- Adapt payloads based on application responses.