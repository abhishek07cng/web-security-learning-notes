# Error-Based XXE

## Overview

Error-based XXE is a technique for extracting information from a vulnerable XML parser through error messages.

It is particularly useful in situations where:

- The application does not return the value of an external entity.
- Out-of-band interaction is unavailable.
- The application exposes detailed XML parser errors.

---

# Basic Concept

The general flow is:

```text
External Entity
      ↓
Sensitive Data
      ↓
Malformed / Invalid Resource
      ↓
XML Parser Error
      ↓
Error Message
      ↓
Sensitive Data Disclosed
```

---

# Why Errors Matter

A vulnerable application may not directly reflect an entity value.

For example:

```text
Entity → File
          ↓
      No Response Data
```

However, if the parser generates an error containing information derived from the entity, the application may accidentally disclose the data.

---

# Error-Based XXE Flow

```text
Attacker XML
     ↓
Parameter / External Entity
     ↓
Read Sensitive Resource
     ↓
Trigger Parser Error
     ↓
Application Returns Error
     ↓
Extract Information
```

---

# Role of External DTDs

External DTDs can be useful when constructing complex error-based XXE payloads.

Conceptually:

```text
Main XML
   ↓
External DTD
   ↓
Entity Definitions
   ↓
Sensitive Data
   ↓
Parser Error
```

The external DTD can contain entity declarations that are difficult or impossible to construct directly inside the original XML document.

---

# Error Messages

Useful error messages may reveal:

- File paths.
- Entity values.
- Parser state.
- XML syntax information.
- Referenced resources.
- Internal application information.

---

# Testing Workflow

### Step 1

Identify an XML-processing endpoint.

### Step 2

Determine whether external entities are processed.

### Step 3

Check whether detailed XML parser errors are returned.

### Step 4

Investigate whether an external DTD can be processed.

### Step 5

Observe whether parser errors reveal information derived from the entity.

---

# Error-Based vs Response-Based XXE

### Response-Based

```text
Entity
 ↓
File
 ↓
Normal XML Response
```

### Error-Based

```text
Entity
 ↓
File
 ↓
Parser Error
 ↓
Error Response
```

---

# Error-Based vs Blind XXE

Both can be useful when the application does not directly return entity contents.

```text
Blind XXE
   ↓
Indirect observation

Error-Based XXE
   ↓
Parser error
   ↓
Information disclosure
```

---

# Important Consideration

Detailed error messages significantly increase the attack surface of XML parsers.

Production applications should avoid exposing unnecessary parser errors to untrusted users.

---

# Key Takeaways

- Error-based XXE uses parser errors as an information channel.
- It is useful when direct entity reflection is unavailable.
- External DTDs can help construct advanced payloads.
- Detailed parser errors may disclose sensitive information.
- Error messages should not expose unnecessary internal information.