# Insecure Deserialization Testing Methodology

## Phase 1 — Discovery

Look through requests for serialized data.

Check:

- Cookies.
- Parameters.
- Encoded objects.
- Binary data.

## Phase 2 — Decode

Determine:

- Serialization language.
- Encoding layers.
- Object/class.
- Attributes.

## Phase 3 — Basic manipulation

Try authorized lab-safe changes to:

- Attribute values.
- Boolean values.
- Integer/string types.
- Object fields.

## Phase 4 — Application behavior

Trace where modified fields are used.

Look for:

- File operations.
- Database queries.
- Authentication checks.
- Callbacks.
- Templates.
- Commands.

## Phase 5 — Advanced analysis

If source code is available:

- Find magic methods.
- Find arbitrary object classes.
- Trace method calls.
- Build gadget chains.

## Phase 6 — Blind detection

Where appropriate, consider OAST techniques such as URLDNS.

## Phase 7 — Document

Record:

- Serialized format.
- Entry point.
- Modified field/type.
- Relevant code path.
- Gadget chain.
- Impact.
