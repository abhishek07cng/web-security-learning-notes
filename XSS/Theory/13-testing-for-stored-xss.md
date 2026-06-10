# Testing For Stored XSS

## Overview

Testing Stored XSS is more difficult than testing Reflected XSS because:

```text
Input Location
≠
Output Location
```

The payload may appear on a completely different page.

---

# Core Idea

Find:

```text
Entry Point
        ↓
Storage
        ↓
Exit Point
```

---

# Step 1 - Find Entry Points

Look for locations where data can be stored.

Examples:

```text
Comments
Usernames
Profile Fields
Reviews
Messages
Support Tickets
```

---

# Step 2 - Submit Probe Value

Example:

```text
XSSTEST123
```

Purpose:

```text
Track Stored Data
```

---

# Step 3 - Browse Application

Search for:

```text
XSSTEST123
```

in:

```text
Pages
Profiles
Admin Panels
Logs
Reports
```

---

# Step 4 - Confirm Data Is Stored

Question:

```text
Does Data Appear Later?
```

---

If yes:

```text
Stored Reflection Found
```

---

# Step 5 - Determine Context

Possible contexts:

```text
HTML
Attribute
JavaScript
URL
```

---

# Step 6 - Test Payload

Simple payload:

```html
<script>alert(1)</script>
```

---

# Step 7 - Verify Execution

Observe:

```text
Alert
Print
DOM Changes
```

---

# Testing Workflow

```text
Find Storage Point
        ↓
Submit Probe
        ↓
Locate Output
        ↓
Determine Context
        ↓
Inject Payload
        ↓
Verify Execution
```

---

# Challenges

## Hidden Exit Points

Payload may appear:

```text
Admin Dashboard
Log Viewer
Email Notification
```

instead of the page where it was submitted.

---

## Temporary Data

Some data:

```text
Expires Quickly
```

before testing completes.

---

## Multiple Display Locations

One payload may appear:

```text
Profile
Comments
Admin Pages
Reports
```

simultaneously.

---

# Personal Revision Note

For Stored XSS always ask:

```text
Where Can Data Be Saved?
```

instead of:

```text
Where Is Data Reflected?
```

---

# Related Lab

- lab02-stored-xss-html-context.md

---

# Key Takeaways

- Stored XSS testing requires patience.
- Entry point and exit point are often different.
- Probe values help locate stored data.
- Context determines exploitability.