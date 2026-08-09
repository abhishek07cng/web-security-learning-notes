# Payload 02 – Rate Limit Race Condition

## Target

```http
POST /login
```

---

## Basic Request

```http
POST /login HTTP/2
Host: YOUR-LAB-ID.web-security-academy.net
Content-Type: application/x-www-form-urlencoded

username=carlos&password=PASSWORD
```

---

## Race Strategy

Normally:

```text
Attempt 1 → Counter = 1
Attempt 2 → Counter = 2
Attempt 3 → Counter = 3
Attempt 4 → LOCKED
```

Race condition:

```text
Attempt 1 ─┐
Attempt 2 ─┤
Attempt 3 ─┤
Attempt 4 ─┤──→ processed before counter update
Attempt 5 ─┤
Attempt 6 ─┘
```

This can allow more login attempts than the intended limit.

---

## Burp Repeater

Create approximately 20 copies of the login request.

First test:

```text
Send group in sequence
```

Then:

```text
Send group in parallel
```

The source notes that parallel requests can result in more than three requests receiving the normal invalid-login response despite the account lock being triggered. :contentReference[oaicite:2]{index=2}

---

## Turbo Intruder

Send the login request to:

```text
Extensions
→ Turbo Intruder
```

Use the supplied password list from the lab.

The goal is to make the password attempts collide within the rate-limit race window.

---

## Important Observation

Test whether the rate limit is:

```text
Per session
Per username
Per IP
```

In this lab, the behavior indicates that the limit is associated with the username. :contentReference[oaicite:3]{index=3}