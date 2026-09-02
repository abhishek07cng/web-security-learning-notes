# Creating a Custom Gadget Chain

When pre-built chains and documented exploits do not work, source-code analysis can be used to construct a custom chain.

## Methodology

### Step 1 — Find the kick-off gadget

Look for a class with a magic method invoked during deserialization.

### Step 2 — Analyze the method

Determine whether it performs a dangerous operation using attacker-controlled attributes.

### Step 3 — Follow method calls

If the first method is not directly exploitable, follow every method it invokes.

Track which values remain attacker-controlled.

### Step 4 — Find the sink

Continue until controlled data reaches a dangerous sink.

### Step 5 — Build the serialized object

Construct an object containing the required classes and values.

### Binary formats

For binary formats such as Java serialization, writing a small program in the target language can be easier than manually editing bytes.

## Secondary vulnerabilities

The source also recommends looking for opportunities where a gadget chain can trigger another vulnerability.
