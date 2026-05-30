# CSRF Testing Checklist

## Purpose

Pentesting Checklist

Use during every CSRF assessment.

---

# Initial Assessment

- [ ] Identify state-changing action
- [ ] Confirm cookie-based authentication
- [ ] Check for CSRF token
- [ ] Check SameSite cookies

---

# Token Testing

## Remove Token

- [ ] Remove parameter completely
- [ ] Observe response

---

## Modify Token

- [ ] Change token value
- [ ] Observe response

---

## Change Request Method

- [ ] POST → GET
- [ ] Retest functionality

---

## Session Binding

- [ ] Use token from another account
- [ ] Retest request

---

## Cookie Binding

- [ ] Replace csrfKey
- [ ] Replace csrf cookie
- [ ] Retest request

---

## Double Submit Testing

- [ ] Compare cookie and body token
- [ ] Check server-side state

---

# Browser Protections

- [ ] Check SameSite
- [ ] Check Origin validation
- [ ] Check Referer validation

---

# Final Validation

- [ ] Generate PoC
- [ ] Host exploit
- [ ] Verify attack
- [ ] Deliver exploit

---

# Common Findings

- Method-based validation
- Missing-token validation
- Session-independent tokens
- Cookie-bound tokens
- Double submit flaws