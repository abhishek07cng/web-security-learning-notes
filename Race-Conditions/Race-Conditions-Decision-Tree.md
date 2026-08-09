# Race Conditions Decision Tree

```text
                    START
                      │
                      ▼
             Map Application
                      │
                      ▼
       Is there security-critical functionality?
                 /           \
               NO             YES
               │               │
               ▼               ▼
          Lower Priority   Identify Shared State
                                │
                                ▼
                    Can multiple requests
                    access the same state?
                         /          \
                       NO            YES
                       │              │
                       ▼              ▼
                  Move On       Identify State
                                      │
                                      ▼
                         Is there a temporary state?
                              /            \
                            NO              YES
                            │                │
                            ▼                ▼
                       Look for        Identify Race
                       other targets      Window
                                           │
                                           ▼
                                  Establish Baseline
                                           │
                                           ▼
                                  Sequential Requests
                                           │
                                           ▼
                                  Parallel Requests
                                           │
                                           ▼
                              Any unexpected behavior?
                                  /            \
                                NO              YES
                                │                │
                                ▼                ▼
                           Try another       Investigate
                           candidate            │
                                               ▼
                                     Reduce unnecessary
                                          requests
                                               │
                                               ▼
                                         Reproduce
                                               │
                                               ▼
                                     Security impact?
                                      /          \
                                    NO            YES
                                    │              │
                                    ▼              ▼
                              Document as      Confirm & Report
                              non-exploitable
```

---

# Race Type Identification

```text
Multiple requests exceed a limit?
        │
        └── YES → LIMIT OVERRUN

Check followed by use/update?
        │
        └── YES → TOCTOU

Different endpoints share state?
        │
        └── YES → MULTI-ENDPOINT RACE

Same endpoint + different inputs?
        │
        └── YES → SINGLE-ENDPOINT RACE

Object temporarily exists before completion?
        │
        └── YES → PARTIAL CONSTRUCTION RACE
```

---

# Synchronization Decision

```text
Can Repeater reproduce it?
        │
      YES
        │
        ▼
Use Repeater
        │
        ▼
Need many requests/custom timing?
        │
      YES
        │
        ▼
Use Turbo Intruder
        │
        ▼
Very small race window?
        │
      YES
        │
        ▼
Consider HTTP/2
single-packet synchronization
```

---

# Core Method

```text
PREDICT
   ↓
PROBE
   ↓
PROVE
```