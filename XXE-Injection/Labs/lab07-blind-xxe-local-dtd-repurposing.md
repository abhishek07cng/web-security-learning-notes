# Lab 07 – Blind XXE with Local DTD Repurposing

## Objective

Exploit a blind XXE vulnerability when the application blocks the use of an external DTD.

The technique involves repurposing an existing local DTD on the server.

---

# Vulnerability

The application processes XML and allows DTD-related functionality, but direct external DTD loading is restricted.

A local DTD may already exist on the server.

The attack attempts to:

```text
XML
 ↓
Local DTD
 ↓
Existing Entity
 ↓
Repurposed Entity
 ↓
Parser Error / Information Disclosure
```

---

# Step 1 — Identify Blind XXE

First establish that:

```text
XML input
+
DTD processing
```

are supported.

Determine whether normal external DTD retrieval is blocked.

---

# Step 2 — Identify a Local DTD

The target environment may contain DTD files supplied by:

- Operating-system components.
- Installed software.
- XML libraries.
- Application dependencies.

The exact DTD location is environment-dependent.

---

# Step 3 — Identify Existing Entity Definitions

Inspect the available local DTD for entity declarations.

Conceptually:

```text
Local DTD
   ↓
Entity Declaration
   ↓
Existing Entity
```

The goal is to find an entity whose declaration can be influenced or reused.

---

# Step 4 — Repurpose the Entity

Construct the XML so that the local DTD is loaded and an existing declaration is used in an unintended way.

Conceptually:

```text
Local DTD
     +
Attacker Declaration
     ↓
Entity Collision
     ↓
Modified Parsing Behavior
```

---

# Step 5 — Trigger an Error

If the application returns detailed parser errors, use the modified entity behavior to trigger an error.

The resulting error may contain information derived from a local resource.

---

# Attack Flow

```text
Attacker XML
      ↓
Local DTD
      ↓
Existing Entity
      ↓
Entity Repurposing
      ↓
Parser Error
      ↓
Information Disclosure
```

---

# Why This Technique Is Useful

External DTD techniques require:

```text
Target → External DTD
```

If outbound access is restricted, that may fail.

Local DTD repurposing instead uses:

```text
Target → Local DTD
```

which can bypass the need for external DTD retrieval.

---

# Limitations

The technique depends on:

- A suitable local DTD existing.
- The XML parser being able to access it.
- Useful entity declarations being present.
- Parameter-entity behavior.
- Parser error behavior.

---

# Testing Workflow

```text
Blind XXE
   ↓
External DTD Blocked?
   ↓
YES
   ↓
Identify Local DTD
   ↓
Find Useful Entity
   ↓
Attempt Repurposing
   ↓
Trigger Parser Behavior
   ↓
Inspect Response
```

---

# Key Learning

Local DTD repurposing is an advanced technique for blind XXE when conventional external-DTD and OOB approaches are unavailable.