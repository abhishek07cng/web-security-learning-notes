# Lab 01 – Limit Overrun Race Conditions

## Lab Overview

### Objective

Exploit a race condition in the purchasing flow to purchase a:

```text
Lightweight L33t Leather Jacket
```

The lab uses a race condition that allows an unintended purchase price.

Credentials:

```text
Username: wiener
Password: peter
```

---

# Vulnerability

The application contains a limit-overrun race condition in its coupon functionality.

The discount code is intended to be applied only once.

Normally:

```text
Check coupon
      ↓
Apply discount
      ↓
Mark coupon as used
```

A race condition exists because multiple requests can enter the temporary state before the application records that the coupon has already been used.

---

# Predict the Collision

1. Log in using:

```text
wiener:peter
```

2. Add an arbitrary item to the cart.

3. Apply the available discount code.

4. Send the coupon request to Burp Repeater.

5. Create a request group containing multiple copies of:

```text
POST /cart/coupon
```

---

# Benchmark the Behavior

Send the requests sequentially.

Expected behavior:

```text
First request  → Discount applied
Other requests → Coupon already applied
```

This establishes the normal behavior.

---

# Probe for Race Condition

Remove the discount code from the cart.

Send the grouped coupon requests in parallel.

Use:

```text
Send group in parallel
```

Observe the responses.

A successful race condition may cause multiple requests to report that the coupon was successfully applied.

---

# Verify the Overrun

Refresh the cart.

Check whether the discount has been applied more than once.

The source describes the expected result as a repeated:

```text
20% reduction
```

This confirms that the same single-use coupon has been processed multiple times. :contentReference[oaicite:1]{index=1}

---

# Prove the Concept

1. Remove the previously applied codes.
2. Remove the arbitrary item.
3. Add the:

```text
Lightweight L33t Leather Jacket
```

4. Send the grouped:

```text
POST /cart/coupon
```

requests in parallel.

5. Refresh the cart.

6. Check the final order total.

If the discounted price is within the remaining store credit, purchase the jacket.

---

# Race Window

The vulnerable sequence is approximately:

```text
Check coupon
      ↓
Race Window
      ↓
Apply discount
      ↓
Mark coupon as used
```

Multiple requests can pass the check before the database state is updated.

---

# Why the Attack Works

The application does not make the check-and-update operation atomic.

Multiple concurrent requests can therefore observe the coupon as unused.

Each request can then apply the discount.

---

# Impact

A successful attack can allow an attacker to:

- Reuse single-use discounts.
- Manipulate order prices.
- Purchase expensive items for an unintended price.

---

# Key Learnings

- Limit overruns are a classic race-condition category.
- Sequential testing establishes the baseline.
- Parallel testing exposes concurrent state changes.
- Multiple successful responses are an important clue.
- Always prove the business impact after identifying the race.