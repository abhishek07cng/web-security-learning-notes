# Access Control Decision Tree

Sensitive Function Found?

│
├── No
│
│     └── Continue Recon
│
└── Yes

      │
      ├── Admin Function?
      │
      │      └── Direct Access Test
      │
      ├── User Identifier Present?
      │
      │      └── IDOR Test
      │
      ├── Hidden URL?
      │
      │      └── Direct Browse
      │
      ├── Role Parameter?
      │
      │      └── Modify Role
      │
      ├── 403 Forbidden?
      │
      │      └── Header Manipulation
      │
      ├── POST Request?
      │
      │      └── Method Bypass
      │
      ├── Multi-Step Workflow?
      │
      │      └── Skip Steps
      │
      └── File Access?
             │
             └── Filename Manipulation