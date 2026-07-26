# Information Disclosure Bug Bounty Checklist

## Recon

☐ Browse every page.

☐ Observe all HTTP responses.

☐ Review page source.

☐ Inspect response headers.

---

## Error Handling

☐ Trigger application errors.

☐ Test invalid parameter values.

☐ Compare error responses.

☐ Record framework versions.

☐ Record stack traces.

---

## Hidden Resources

☐ robots.txt

☐ sitemap.xml

☐ Backup directories

☐ Debug pages

☐ Hidden resources

---

## Developer Artifacts

☐ HTML comments

☐ TODO notes

☐ Debug information

☐ Internal endpoints

---

## Configuration

☐ HTTP TRACE enabled?

☐ Directory listing enabled?

☐ Verbose errors?

☐ Debug mode enabled?

☐ Version control exposed?

---

## Backup Files

☐ *.bak

☐ *~

☐ .old

---

## Git

☐ /.git accessible?

☐ Review commit history.

☐ Search for deleted credentials.

---

## Burp Suite

☐ Repeater

☐ Intruder

☐ Search

☐ Find Comments

☐ Discover Content

☐ Logger++

---

## Reporting

☐ Endpoint

☐ Reproduction steps

☐ Evidence

☐ Security impact

☐ Recommended mitigation

---

## Final Verification

☐ Information disclosure confirmed.

☐ Sensitive information documented.

☐ Follow-on attack potential assessed.