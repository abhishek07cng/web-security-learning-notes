# API Decision Tree

API Found?

│
├── No
│
│      └── Continue Recon
│
└── Yes

       │
       ├── Documentation Available?
       │
       │       └── Enumerate Endpoints
       │
       ├── Methods Supported?
       │
       │       └── OPTIONS Testing
       │
       ├── JSON Objects?
       │
       │       └── Mass Assignment
       │
       ├── Hidden Parameters?
       │
       │       └── Parameter Discovery
       │
       ├── Internal Requests?
       │
       │       └── SSPP
       │
       ├── REST Paths?
       │
       │       └── Path Manipulation
       │
       ├── Query Strings?
       │
       │       └── Parameter Injection
       │
       └── Impact?
               │
               ├── Information Disclosure
               ├── Privilege Escalation
               └── Account Takeover