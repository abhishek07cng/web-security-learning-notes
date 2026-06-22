# Business Logic Methodology

## Step 1 - Understand The Application

Ask:

```text
What Problem Is This Feature Solving?
```

Examples:

```text
Checkout
Coupons
Gift Cards
2FA
Password Reset
Wallets
Invitations
```

---

## Step 2 - Identify Business Rules

Questions:

```text
What Is Supposed To Happen?
What Assumptions Exist?
```

---

## Step 3 - Look For User-Controlled Data

Check:

```text
Prices
Coupons
Discounts
Quantities
Roles
Email Addresses
```

---

## Step 4 - Break Assumptions

Try:

```text
Negative Values
Large Values
Missing Parameters
Duplicate Parameters
```

---

## Step 5 - Break Workflow

Ask:

```text
Can I Skip Steps?
Can I Replay Requests?
Can I Reach The Final Step Directly?
```

---

## Step 6 - Abuse State Machines

Questions:

```text
When Is Session Created?
When Is User Authenticated?
```

---

## Step 7 - Test Financial Logic

Check:

```text
Coupons
Wallets
Gift Cards
Reward Points
```

Ask:

```text
Can Value Be Created?
```

---

## Step 8 - Assess Impact

```text
Authentication Bypass
Account Takeover
Financial Fraud
Privilege Escalation
```

---

# Personal Formula

```text
Understand Rules
        ↓
Find Assumptions
        ↓
Break Assumptions
        ↓
Unexpected State
        ↓
Impact
```