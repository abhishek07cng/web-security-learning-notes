# Fuzzing Checklist

## Goal

Trigger unexpected application behaviour that reveals useful information.

---

## Test Invalid Values

```
abc

"

'

NULL

-1

999999999
```

---

## Missing Values

```
parameter=

parameter

(empty value)
```

---

## Unexpected Data Types

```
String instead of Integer

Integer instead of String

Boolean

Special Characters
```

---

## Compare Responses

Look for differences in:

- Status Code
- Response Length
- Response Time
- Error Message
- Stack Trace

---

## Burp Intruder Workflow

```
Request

↓

Mark Payload Position

↓

Add Test Inputs

↓

Send Requests

↓

Compare Responses
```

---

## Indicators of Information Disclosure

- Framework version
- File path
- SQL error
- Stack trace
- Configuration details
- Internal server information