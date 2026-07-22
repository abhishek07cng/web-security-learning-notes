# SSRF Bug Bounty Checklist

## Discovery

☐ Identify URL-fetching functionality

☐ Locate parameters containing URLs or hostnames

☐ Test headers (Referer, etc.)

☐ Review import and webhook features

---

## Localhost Testing

☐ localhost

☐ 127.0.0.1

☐ 127.1

☐ Different ports

☐ /admin

☐ /debug

---

## Internal Network

☐ 192.168.x.x

☐ 10.x.x.x

☐ 172.16.x.x

☐ Scan with Burp Intruder

---

## Filter Bypass

☐ Alternative IP formats

☐ URL Encoding

☐ Double URL Encoding

☐ Embedded Credentials

☐ URL Fragments

☐ Nested Hostnames

☐ Open Redirects

---

## Blind SSRF

☐ Burp Collaborator

☐ Referer Header

☐ Webhooks

☐ Callback URLs

☐ Analytics

---

## Impact Assessment

☐ Admin Panel Access

☐ Internal APIs

☐ Authentication Bypass

☐ Cloud Metadata

☐ Internal Network Discovery

☐ Sensitive Data Exposure

---

## Reporting

☐ Payload

☐ Request

☐ Response

☐ Impact

☐ Mitigation

☐ Screenshots