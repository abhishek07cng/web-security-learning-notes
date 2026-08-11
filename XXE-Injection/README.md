# XXE Injection

## Overview

XML External Entity (XXE) injection is a vulnerability that occurs when an application processes attacker-controlled XML using an unsafe XML parser configuration.

Depending on the parser and application behavior, XXE can lead to:

- Local file disclosure
- Server-Side Request Forgery (SSRF)
- Blind XXE
- Out-of-band interactions
- Error-based information disclosure
- Other security-impacting behavior

---

# Learning Objectives

This module covers:

- XML entities
- Document Type Definitions (DTD)
- Custom entities
- External entities
- Basic XXE
- Local file retrieval
- XXE-based SSRF
- Blind XXE
- OOB/OAST detection
- Parameter entities
- External DTDs
- Error-based XXE
- Local DTD repurposing
- XInclude
- XXE through file uploads
- Modified Content-Type testing
- Detection methodology
- Prevention

---

# Directory Structure

```text
XXE-Injection/
│
├── Theory/
│   ├── 01-what-is-xxe-injection.md
│   ├── 02-xml-entities.md
│   ├── 03-document-type-definition-dtd.md
│   ├── 04-custom-and-external-entities.md
│   ├── 05-xxe-file-retrieval.md
│   ├── 06-xxe-ssrf.md
│   ├── 07-blind-xxe.md
│   ├── 08-oob-xxe-and-oast.md
│   ├── 09-parameter-entities.md
│   ├── 10-error-based-xxe.md
│   ├── 11-local-dtd-repurposing.md
│   ├── 12-xinclude-attacks.md
│   ├── 13-xxe-via-file-upload.md
│   ├── 14-modified-content-type-xxe.md
│   └── 15-xxe-detection-and-prevention.md
│
├── Labs/
│   ├── lab01-xxe-file-retrieval.md
│   ├── lab02-xxe-ssrf.md
│   ├── lab03-blind-xxe-oob-interaction.md
│   ├── lab04-blind-xxe-parameter-entities.md
│   ├── lab05-blind-xxe-data-exfiltration.md
│   ├── lab06-blind-xxe-error-messages.md
│   ├── lab07-blind-xxe-local-dtd-repurposing.md
│   ├── lab08-xinclude-file-retrieval.md
│   └── lab09-xxe-image-file-upload.md
│
├── Payloads/
│   ├── 01-basic-xxe-file-retrieval.md
│   ├── 02-xxe-ssrf.md
│   ├── 03-blind-xxe-oob.md
│   ├── 04-parameter-entity-xxe.md
│   ├── 05-external-dtd-exfiltration.md
│   ├── 06-error-based-xxe.md
│   ├── 07-local-dtd-repurposing.md
│   ├── 08-xinclude.md
│   ├── 09-xxe-svg-file-upload.md
│   └── 10-modified-content-type.md
│
├── Notes/
│   ├── 01-xxe-testing-checklist.md
│   └── 02-xxe-burp-workflow.md
│
├── README.md
├── XXE-Injection-Methodology.md
├── XXE-Injection-Bug-Bounty-Checklist.md
├── XXE-Injection-Decision-Tree.md
└── XXE-Injection-Quick-Revision.md