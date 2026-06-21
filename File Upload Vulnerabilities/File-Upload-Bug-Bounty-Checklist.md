# File Upload Bug Bounty Checklist

## Extensions

- [ ] Mixed Case
- [ ] Double Extensions
- [ ] Trailing Dot
- [ ] URL Encoding
- [ ] Alternative Extensions

---

## MIME Type

- [ ] image/jpeg
- [ ] image/png
- [ ] image/gif

---

## File Content

- [ ] Magic Byte Validation
- [ ] Polyglot Possibility

---

## Storage

- [ ] Web Accessible Directory
- [ ] Filename Randomization
- [ ] File Rename

---

## Execution

- [ ] Server-side Execution
- [ ] Source Disclosure

---

## Path Traversal

- [ ] Filename Manipulation
- [ ] Directory Escape

---

## Race Conditions

- [ ] Temporary Files
- [ ] Parallel Requests

---

## HTTP Methods

- [ ] PUT
- [ ] OPTIONS

---

## Impact

- [ ] Stored XSS
- [ ] Information Disclosure
- [ ] File Overwrite
- [ ] Remote Code Execution