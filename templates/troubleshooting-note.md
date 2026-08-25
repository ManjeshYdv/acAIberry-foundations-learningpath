# Troubleshooting Note

**Date:**

**Symptom:** What did the user or command observe?

**Expected:** What should have happened?

## Checks in order

- [ ] Reproduced the exact failure
- [ ] Checked process/container state
- [ ] Checked the listening port and HTTP response
- [ ] Read the relevant logs around the failure time
- [ ] Checked CPU, memory, and disk
- [ ] Checked environment/configuration without printing secrets
- [ ] Checked the latest Git/deployment change

## Evidence

Record only the few useful commands and outputs.

## Cause

State the verified cause, not the first guess.

## Fix and verification

What changed? Which command proves recovery?

## Prevention

Would a test, clearer log, health check, documentation change, or alert catch this sooner?
