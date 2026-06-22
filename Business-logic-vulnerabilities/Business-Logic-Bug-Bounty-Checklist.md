# Business Logic Bug Bounty Checklist

## Client-Side Trust

- [ ] Prices
- [ ] Quantity
- [ ] Discount
- [ ] Role
- [ ] Hidden Fields

---

## Unconventional Input

- [ ] Negative Values
- [ ] Zero
- [ ] Large Numbers
- [ ] Empty Values

---

## Parameters

- [ ] Remove Parameters
- [ ] Duplicate Parameters
- [ ] Empty Parameters

---

## Workflow

- [ ] Skip Steps
- [ ] Replay Requests
- [ ] Call Final Request Directly

---

## Authentication

- [ ] Session State
- [ ] Password Reset
- [ ] 2FA

---

## Financial Logic

- [ ] Coupons
- [ ] Gift Cards
- [ ] Wallets
- [ ] Reward Points

---

## Parser Issues

- [ ] Email Parsing
- [ ] Encoding
- [ ] Validation Differences

---

## Encryption Oracles

- [ ] Response Length
- [ ] Error Messages
- [ ] Status Codes

---

## Impact

- [ ] Authentication Bypass
- [ ] Account Takeover
- [ ] Financial Abuse
- [ ] Privilege Escalation