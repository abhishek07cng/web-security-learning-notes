# Types of Information Disclosure

Information Disclosure can expose many different categories of sensitive information.

The PortSwigger material groups these disclosures into three broad categories.

---

# 1. User Information

Sensitive information belonging to users may be accidentally exposed.

Examples include:

- Usernames
- Email addresses
- Phone numbers
- Financial information
- Credit card information

---

## Risks

Leaked user information may lead to:

- Privacy violations
- Account enumeration
- Identity theft
- Targeted phishing

---

# 2. Business Information

Applications sometimes reveal confidential organizational information.

Examples include:

- Internal documents
- Business logic
- Configuration data
- Commercial information

---

## Risks

Business information may reveal:

- Internal processes
- Development practices
- Hidden functionality
- Sensitive operational details

---

# 3. Technical Information

Technical disclosures are extremely valuable during penetration testing because they reveal how the application works.

Examples include:

- Framework names
- Framework versions
- Database technologies
- Database table names
- Internal IP addresses
- Source code
- Backup files
- API keys
- Directory structure
- Version control history

---

# Why Technical Information Matters

Even when technical information is not directly sensitive, it helps attackers answer questions such as:

- Which framework is used?
- Which version is installed?
- Is the version vulnerable?
- Which files exist?
- Which technologies are running?
- Where are sensitive resources located?

---

# Examples from the PortSwigger Material

The uploaded content includes examples such as:

- Hidden directories listed in `robots.txt`
- Directory listings
- Source code exposed via backup files
- Verbose database errors
- Hard-coded API keys
- Database credentials
- Framework version disclosure
- User enumeration through application behavior

---

# Direct vs Indirect Impact

## Direct Impact

Information itself is sensitive.

Examples:

- Credit card numbers
- API keys
- Passwords

---

## Indirect Impact

Information assists in exploiting another vulnerability.

Examples:

- Framework version
- Directory names
- Database structure
- Hidden endpoints

---

# Key Takeaways

- Information Disclosure is not limited to personal data.
- Technical information often has significant security value.
- Even small disclosures can become important when combined with other findings.