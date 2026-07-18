# OAuth Decision Tree

```
OAuth Detected
        │
        ▼
Capture Authorization Request
        │
        ▼
Identify Flow
        │
 ┌──────┴─────────┐
 │                │
 ▼                ▼
Code Flow     Implicit Flow
 │                │
 ▼                ▼
Test           Check Token
redirect_uri   Leakage
 │                │
 ▼                ▼
Check state   Inspect JS
 │                │
 ▼                ▼
Check PKCE    postMessage
 │                │
 ▼                ▼
Inspect Callback
        │
        ▼
Test Resource Server
        │
        ▼
Report Findings
```