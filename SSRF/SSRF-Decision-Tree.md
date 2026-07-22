# SSRF Decision Tree

```
Identify URL-Fetching Feature
            │
            ▼
     Does the server make
      a backend request?
            │
     ┌──────┴──────┐
     │             │
    No            Yes
     │             │
     ▼             ▼
 Not SSRF     Test Localhost
                    │
          ┌─────────┴─────────┐
          │                   │
        Blocked            Accessible
          │                   │
          ▼                   ▼
 Test Bypass Methods     Check Admin Panel
          │                   │
          ▼                   ▼
 Alternative IPs        Sensitive Access?
 URL Encoding                │
 Double Encoding             │
 Open Redirect               ▼
          │            High / Critical
          ▼
 Still Blocked?
          │
     ┌────┴────┐
     │         │
    Yes       No
     │         │
     ▼         ▼
 Test Blind   Test Internal
   SSRF         Network
     │             │
     ▼             ▼
 Burp Collaborator
     │
     ▼
 DNS / HTTP
 Interaction?
     │
     ▼
 Blind SSRF Confirmed
```