# Insecure Deserialization Decision Tree

```text
Serialized-looking input?
        |
       Yes
        ↓
Identify format
        |
        +-- PHP → inspect unserialize()/object structure
        |
        +-- Java → inspect rO0/ac ed/readObject()
        |
        +-- Ruby → inspect Marshal data
        ↓
Can object attributes be controlled?
        |
       Yes
        ↓
Test attribute modification
        |
        +-- privilege/session logic
        +-- dangerous functionality
        +-- type manipulation
        ↓
Can object class be controlled?
        |
       Yes
        ↓
Inspect arbitrary object injection
        ↓
Source code available?
        |
       Yes
        ↓
Find magic methods
        ↓
Trace data flow
        ↓
Find sink gadget
        ↓
Construct gadget chain
        |
        +-- pre-built chain available?
        |       ↓
        |    test compatible chain
        |
        +-- no
                ↓
             build custom chain
        ↓
Blind behavior?
        |
       Yes
        ↓
Consider OAST detection
```
