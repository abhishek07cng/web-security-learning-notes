# Lab Lessons

| Lab | Main lesson |
|---|---|
| 01 | Hidden object + introspection + exposed field |
| 02 | Private fields + direct object reference |
| 03 | Endpoint discovery + weak introspection regex + destructive mutation |
| 04 | Aliases can bypass request-based rate limiting |
| 05 | Browser-forgeable GraphQL mutations can enable CSRF |

## Overall pattern

GraphQL vulnerabilities often chain several weaknesses:

**Discovery → schema knowledge → unauthorized operation/data access → impact.**

The source repeatedly demonstrates that the security boundary must be enforced on the server rather than inferred from what the frontend normally requests.
