# Web Cache Poisoning Decision Tree

```text
START
 |
 |-- Find a cache oracle
 |       |
 |       +-- Hit/miss header?
 |       +-- Age?
 |       +-- Dynamic response?
 |       +-- Timing?
 |
 |-- Determine cache key
 |       |
 |       +-- Request line?
 |       +-- Host?
 |       +-- Port?
 |       +-- Query string?
 |       +-- Selected parameters?
 |       +-- Headers?
 |       +-- Cookies?
 |       +-- Vary?
 |
 |-- Find unkeyed/ambiguous input
 |       |
 |       +-- Header?
 |       +-- Cookie?
 |       +-- Parameter?
 |       +-- GET body?
 |
 |-- Does input alter response?
 |       |
 |       +-- NO → test another input
 |       |
 |       +-- YES
 |
 |-- Is response cacheable?
 |       |
 |       +-- NO → study cache conditions
 |       |
 |       +-- YES
 |
 |-- Find gadget
 |       |
 |       +-- XSS
 |       +-- DOM-XSS
 |       +-- Redirect
 |       +-- Resource import
 |       +-- JSON/CSS/JS
 |
 |-- Implementation flaw?
 |       |
 |       +-- Query exclusion
 |       +-- Parameter cloaking
 |       +-- Normalization
 |       +-- Key injection
 |       +-- Fat GET
 |       +-- Internal cache
 |
 END → Verify cache hit → Verify authorized lab impact
