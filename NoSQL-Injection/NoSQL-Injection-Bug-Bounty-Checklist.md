# NoSQL Injection Bug Bounty Checklist

## Reconnaissance

☐ Identify user-controlled parameters.

☐ Determine whether the application uses MongoDB.

☐ Intercept requests using Burp Suite.

---

## Syntax Testing

☐ Submit fuzz strings.

☐ Test individual special characters.

☐ Compare normal and escaped input.

---

## Boolean Testing

☐ False condition.

☐ True condition.

☐ Always-true condition.

---

## Operator Testing

☐ Test `$ne`.

☐ Test `$regex`.

☐ Test `$where`.

☐ Test `$in`.

---

## Authentication Testing

☐ Attempt login bypass.

☐ Target privileged accounts.

---

## Data Extraction

☐ Determine field names.

☐ Determine password length.

☐ Extract values character by character.

---

## Timing Testing

☐ Establish response baseline.

☐ Inject timing payloads.

☐ Observe response delays.

---

## Reporting

Include:

- Vulnerable endpoint
- Vulnerable parameter
- Payload used
- Proof of exploitation
- Impact
- Recommended mitigation

---

# Final Checklist

☐ Vulnerability confirmed.

☐ Evidence collected.

☐ Impact assessed.

☐ Report completed.