# Client-Side Template Injection (CSTI) CheatSheet

## What Is CSTI?

Client-Side Template Injection occurs when:

```text
User Input
        ↓
Client-Side Template
        ↓
Framework Evaluation
        ↓
Code Execution
```

---

# Common Frameworks

```text
AngularJS
Vue.js
Mustache
Handlebars
```

---

# Detection Payload

```html
{{7*7}}
```

---

Expected Output

```text
49
```

---

# Alternative Detection

```html
{{1337+1}}
```

---

Expected Output

```text
1338
```

---

# Execution Flow

```text
User Input
        ↓
Template Engine
        ↓
Expression Evaluation
        ↓
Execution
```

---

# Related Labs

```text
Lab24
Lab25
```

---

# Bug Bounty Reminder

Whenever you see:

```html
{{ }}
```

test:

```html
{{7*7}}
```

immediately.