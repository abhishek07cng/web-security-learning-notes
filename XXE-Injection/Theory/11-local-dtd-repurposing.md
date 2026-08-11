# Local DTD Repurposing

## Overview

Local DTD repurposing is an advanced blind XXE technique.

It is useful in situations where:

- External DTD retrieval is blocked.
- Out-of-band interactions are unavailable.
- The application has access to a local DTD.
- The XML parser supports DTD processing.

---

# The Core Idea

Many operating systems and applications contain local DTD files.

If the XML parser can access one of these files, an attacker may attempt to reuse an existing entity declaration from that DTD.

Conceptually:

```text
Local DTD
   ↓
Existing Entity
   ↓
Repurpose Entity
   ↓
Trigger XML Parser Behavior
```

---

# Why Local DTDs Matter

A local DTD can provide declarations that already exist on the server.

This can sometimes bypass the requirement for hosting an external malicious DTD.

---

# General Flow

```text
Attacker XML
      ↓
Reference Local DTD
      ↓
Reuse Existing Declaration
      ↓
Modify / Extend Behavior
      ↓
Trigger Error or Other Channel
      ↓
Observe Result
```

---

# When to Consider This Technique

Consider local DTD repurposing when:

```text
External DTD
     ↓
Blocked
```

and:

```text
OOB interaction
     ↓
Unavailable
```

but:

```text
Local DTD
     ↓
Accessible
```

---

# Finding Candidate DTDs

The source material describes using operating-system DTD files that are commonly present on the target system.

The exact file and entity names depend on:

- Operating system.
- Installed software.
- XML libraries.
- Application environment.

Therefore, local DTD repurposing is environment-specific.

---

# Entity Collision

A local DTD may already define an entity.

The attacker can attempt to reference the same entity in a way that causes useful parser behavior.

Conceptually:

```text
Existing Entity
       +
Attacker Declaration
       ↓
Entity Collision
       ↓
Modified Parsing Behavior
```

---

# Error-Based Usage

Local DTD repurposing is commonly associated with error-based blind XXE.

The general concept is:

```text
Local DTD
    ↓
Existing Entity
    ↓
Repurposed Entity
    ↓
Parser Error
    ↓
Information Disclosure
```

---

# Limitations

This technique depends heavily on the environment.

Important factors include:

- Which DTD files exist.
- Whether the application can access them.
- Parser configuration.
- Entity behavior.
- Whether parameter entities are supported.
- Whether useful parser errors are returned.

---

# Testing Workflow

```text
Identify Blind XXE
       ↓
Test OOB Interaction
       ↓
External DTD Blocked?
       ↓
Identify Local DTD
       ↓
Check Available Entities
       ↓
Test Entity Repurposing
       ↓
Observe Parser Behavior
       ↓
Determine Impact
```

---

# Key Takeaways

- Local DTD repurposing is an advanced blind XXE technique.
- It can be useful when external DTDs cannot be retrieved.
- The technique depends on DTD files already present on the target.
- Existing entity declarations can potentially be reused.
- Environment and parser behavior determine whether the technique works.