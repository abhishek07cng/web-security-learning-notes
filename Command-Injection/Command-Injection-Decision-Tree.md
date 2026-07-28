# Command Injection Decision Tree

```
                    User Input
                         │
                         ▼
            Does the response contain
               injected command output?
                  /               \
                Yes               No
                 │                 │
                 ▼                 ▼
      Visible Command      Blind Command
         Injection           Injection
                 │                 │
                 ▼                 ▼
         Confirm Issue      Test Time Delay
                                   │
                        Delay Observed?
                           /      \
                         Yes      No
                          │        │
                          ▼        ▼
                 Confirm Issue  Test Output
                                Redirection
                                     │
                          Output Retrieved?
                             /        \
                           Yes        No
                            │          │
                            ▼          ▼
                    Confirm Issue   Test OAST
                                        │
                              DNS Interaction?
                                 /        \
                               Yes        No
                                │          │
                                ▼          ▼
                        Confirm Issue  Test Data
                                     Exfiltration
                                          │
                                 Output Recovered?
                                    /          \
                                  Yes          No
                                   │            │
                                   ▼            ▼
                           Confirm Issue   Continue
                                           Investigation
```

---

# Workflow Summary

1. Test visible output.
2. If blind, test time delays.
3. Try output redirection.
4. Use Burp Collaborator.
5. Attempt out-of-band data exfiltration.
6. Gather system information.
7. Report the findings.