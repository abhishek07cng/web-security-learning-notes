# Information Disclosure Decision Tree

```
Start
  │
  ▼
Browse Application
  │
  ▼
Unexpected Information?
  │
 ├── No
 │      │
 │      ▼
 │ Continue Testing
 │
 └── Yes
        │
        ▼
Classify Information
        │
        ├── Error Message
        ├── Debug Data
        ├── Source Code
        ├── Configuration
        ├── Version Control
        └── Hidden Resource
                │
                ▼
Sensitive?
        │
      ├── No
      │      │
      │      ▼
      │ Continue Assessment
      │
      └── Yes
             │
             ▼
Can It Enable Another Attack?
             │
       ├── No
       │      │
       │      ▼
       │ Report Information Disclosure
       │
       └── Yes
              │
              ▼
Demonstrate Impact
              │
              ▼
Document Evidence
              │
              ▼
Recommend Mitigation
```

---

# Questions to Ask

- What information has been exposed?
- Is it sensitive?
- Can it be used for further attacks?
- Is additional testing required?
- How should the issue be prioritised?

---

# Common Follow-on Attacks

- Framework fingerprinting
- Authentication bypass
- Credential recovery
- Source code analysis
- Administrative access
- Reconnaissance for additional vulnerabilities