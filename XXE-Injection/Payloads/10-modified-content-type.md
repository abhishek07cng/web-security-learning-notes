# Payload 10 – Modified Content-Type XXE

## Purpose

Test whether an endpoint continues to process XML when the declared request Content-Type is changed.

---

## Normal Request

Example:

```http
POST /endpoint HTTP/1.1
Content-Type: application/xml
```

Body:

```xml
<?xml version="1.0"?>
<root>
    <value>test</value>
</root>
```

---

## Test Variant

Change the Content-Type and observe whether the application still processes the XML body.

For example:

```http
Content-Type: application/x-www-form-urlencoded
```

The exact request format depends on the application.

---

## Testing Concept

```text
Normal XML Request
        ↓
Change Content-Type
        ↓
Send XML Data
        ↓
Does XML Still Get Parsed?
```

---

## XXE Test

If the application continues to parse the body as XML, investigate whether external entities are also processed.

Conceptually:

```xml
<?xml version="1.0"?>

<!DOCTYPE foo [
    <!ENTITY xxe SYSTEM "RESOURCE">
]>

<foo>
    &xxe;
</foo>
```

---

## Burp Repeater Workflow

```text
Intercept Request
      ↓
Send to Repeater
      ↓
Record Normal Behavior
      ↓
Change Content-Type
      ↓
Send Request
      ↓
Compare Response
      ↓
Check XML Processing
      ↓
Test XXE Behavior
```

---

## Indicators

Look for:

```text
XML parser errors
Same XML response
XML-specific validation
Unexpected entity processing
OOB interaction
```

---

## Important

Changing the Content-Type alone does not create an XXE vulnerability.

The application must still:

```text
Accept the request
       +
Process the body as XML
       +
Allow unsafe XML functionality
```

---

## Key Learning

The declared Content-Type should not be treated as the only indicator of whether an application processes XML. Testing should focus on the application's actual parsing behavior.