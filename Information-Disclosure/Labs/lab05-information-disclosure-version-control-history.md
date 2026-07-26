# Lab 05: Information Disclosure in Version Control History

## Lab Description

This lab demonstrates how exposing a Git repository can leak sensitive information from previous commits.

Although the current application no longer contains a hard-coded administrator password, it remains visible in the Git commit history.

Your objective is to recover the administrator password, log in, and delete the user **carlos**.

---

# Objective

- Download the exposed Git repository.
- Review the commit history.
- Recover the administrator password.
- Log in as the administrator.
- Delete the user **carlos**.

---

# Vulnerability

The application's `.git` directory is publicly accessible.

This exposes version control history, including previous commits containing sensitive information.

---

# Exploitation Steps

## Step 1

Browse to:

```text
/.git
```

The Git repository is publicly accessible.

---

## Step 2

Download the repository.

For Linux users, the PortSwigger material demonstrates:

```bash
wget -r https://YOUR-LAB-ID.web-security-academy.net/.git/
```

---

## Step 3

Open the downloaded repository using Git.

Review the commit history.

---

## Step 4

Locate the commit with the message:

```text
Remove admin password from config
```

---

## Step 5

Inspect the commit diff.

Notice that the application replaced a hard-coded administrator password with an environment variable.

However, the previous password is still visible in the Git history.

---

## Step 6

Use the recovered password to log in as the administrator.

---

## Step 7

Open:

```text
/admin
```

Delete:

```
carlos
```

The lab is solved.

---

# Burp / Git Workflow

```
Browse /.git

↓

Download Repository

↓

Review Commit History

↓

Inspect Git Diff

↓

Recover Admin Password

↓

Administrator Login

↓

Delete Carlos
```

---

# Why This Works

Git preserves historical versions of files.

Removing sensitive information from the current version of a file does not remove it from previous commits.

If the `.git` directory is publicly accessible, attackers can inspect the entire development history.

---

# Impact

Exposed version control history may reveal:

- Passwords
- API keys
- Secrets
- Source code
- Previous configurations
- Internal implementation details

---

# Mitigation

- Never expose the `.git` directory in production.
- Remove secrets from version control history when necessary.
- Store sensitive values in secure environment variables instead of source code.
- Regularly audit production deployments for exposed repositories.

---

# Bug Bounty Methodology

Always test for:

- `/.git`
- Exposed repository metadata
- Commit history
- Sensitive values in historical changes
- Deleted credentials remaining in Git diffs

---

# Key Learnings

- Git history may contain secrets that no longer exist in the current code.
- Exposed version control data can significantly simplify further attacks.
- Secrets should never be committed to version control repositories.