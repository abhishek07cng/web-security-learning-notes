# JWT Decision Tree

JWT Found?

│

├── No

│

│      └── Continue Recon

│

└── Yes

       │

       ├── Decode JWT

       │

       ├── Inspect Claims

       │

       ├── Inspect Header

       │

       ├── HS Algorithm?

       │

       │       └── Review Secret Management

       │

       ├── RS Algorithm?

       │

       │       └── Review Key Management

       │

       ├── alg Present?

       │

       │       └── Review Verification Logic

       │

       ├── kid?

       │

       │       └── Review Key Resolution

       │

       ├── jwk?

       │

       │       └── Review Embedded Keys

       │

       ├── jku?

       │

       │       └── Review Remote Key Retrieval

       │

       └── Impact?

               │

               ├── Authentication Bypass

               ├── JWT Forgery

               ├── Privilege Escalation

               └── Account Takeover