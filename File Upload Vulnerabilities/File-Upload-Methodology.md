# File Upload Methodology

## Step 1 - Identify Upload Features

Look For:

```text
Profile Pictures
Documents
Avatars
Attachments
Images
PDF Uploads
CSV Imports
Video Uploads
```

---

## Step 2 - Understand Storage

Questions:

```text
Where Are Files Stored?
Can I Access Them?
Are Names Changed?
```

---

## Step 3 - Test Extension Validation

Try:

```text
Mixed Case
Double Extensions
Alternative Extensions
Trailing Dots
Encoded Extensions
```

---

## Step 4 - Test Content-Type Validation

Change:

```http
Content-Type
```

to:

```http
image/jpeg
image/png
image/gif
```

---

## Step 5 - Test File Contents

Questions:

```text
Magic Byte Validation?
Content Inspection?
```

---

## Step 6 - Test File Accessibility

Ask:

```text
Can I Access Uploaded Files?
```

Example:

```text
/uploads/
```

---

## Step 7 - Test Execution

Ask:

```text
Does Server Execute Uploaded Files?
```

---

## Step 8 - Test Path Traversal

Question:

```text
Can I Escape Upload Directory?
```

---

## Step 9 - Test Race Conditions

Question:

```text
Can I Access File Before Security Processing?
```

---

## Step 10 - Assess Impact

```text
Stored XSS
Information Disclosure
File Overwrite
RCE
```

---

# Personal Formula

```text
Upload
        ↓
Store
        ↓
Access
        ↓
Execute
        ↓
Impact
```