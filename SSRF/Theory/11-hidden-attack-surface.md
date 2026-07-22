# Finding Hidden Attack Surface for SSRF

## Overview

Not every SSRF vulnerability is obvious.

Some applications do not expose full URLs directly but still construct server-side requests using user-controlled input.

Identifying these hidden attack surfaces is an important part of SSRF testing.

---

# Partial URLs

Some applications accept only part of a URL.

Example:

```
Hostname

↓

Server Builds Full URL

↓

Backend Request
```

Although the user controls only a portion of the request, SSRF may still be possible.

---

# URLs Embedded in Data Formats

Certain data formats allow embedded URLs.

Examples include:

- XML
- RSS
- SVG

If the server parses these formats and follows embedded URLs, SSRF may occur.

---

# SSRF via XXE

Applications vulnerable to XML External Entity (XXE) injection may also be vulnerable to SSRF.

The XML parser can retrieve remote resources specified by external entities.

---

# Referer Header

Some analytics software automatically visits URLs found in the Referer header.

Example:

```http
Referer: http://attacker.com
```

If the analytics service fetches this URL, it creates a Blind SSRF opportunity.

---

# Other Potential Attack Surfaces

Look for functionality involving:

- Webhooks
- URL previews
- Image importers
- PDF generators
- Feed readers
- File import features
- Analytics systems
- External API integrations

---

# Bug Bounty Methodology

When testing an application, ask:

- Does the server fetch URLs?
- Does it parse XML?
- Does it import remote content?
- Does it process Referer headers?
- Does it generate previews?

These features frequently expose SSRF vulnerabilities.

---

# Key Learnings

SSRF attack surfaces are not limited to URL parameters. Hidden functionality that performs server-side requests should always be investigated during security testing.