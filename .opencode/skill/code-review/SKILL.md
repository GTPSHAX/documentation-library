---
name: code-review
description: "Review code for correctness, security, performance, and maintainability using a systematic checklist. Use when the reviewer agent is asked to assess any code change or existing code."
---

# Code review skill

Systematic code review. Every section runs on every review.
Findings are ranked by severity. Nothing is invented.

## When to invoke

Invoke this skill when:
- The engineer has delivered an implementation and the task list calls for review.
- The user asks for a code review on existing code.
- A design needs security validation before implementation starts.
- A bug fix needs verification before it is closed.

## Pre-review: gather context

Before opening the diff:
1. Read the task description and the engineer's delivery summary.
2. Identify the risk level from the planner's profile (`low` / `medium` / `high`).
3. Check `./sources.txt` for any library involved in the change.
4. Read the test files that cover the changed code, if any.

## Checklist

Run every section. A section with no findings gets `No issues.`

### Section 1 — Correctness
- Does the code match the task description?
- Are all edge cases from the task plan handled?
- Are errors propagated explicitly? No silent `null` on failure, no swallowed exceptions.
- Are async calls awaited? Are promises chained, not floating?
- Are mutations side-effect-free or explicitly scoped?
- If the task involved a bug fix: does the fix address the verified root cause?

### Section 2 — Security (all risk levels)
- Are user-supplied inputs sanitized before use in queries, paths, or templates?
- Are database queries parameterized? No string concatenation.
- Are secrets absent from logs, error messages, and API responses?
- Is authorization checked (not just authentication) on every protected operation?
- For file operations: are paths validated against traversal (`../`)?
- For LLM integrations: is user input isolated from the system prompt context?

**High-risk additions**
Run these when risk is `high`:
- Cryptographic operations use standard library functions, not custom implementations.
- Session tokens are generated with a CSPRNG, not `Math.random()` or `Date.now()`.
- Rate limiting or abuse protection is present on public-facing endpoints.
- PII is not logged, stored unencrypted, or sent to third parties without consent.

### Section 3 — Performance
- Is there an O(n²) loop over unbounded input?
- Is there a database query inside a loop (N+1)?
- Are large responses streamed rather than fully buffered?
- Are expensive operations (DB, network, compute) cached where appropriate?
- Are memory allocations in hot paths justified?

### Section 4 — Maintainability
- Are function and variable names self-explanatory?
- Does each function do one thing?
- Are comments explaining *why*, not *what*? Are predictive or decorative comments absent?
- Does the code follow the patterns established in the rest of the codebase?
- Are tests present? Do they cover the happy path and at least one meaningful edge case?
- Are new dependencies justified (not achievable in <20 lines)?

### Section 5 — Library usage
- Are all library calls consistent with the version in `./sources.txt`?
- Are deprecated APIs avoided?
- Were unfamiliar APIs verified in `doc-library` before use?

## Severity classification

| Severity    | Definition                                                          |
|-------------|---------------------------------------------------------------------|
| `BLOCKER`   | Must be fixed before merge. Correctness, security, or data safety.  |
| `IMPROVE`   | Should be fixed; technical debt or maintainability concern.         |
| `NITPICK`   | Optional; style, minor naming, non-functional.                      |

## Output format

```markdown
## Code review: <task or file name>

**Verdict:** ✅ Approved | ⚠️ Approved with notes | 🔴 Changes required

### Blockers
- [SECURITY | CORRECTNESS | PERF] `file.ext:line` — what is wrong and why it matters.
  Fix: <one-liner or approach>

### Improvements
- `file.ext:line` — what and why.

### Nitpicks
- `file.ext:line` — optional detail.

### Notes for engineer
Priority-ordered list of what to address.
Route to /agent engineer with the blockers above.
```

## After review

| Verdict              | Next step                                                  |
|----------------------|------------------------------------------------------------|
| ✅ Approved          | Task complete. Return to planner if further tasks remain.  |
| ⚠️ Approved w/ notes | Engineer may address improvements in a follow-up task.     |
| 🔴 Changes required  | Route to engineer with blockers. Re-review after fix.      |

If the root cause of a blocker is architectural, route to `architect` before
sending back to `engineer`.
