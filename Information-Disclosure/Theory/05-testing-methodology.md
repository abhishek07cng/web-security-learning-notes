# Testing Methodology for Information Disclosure

## Overview

The PortSwigger material emphasizes avoiding **tunnel vision** during testing.

Instead of looking only for one vulnerability, continuously observe every response for unexpected information.

Many Information Disclosure findings are discovered while testing for completely different vulnerabilities.

---

# Step 1 – Browse the Application

Explore the website normally.

Pay attention to:

- Page source
- Comments
- HTTP headers
- Hidden resources
- Error messages

---

# Step 2 – Inspect Responses

Look carefully for unexpected information such as:

- Framework names
- Version numbers
- Database errors
- Internal paths
- File names
- IP addresses

---

# Step 3 – Test Input Validation

Submit unexpected input.

Examples include:

- Strings
- Numbers
- Special characters
- Invalid data types

Observe whether different responses reveal useful information.

---

# Step 4 – Use Fuzzing

Identify interesting parameters.

Submit many different inputs.

Compare:

- Status codes
- Response lengths
- Response times
- Error messages

---

# Step 5 – Use Burp Suite

The uploaded material recommends:

- Burp Intruder
- Burp Scanner
- Search
- Find Comments
- Discover Content

These tools help identify hidden information more efficiently.

---

# Step 6 – Check Common Disclosure Locations

Always inspect:

- robots.txt
- sitemap.xml
- Directory listings
- Backup files
- Debug pages
- Version control directories

---

# Step 7 – Analyse Error Messages

Compare different responses.

Small differences may indicate:

- Valid usernames
- Existing resources
- Framework details
- Database structure

---

# Step 8 – Record Findings

Document:

- The affected endpoint
- The leaked information
- Potential impact
- Possible follow-on attacks

---

# Testing Workflow

```
Browse Application

↓

Observe Responses

↓

Test Parameters

↓

Fuzz Inputs

↓

Inspect Errors

↓

Search Hidden Resources

↓

Document Findings
```

---

# Key Takeaways

- Avoid focusing on a single vulnerability.
- Treat every response as a potential source of information.
- Small disclosures often lead to significant discoveries later in an assessment.