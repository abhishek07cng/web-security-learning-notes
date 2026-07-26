# Information Disclosure Testing Checklist

## Initial Recon

☐ Browse the application manually.

☐ Observe every response carefully.

☐ Check page source.

☐ Inspect response headers.

☐ Review cookies.

☐ Look for unexpected information.

---

## Error Handling

☐ Submit invalid parameter values.

☐ Submit unexpected data types.

☐ Trigger application errors.

☐ Compare different error messages.

☐ Look for:

- Framework names
- Framework versions
- File paths
- Database information
- Stack traces

---

## Hidden Resources

Check:

☐ /robots.txt

☐ /sitemap.xml

☐ Hidden directories

☐ Backup folders

☐ Debug pages

---

## Developer Information

☐ Search HTML comments.

☐ Look for TODO notes.

☐ Identify hidden endpoints.

☐ Review JavaScript files.

---

## Configuration Review

Check for:

☐ Directory listing

☐ HTTP TRACE

☐ Debug mode

☐ Debug pages

☐ Version control exposure

---

## Burp Suite

Use:

☐ Repeater

☐ Intruder

☐ Search

☐ Find Comments

☐ Discover Content

☐ Logger++

---

## Documentation

Record:

- Endpoint
- Request
- Response
- Leaked information
- Security impact
- Possible follow-on attacks

---

## Final Checklist

☐ No sensitive information exposed.

☐ No unnecessary debugging information.

☐ No verbose errors.

☐ No exposed hidden resources.