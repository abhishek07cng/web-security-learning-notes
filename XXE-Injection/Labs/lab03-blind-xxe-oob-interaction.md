# Lab 03 – Blind XXE with Out-of-Band Interaction

## Objective

Detect a blind XXE vulnerability using an out-of-band interaction.

---

## Vulnerability

The application processes XML but does not return the value of the external entity in the HTTP response.

Therefore:

```text
Normal XXE
   ↓
No useful response
```

An out-of-band technique is required.

---

## Step 1 — Identify XML Input

Intercept the XML request with Burp Suite.

Send it to:

```text
Burp Repeater
```

---

## Step 2 — Generate an OOB Address

Use:

```text
Burp Collaborator
```

Generate a unique interaction address.

---

## Step 3 — Define External Entity

Conceptual structure:

```xml
<!DOCTYPE foo [
    <!ENTITY xxe SYSTEM "YOUR-COLLABORATOR-ADDRESS">
]>
```

Reference:

```xml
&xxe;
```

inside the XML document.

---

## Step 4 — Send Request

Send the request through Burp Repeater.

The application response may not contain anything useful.

---

## Step 5 — Check Collaborator

Check Burp Collaborator for interactions.

Possible results include:

```text
DNS interaction
HTTP interaction
```

---

## Successful Detection

A recorded interaction indicates:

```text
XML Parser
     ↓
External Entity
     ↓
Collaborator
```

The server attempted to resolve the external entity.

---

## Attack Flow

```text
Malicious XML
      ↓
External Entity
      ↓
OOB Address
      ↓
Server Resolves Entity
      ↓
Collaborator Interaction
```

---

## Why It Works

The entity is processed even though its value is not reflected in the application's HTTP response.

The external interaction therefore provides an alternative observation channel.

---

## Key Learning

Blind XXE can often be detected through out-of-band interaction even when the application does not directly return the entity value.