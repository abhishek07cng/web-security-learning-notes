# Payload 09 – Parallel Request Template

## Generic Race Structure

Use when two requests interact with the same server-side state.

```text
Request A ─────────┐
                   │
                   ├──→ Collision
                   │
Request B ─────────┘
```

---

## Burp Repeater

Group:

```text
Request A
Request B
```

Then:

```text
Send group in parallel
```

---

## Examples

### Coupon

```text
POST /cart/coupon
POST /cart/coupon
```

### Cart Race

```text
POST /cart
POST /cart/checkout
```

### Email Race

```text
POST /my-account/change-email
POST /my-account/change-email
```

### Password Reset

```text
POST /forgot-password
POST /forgot-password
```

### Registration

```text
POST /register
POST /confirm?token[]=
```

---

## What to Look For

Do not only inspect the immediate HTTP response.

Also check:

```text
Response body
Response length
Status code
Response timing
Email contents
Session state
Cart state
Account state
Database-backed behavior
```

The source emphasizes that second-order effects, such as changed email contents or later application behavior, can reveal a race condition. :contentReference[oaicite:15]{index=15}