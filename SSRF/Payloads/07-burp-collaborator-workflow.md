# Burp Collaborator Workflow

## Step 1

Generate a Collaborator payload.

---

## Step 2

Insert the payload into:

- Referer
- URL parameter
- Callback URL

---

## Step 3

Send the request.

---

## Step 4

Poll Collaborator.

---

## Step 5

Review interactions.

Possible results:

- DNS
- HTTP
- SMTP

---

## Notes

DNS-only interactions may still indicate Blind SSRF if outbound HTTP connections are restricted.