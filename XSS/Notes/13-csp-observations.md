# CSP Observations

## Observation 1

CSP is:

```text
Defense In Depth
```

not a primary defense.

---

## Observation 2

A weak CSP often provides:

```text
False Sense Of Security
```

---

## Observation 3

Many real-world CSP policies contain:

```http
unsafe-inline
unsafe-eval
```

which significantly weaken protection.

---

## Observation 4

Trusted third-party domains increase attack surface.

---

## Observation 5

CSP can mitigate:

```text
XSS
Clickjacking
Data Exfiltration
```

but not eliminate them.

---

## Observation 6

Policy Injection can completely bypass CSP.

---

## Observation 7

Security headers should never contain:

```text
User Controlled Input
```

---

# Personal Revision Formula

```text
CSP
        ↓
Mitigation
        ↓
Not Prevention
```