# Insecure Deserialization Bug Bounty Checklist

## Discovery
- [ ] Inspect cookies and parameters.
- [ ] Look for serialized PHP objects.
- [ ] Look for Java `rO0`/`ac ed` indicators.
- [ ] Identify Ruby Marshal data where applicable.
- [ ] Check Burp Scanner findings.

## Basic testing
- [ ] Decode the serialized object.
- [ ] Identify interesting attributes.
- [ ] Modify safe/lab-controlled attributes.
- [ ] Test type changes where appropriate.
- [ ] Preserve serialization lengths and type labels.

## Application functionality
- [ ] Trace file paths.
- [ ] Trace database identifiers.
- [ ] Trace callbacks.
- [ ] Trace template values.
- [ ] Trace authentication/authorization attributes.

## Advanced testing
- [ ] Identify magic methods.
- [ ] Check arbitrary object injection.
- [ ] Search for gadget chains.
- [ ] Identify kick-off and sink gadgets.
- [ ] Consider pre-built chains.
- [ ] Consider OAST for blind behavior.
- [ ] Check PHAR paths for PHP applications.

## Defensive review
- [ ] Is user input deserialized?
- [ ] Is integrity checked before deserialization?
- [ ] Are generic serializers being used?
- [ ] Are sensitive/private fields unnecessarily serialized?
