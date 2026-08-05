# NoSQL Injection Testing Methodology

## Overview

The objective of NoSQL injection testing is to determine whether user-controlled input can manipulate NoSQL database queries.

The PortSwigger methodology recommends progressing from simple syntax testing to advanced data extraction techniques.

---

# Step 1 – Identify User Input

Locate parameters that are incorporated into database queries.

Common examples include:

- Login forms
- Search functionality
- Category filters
- User lookup features

---

# Step 2 – Test Syntax Injection

Submit fuzz strings and special characters.

Example:

```text
'"`{
;$Foo}
$Foo \xYZ
```

Observe whether the application:

- Returns errors.
- Changes its response.
- Behaves unexpectedly.

---

# Step 3 – Test Individual Characters

Inject characters individually.

Example:

```text
'
```

If a syntax error occurs, attempt an escaped version to confirm that the character affects the query.

---

# Step 4 – Test Boolean Conditions

Compare false and true conditions.

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

# Step 5 – Override Existing Conditions

Inject a condition that always evaluates to true.

Example:

```text
'||'1'=='1
```

This may expose hidden or restricted data.

---

# Step 6 – Test Operator Injection

Submit MongoDB operators such as:

```text
$ne
```

```text
$regex
```

```text
$where
```

Observe whether the application processes the injected operators.

---

# Step 7 – Extract Data

If JavaScript execution is possible:

- Identify field names.
- Determine field lengths.
- Extract values character by character.

---

# Step 8 – Use Timing Techniques

If no visible response differences exist:

- Establish a baseline response time.
- Inject timing payloads.
- Observe delays.

---

# Testing Workflow

```
Identify Input

↓

Syntax Injection

↓

Character Testing

↓

Boolean Conditions

↓

Override Conditions

↓

Operator Injection

↓

Data Extraction

↓

Timing-Based Testing
```

---

# Key Takeaways

- Begin with simple syntax testing.
- Progress methodically toward data extraction.
- Adapt testing based on application responses.