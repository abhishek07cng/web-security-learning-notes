# NoSQL Injection Decision Tree

```
             User Input
                  │
                  ▼
       Test Syntax Injection
                  │
          Syntax Error?
          /          \
        Yes          No
         │            │
         ▼            ▼
 Confirm Injection  Test Boolean
                    Conditions
                         │
                 Different Responses?
                    /           \
                  Yes           No
                   │             │
                   ▼             ▼
          Override Conditions  Test Operators
                                    │
                           $ne / $regex / $where
                                    │
                           Operator Accepted?
                             /            \
                           Yes            No
                            │              │
                            ▼              ▼
                 Authentication Bypass  Timing Test
                            │
                            ▼
                    Extract Sensitive Data
                            │
                            ▼
                     Enumerate Fields
                            │
                            ▼
                    Report Vulnerability
```

---

# Workflow Summary

1. Test syntax injection.
2. Confirm boolean behavior.
3. Override existing conditions.
4. Test MongoDB operators.
5. Attempt authentication bypass.
6. Extract sensitive data.
7. Report findings.