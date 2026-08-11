# Blind XXE

## Overview

Blind XXE occurs when the application processes an external entity but does not return the entity's value directly in the application's response.

This makes traditional response-based XXE techniques ineffective.

Instead, the attacker needs to detect the vulnerability indirectly.

---

# Basic Difference

### Normal XXE

```text
Malicious XML
     ↓
External Entity
     ↓
File
     ↓
Application Response
     ↓
Attacker sees data
```

### Blind XXE

```text
Malicious XML
     ↓
External Entity
     ↓
File / URL
     ↓
No useful value in response
```

---

# Why Blind XXE Is Important

An application may still be vulnerable even when:

```text
HTTP Response
      ↓
No file contents
```

are returned.

The XML parser may still be resolving external entities in the background.

---

# Detection

One approach is to define an external entity that references a system controlled by the tester.

Conceptually:

```text
Attacker XML
     ↓
External Entity
     ↓
Controlled Server
     ↓
Interaction observed
```

An out-of-band interaction can confirm that the XML parser processed the external entity.

---

# Common Blind XXE Techniques

Blind XXE can involve:

- Out-of-band interaction.
- Parameter entities.
- External malicious DTDs.
- Error-based data retrieval.
- Local DTD repurposing.

---

# Out-of-Band Detection

A controlled URL can be used as the external entity destination.

The tester monitors the controlled server for:

```text
DNS interaction
HTTP interaction
```

An interaction indicates that the vulnerable application attempted to resolve the external entity.

---

# External DTD

A malicious external DTD can be hosted on a server controlled by the tester.

Conceptually:

```text
XML
 ↓
External DTD
 ↓
Parameter Entity
 ↓
File / URL
```

This provides additional flexibility when a normal internal entity declaration cannot directly return data.

---

# Error-Based Blind XXE

If the application returns XML parser errors, sensitive data may sometimes be caused to appear inside an error message.

Flow:

```text
External Entity
      ↓
Sensitive Data
      ↓
Malformed Resource Reference
      ↓
Parser Error
      ↓
Error Response
```

---

# Detection Workflow

```text
Identify XML Input
       ↓
Test External Entity Processing
       ↓
No Data in Response?
       ↓
Try Out-of-Band Detection
       ↓
If OOB Blocked
       ↓
Consider Error-Based Techniques
       ↓
Investigate Local DTDs
```

---

# Key Takeaways

- Blind XXE does not directly return entity contents.
- Out-of-band interactions are useful for detection.
- External DTDs can provide additional attack capabilities.
- Error messages may sometimes disclose sensitive data.
- Local DTD repurposing can be useful when external OOB interaction is blocked.