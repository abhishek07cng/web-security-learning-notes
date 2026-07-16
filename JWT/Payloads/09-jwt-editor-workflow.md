# Burp JWT Editor Workflow

## Step 1

Capture a request containing a JWT.

↓

Send it to:

```text
Repeater
```

---

## Step 2

Open the:

```text
JSON Web Token Editor
```

---

## Step 3

Inspect:

```text
Header

Payload

Signature
```

---

## Step 4

Identify:

```text
Algorithm

Claims

Header Parameters
```

---

## Step 5

If appropriate for the assessment and within authorization:

```text
Generate Keys

Sign Tokens

Test Verification Behavior
```

using the JWT Editor features.

---

## Common JWT Editor Features

```text
Generate RSA Keys

Generate Symmetric Keys

Embedded JWK

Sign JWT

Decode Claims
```

---

# Personal Workflow

```text
Capture JWT

↓

Decode

↓

Understand Claims

↓

Inspect Header

↓

Review Verification Behavior

↓

Assess Impact
```

---

# Key Learnings

Burp JWT Editor greatly simplifies JWT analysis, but understanding the underlying verification process is far more important than simply using the tool.