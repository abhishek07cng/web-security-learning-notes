# Race Conditions Bug Bounty Checklist

## Reconnaissance

☐ Map the application.

☐ Identify security-critical functionality.

☐ Identify requests that modify shared state.

☐ Identify single-use functionality.

☐ Identify rate-limited functionality.

☐ Identify financial operations.

☐ Identify authentication/account-management workflows.

---

# Collision Analysis

☐ Can multiple requests access the same record?

☐ Can multiple requests use the same session?

☐ Can multiple endpoints modify the same state?

☐ Are there temporary application states?

☐ Is there a check followed by an update?

---

# Potential Targets

☐ Coupons

☐ Gift cards

☐ Checkout

☐ Login

☐ Password reset

☐ Email change

☐ Email verification

☐ Registration

☐ CAPTCHA

☐ Rate limits

☐ Financial transactions

☐ Account changes

---

# Baseline

☐ Send requests sequentially.

☐ Record status codes.

☐ Record response lengths.

☐ Record response timing.

☐ Record application state.

---

# Parallel Testing

☐ Create a Burp Repeater request group.

☐ Duplicate relevant requests.

☐ Send group in parallel.

☐ Compare with sequential behavior.

☐ Check for second-order effects.

---

# Race Window

☐ Identify the check.

☐ Identify the temporary state.

☐ Identify the final update.

☐ Determine where another request could interfere.

---

# Synchronization

☐ Try Burp Repeater parallel requests.

☐ Test connection warming if timing differs.

☐ Use Turbo Intruder when necessary.

☐ Consider HTTP/2 single-packet synchronization where applicable.

---

# Verification

☐ Remove unnecessary requests.

☐ Reduce to minimum required requests.

☐ Repeat the attack.

☐ Confirm reproducibility.

☐ Measure success/failure rate.

---

# Impact

☐ Authentication bypass

☐ Authorization bypass

☐ Account takeover

☐ Rate-limit bypass

☐ Financial impact

☐ Coupon/discount abuse

☐ Sensitive data exposure

☐ Security-control bypass

---

# Reporting

☐ Vulnerable endpoint documented.

☐ Parameters documented.

☐ Race window explained.

☐ Sequential behavior documented.

☐ Concurrent behavior documented.

☐ Reproduction steps documented.

☐ Security impact demonstrated.

☐ Recommended mitigation provided.

---

# Final Question

```text
Can concurrent requests interact with the same
security-sensitive state before it is safely updated?
```

If yes:

```text
Investigate the race condition.
```