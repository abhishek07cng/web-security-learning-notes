# Other DOM Sink Payloads

## 1. Purpose

Reference payloads and test values for less-common DOM/browser sinks.

Covered areas:

```text
eval()
WebSocket()
setRequestHeader()
FileReader
ExecuteSql()
sessionStorage
document.evaluate()
JSON.parse()
setAttribute()
RegExp()
```

The correct approach is always:

```text
SOURCE → DATA → SINK → BEHAVIOR
```

---

# 2. `eval()` Testing

Use a harmless execution test:

```javascript
print()
```

Conceptually:

```javascript
eval("print()");
```

If the application places attacker-controlled data into an `eval()` call, determine whether the input can alter the evaluated JavaScript.

---

# 3. `eval()` Marker

Start with:

```text
evaltest123
```

Trace:

```text
evaltest123
      ↓
variable
      ↓
eval()
```

---

# 4. WebSocket URL Testing

If code contains:

```javascript
new WebSocket(url)
```

test a controlled URL:

```text
wss://example.com
```

or:

```text
ws://example.com
```

Determine whether attacker-controlled input can modify:

```text
Scheme
Host
Port
Path
```

---

# 5. `setRequestHeader()` Testing

For:

```javascript
xhr.setRequestHeader(name, value);
```

use a harmless marker:

```text
headertest123
```

Then inspect the resulting request.

---

# 6. FileReader Testing

If attacker-controlled input influences:

```javascript
FileReader.readAsText()
```

first determine:

```text
What object is supplied?
Can attacker control the selected file?
Can the attacker control the path/reference?
```

Use only authorized local test files.

---

# 7. Client-Side SQL Testing

For:

```text
ExecuteSql()
```

start with a marker:

```text
sqltest123
```

Then inspect the resulting query construction.

Test characters:

```text
'
"
\
(
)
```

The objective is to understand:

```text
Input → Query Construction → ExecuteSql()
```

---

# 8. Storage Testing

For:

```javascript
sessionStorage.setItem()
```

use:

```text
storagetest123
```

Example:

```javascript
sessionStorage.setItem("test", "storagetest123");
```

Then inspect:

```text
DevTools → Application → Session Storage
```

---

# 9. Storage Consumer Testing

Search for:

```javascript
sessionStorage.getItem()
```

and:

```javascript
localStorage.getItem()
```

Trace:

```text
Stored Value
      ↓
Application
      ↓
Sink
```

---

# 10. XPath Testing

For:

```javascript
document.evaluate()
```

start with:

```text
xpath123
```

Then test XPath-sensitive characters:

```text
'
"
[
]
(
)
```

Determine whether attacker-controlled data changes the XPath expression.

---

# 11. JSON.parse() Testing

Start with valid JSON:

```json
{"test":"json123"}
```

Then determine:

```text
Which properties are consumed?
```

For example:

```json
{
    "type": "test",
    "url": "https://example.com"
}
```

---

# 12. JSON Property Testing

Test:

```json
{"type":"test"}
```

```json
{"type":"test","url":"https://example.com"}
```

```json
{"type":"test","value":"json123"}
```

Only use properties supported by the application's code.

---

# 13. `setAttribute()` Testing

If code contains:

```javascript
element.setAttribute(attribute, value);
```

identify:

```text
Element
Attribute
Value
```

Test a controlled URL:

```text
https://example.com
```

for URL-related attributes.

---

# 14. Attribute Testing

Security-sensitive attributes include:

```text
href
src
action
style
```

and event-handler attributes:

```text
onclick
onerror
onload
```

The exact security impact depends on whether the application permits the attribute and value.

---

# 15. `RegExp()` Testing

For:

```javascript
new RegExp(pattern)
```

start with:

```text
regextest123
```

Then assess:

```text
Pattern Length
Pattern Complexity
Repeated Processing
Execution Time
```

The objective is to determine whether attacker-controlled patterns can cause excessive resource consumption.

---

# 16. RegExp Special Characters

Useful testing characters:

```text
*
+
?
{
}
(
)
[
]
|
.
\
^
$
```

Do not classify a pattern as a DoS issue without demonstrating meaningful resource consumption.

---

# 17. Generic Sink Marker

Use:

```text
sinktest123
```

Then trace:

```text
sinktest123
      ↓
Source
      ↓
Variable
      ↓
Sink
```

---

# 18. Other-Sink Checklist

```text
☐ Sink identified
☐ Argument identified
☐ Source identified
☐ Attacker control confirmed
☐ Transformation identified
☐ Validation identified
☐ Browser/API behavior understood
☐ Impact confirmed
```

---

# Quick Reference

```text
eval()              → print()
WebSocket()         → controlled ws/wss URL
setRequestHeader()  → headertest123
FileReader          → authorized test file
ExecuteSql()        → sqltest123
sessionStorage      → storagetest123
document.evaluate() → xpath123
JSON.parse()        → valid JSON marker
setAttribute()      → controlled URL
RegExp()            → regextest123
```

---

# Final Rule

```text
SINK FOUND
   ↓
IDENTIFY ARGUMENT
   ↓
TRACE SOURCE
   ↓
CONFIRM CONTROL
   ↓
TEST BEHAVIOR
   ↓
CONFIRM IMPACT
```