# Lab 03: Source Code Disclosure via Backup Files

## Lab Description

This lab exposes application source code through backup files stored in a hidden directory.

Your objective is to retrieve the hard-coded database password from the leaked source code.

---

# Objective

- Discover the hidden backup directory.
- Access the backup source code.
- Extract the database password.
- Submit the password.

---

# Vulnerability

The application exposes source code through publicly accessible backup files.

---

# Exploitation Steps

## Step 1

Browse to:

```text
/robots.txt
```

---

## Step 2

Review the file.

It reveals the existence of:

```text
/backup
```

---

## Step 3

Browse to:

```text
/backup
```

Locate:

```text
ProductTemplate.java.bak
```

---

## Step 4

Open the backup file.

The application returns the Java source code.

---

## Step 5

Review the connection builder.

Locate the hard-coded PostgreSQL database password.

---

## Step 6

Submit the password.

The lab is solved.

---

# Why This Works

The application accidentally exposes backup source code files.

These files contain sensitive implementation details that should never be accessible.

---

# Burp Workflow

```
Browse robots.txt

↓

Discover Backup Directory

↓

Open .bak File

↓

Read Source Code

↓

Locate Database Password
```

---

# Impact

Source code disclosure may reveal:

- Database credentials
- API keys
- Business logic
- Internal endpoints
- Authentication mechanisms

---

# Mitigation

- Remove backup files before deployment.
- Prevent public access to backup directories.
- Regularly audit exposed resources.

---

# Bug Bounty Methodology

Always inspect:

- robots.txt
- Hidden directories
- Backup files
- Temporary files

---

# Key Learnings

- Backup files often contain complete source code.
- Source code frequently exposes sensitive credentials.
- Hidden directories should always be investigated.