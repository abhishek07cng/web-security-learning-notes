# SVG Upload Payloads

## Impact

```text
Stored XSS
```

---

## Targets

```text
Profile Pictures
Documents
SVG Upload Features
```

---

## Attack Flow

```text
Upload SVG
        ↓
Victim Opens File
        ↓
JavaScript Executes
```

---

# Related Theory

```text
13-file-uploads-without-rce
```

---

# Key Learnings

File upload vulnerabilities do not always require RCE.