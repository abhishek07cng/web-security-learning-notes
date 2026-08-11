# XXE Injection Decision Tree

## Start

```text
                    START
                      │
                      ▼
             Does the application
                process XML?
                /           \
              NO             YES
              │                │
              ▼                ▼
          Move On       Establish Baseline
                               │
                               ▼
                    Can you control XML?
                         /          \
                       NO            YES
                       │              │
                       ▼              ▼
                    Move On      Test DTD / Entity
                                      │
                                      ▼
                          Are external entities
                              processed?
                            /             \
                          NO               YES
                          │                 │
                          ▼                 ▼
                    Test alternative    Test local
                    XML features        file retrieval
                          │                 │
                          │                 ▼
                          │             Response
                          │             contains data?
                          │              /      \
                          │            YES       NO
                          │             │          │
                          │             ▼          ▼
                          │        Response-    Test SSRF /
                          │        based XXE    Blind XXE
                          │
                          ▼
                    Is XInclude supported?
                         /       \
                       NO         YES
                       │           │
                       ▼           ▼
                    Check       Test XInclude
                    uploads
```

---

# Response-Based XXE Decision

```text
External Entity
      │
      ▼
Local Resource
      │
      ▼
Does response contain resource?
      │
   ┌──┴──┐
  YES    NO
   │      │
   ▼      ▼
Confirm  Blind XXE
impact      │
            ▼
       Test OOB
```

---

# Blind XXE Decision

```text
Blind XXE
    │
    ▼
Can server make outbound requests?
    │
 ┌──┴──┐
YES    NO
 │      │
 ▼      ▼
OOB    Test parser
       errors
         │
         ▼
    Detailed errors?
       /       \
     YES        NO
      │          │
      ▼          ▼
 Error-Based   Check Local
 XXE           DTD / XInclude
```

---

# External DTD Decision

```text
Need complex DTD behavior?
        │
       YES
        │
        ▼
Can target retrieve external DTD?
      /       \
    YES        NO
     │          │
     ▼          ▼
External      Investigate
DTD           local DTD
     │          │
     ▼          ▼
Parameter     Existing
Entities      Entity
     │          │
     ▼          ▼
OOB / Error   Repurposing
```

---

# File Upload Decision

```text
File Upload
     │
     ▼
Does application accept XML-based formats?
     │
   ┌─┴─┐
  NO   YES
  │     │
  ▼     ▼
Move   Does application parse
On     uploaded content?
          │
        ┌─┴─┐
       NO   YES
       │     │
       ▼     ▼
     Move   Test XML parser
     On        │
               ▼
          External entities?
             /       \
           NO         YES
           │           │
           ▼           ▼
        Check       XXE testing
        XInclude
```

---

# XInclude Decision

```text
DOCTYPE / External Entity blocked
             │
             ▼
       Is XInclude enabled?
          /         \
        NO           YES
        │             │
        ▼             ▼
    Move On      Test XInclude
                      │
                      ▼
              External resource
                accessible?
                 /      \
               NO        YES
               │          │
               ▼          ▼
            Move On   Confirm impact
```

---

# Impact Decision

```text
XXE Confirmed
      │
      ▼
What can the parser access?
      │
 ┌────┼───────────┐
 │    │           │
 ▼    ▼           ▼
File URL       Other Resource
 │    │           │
 ▼    ▼           ▼
LFD  SSRF       Assess Impact
```

Where:

```text
LFD = Local File Disclosure
SSRF = Server-Side Request Forgery
```

---

# Final Testing Flow

```text
IDENTIFY
   ↓
XML Processing
   ↓
BASELINE
   ↓
External Entity
   ↓
┌───────────────┐
│ Response Data?│
└───────┬───────┘
        │
   ┌────┴────┐
  YES       NO
   │          │
   ▼          ▼
File /      OOB
SSRF        / Error
   │          │
   └────┬─────┘
        ▼
   Alternative
   XML Features
        │
        ▼
XInclude / Upload
        │
        ▼
     CONFIRM
        │
        ▼
     IMPACT
        │
        ▼
      REPORT
```