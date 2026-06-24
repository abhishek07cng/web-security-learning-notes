# API Quick Revision

## Recon Sources

```text
JavaScript
Swagger
OpenAPI
Proxy History
```

---

## Common Methods

```text
GET
POST
PUT
PATCH
DELETE
OPTIONS
```

---

## Common Content Types

```text
application/json
application/xml
multipart/form-data
application/x-www-form-urlencoded
```

---

## Hidden Parameters

Examples:

```text
isAdmin
role
discount
price
```

---

## Mass Assignment

```text
Hidden Property
        ↓
Automatic Binding
        ↓
Privilege Escalation
```

---

## SSPP Query Strings

Characters:

```text
&
#
=
?
```

---

## SSPP REST Paths

Test:

```text
../
../../
```

---

## Severity Ladder

```text
Information Disclosure
        ↓
Privilege Escalation
        ↓
Account Takeover
```

---

# Top Lessons From PortSwigger

1. Documentation exposes attack surface.

2. OPTIONS reveals hidden methods.

3. Hidden properties are dangerous.

4. APIs often trust user input too much.

5. Internal APIs are common attack targets.

6. JSON increases attack surface.

7. Ask:

```text
What Does The Backend Know
That The Frontend Doesn't Show?
```

---

# Personal API Formula

```text
Endpoint
        ↓
Method
        ↓
Parameters
        ↓
Hidden Functionality
        ↓
Impact
```