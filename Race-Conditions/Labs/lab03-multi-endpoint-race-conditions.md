# Lab 03 – Multi-Endpoint Race Conditions

## Lab Overview

### Objective

Exploit a multi-endpoint race condition in the purchasing flow to purchase a:

```text
Lightweight L33t Leather Jacket
```

Credentials:

```text
Username: wiener
Password: peter
```

The lab requires Burp Suite 2023.9 or higher. :contentReference[oaicite:4]{index=4}

---

# Vulnerability

The relevant functionality uses multiple endpoints that operate on the same server-side cart.

Important endpoints include:

```text
POST /cart
POST /cart/checkout
```

The cart state is associated with the session.

---

# Predict the Collision

1. Log in.
2. Purchase a gift card so you have additional store credit available during testing.
3. Study the cart functionality through Burp Proxy history.

Identify:

```text
POST /cart
```

for adding items.

And:

```text
POST /cart/checkout
```

for submitting the order.

---

# Confirm Shared State

Send:

```text
GET /cart
```

to Repeater.

Compare the response with and without the session cookie.

Without the session cookie, only an empty cart is accessible.

This indicates that the cart state is stored server-side and associated with the session. :contentReference[oaicite:5]{index=5}

---

# Potential Race Window

The order is validated and confirmed within a single request/response cycle.

Potential sequence:

```text
Validate Order
      ↓
Race Window
      ↓
Confirm Order
```

During this window, another request may modify the cart.

---

# Benchmark

Add these requests to a Repeater group:

```text
POST /cart
POST /cart/checkout
```

Send them sequentially over a single connection.

Observe that the first request consistently takes significantly longer than the second.

---

# Connection Warming

Add:

```text
GET /
```

to the beginning of the group.

Send:

```text
GET /
POST /cart
POST /cart/checkout
```

sequentially over a single connection.

The first request may still take longer, but the remaining requests should now complete within a much smaller window.

This indicates that connection setup was contributing to the timing difference. :contentReference[oaicite:6]{index=6}

---

# Prepare the Attack

1. Remove unnecessary requests from the group.
2. Make sure there is a single gift card in the cart.
3. Modify:

```text
POST /cart
```

so that:

```text
productId=1
```

corresponds to the Lightweight L33t Leather Jacket.

---

# Verify Sequential Behavior

Send the requests sequentially.

The order should be rejected because there are insufficient funds.

This establishes the normal behavior. :contentReference[oaicite:7]{index=7}

---

# Prove the Race

1. Remove the jacket.
2. Add another gift card.
3. Send the relevant requests in parallel.

Check the response to:

```text
POST /cart/checkout
```

If the result is:

```text
insufficient funds
```

repeat the attack.

The race may require several attempts.

If the checkout response is successful, verify that the leather jacket was purchased.

---

# Why the Attack Works

The checkout process validates the available store credit before the order is finally confirmed.

A concurrent cart modification can add the expensive jacket after the validation stage but before final confirmation.

Conceptually:

```text
Checkout Request
      │
      ├── Validate balance
      │
      │ ← Race Window
      │
      └── Confirm order

Cart Request
      │
      └── Add jacket
```

---

# Impact

Successful exploitation allows an attacker to purchase an item for an unintended price.

---

# Key Learnings

- Multi-endpoint races require shared application state.
- Identify endpoints that operate on the same record.
- Benchmark before attacking.
- Connection warming can help distinguish backend connection delays from endpoint-specific processing.
- Parallel requests can manipulate state between validation and confirmation.