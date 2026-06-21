# File Upload Decision Tree

Upload Feature Found?

│
├── No
│
│      └── Continue Recon
│
└── Yes

       │
       ├── Extension Validation Present?
       │
       │       └── Try Extension Bypass
       │
       ├── Content-Type Validation?
       │
       │       └── MIME Spoofing
       │
       ├── Magic Byte Validation?
       │
       │       └── Polyglot Files
       │
       ├── Upload Accessible?
       │
       │       └── Test Execution
       │
       ├── Execution Disabled?
       │
       │       └── Path Traversal
       │
       ├── Virus Scan Present?
       │
       │       └── Race Condition
       │
       ├── PUT Enabled?
       │
       │       └── Arbitrary Upload
       │
       └── Impact?
               │
               ├── Stored XSS
               ├── Information Disclosure
               ├── File Overwrite
               └── RCE