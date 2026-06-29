---
name: debugging
description: "Systematically investigate a bug through evidence-based root cause analysis. Use when the debugger agent is working a reproduction, isolation, or fix-proposal step."
---

# Debugging skill

Evidence-based bug investigation. Never guess. Never fix speculatively.
Every finding is grounded in what is actually observed in the code or logs.

## When to invoke

Invoke this skill when:
- Something is broken and the root cause is unknown.
- A fix was attempted and did not resolve the issue.
- A production incident or regression is under investigation.
- A performance degradation has an unclear origin.

## Protocol

Work through all six steps in sequence. Do not skip ahead to "fix" without
completing "verify."

### Step 1 — Reproduce
Establish the symptom precisely:
- What is the observed behavior?
- What is the expected behavior?
- Can you reproduce it? Always / intermittently / only on specific input?
- If intermittent: what conditions correlate with failure?

If reproduction is not possible with the information available, stop and ask
for reproduction steps. Do not proceed without a reproducible symptom.

### Step 2 — Scope the failure
Narrow the failure to its smallest expression:
1. Read the error message and stack trace completely. Note the exact file and line.
2. If no stack trace: identify the last known-good output and the first wrong output.
3. Trace backwards: what called the failing code, with what input, with what state?
4. Check git history for changes near the failure point. Regressions have a cause.

Scope the failure to: `<file>:<line>` or `<function/component>` before hypothesizing.

### Step 3 — Hypothesize
Form at most **three** hypotheses ranked by evidence strength.
Do not skip this step. Writing hypotheses prevents fixating on the first guess.

```
H1 (most likely): <mechanism>
  Evidence: <what specifically points here>

H2: <mechanism>
  Evidence: <what points here>

H3 (least likely): <mechanism>
  Evidence: <what points here, even if weak>
```

Common root cause patterns to consider:
- **Wrong assumption about state:** value was expected to be X but was Y at call time.
- **Version mismatch:** library API changed between versions (check `sources.txt`).
- **Race condition:** two async operations interleaved in an unexpected order.
- **Off-by-one / boundary:** the edge of a range, page, or index was not handled.
- **Environment difference:** works locally, fails in CI/production due to config.
- **Silenced error:** exception was caught and logged but execution continued.

### Step 4 — Verify
Eliminate hypotheses with evidence, not intuition:
- Read the relevant code path for each hypothesis.
- Check what the actual values are at the failure point (via logs, tests, or tracing).
- Eliminate any hypothesis that contradicts observable evidence.
- Commit to one verified root cause before proceeding.

If two hypotheses survive verification, the bug may have multiple causes. Document both.

### Step 5 — Fix
Propose the **minimal** fix that addresses the verified root cause:
- Change only what is proven to be broken.
- Do not refactor adjacent code.
- Show the diff explicitly.

```diff
File: src/path/to/file.ts
Line: 42

- const result = cache.get(key)  // returns undefined when key missing
+ const result = cache.get(key) ?? defaultValue
```

State in one sentence why this change fixes the verified root cause.

### Step 6 — Verify the fix
Before proposing the fix as done:
1. Trace the reproduction steps with the fix applied. What does the output become?
2. Identify edge cases the fix might introduce.
3. Identify which existing tests cover this path. If none, say so and propose one.

## Output format

```markdown
## Bug investigation: <symptom in one line>

### Symptom
Observed: ...
Expected: ...
Reproduces: always | intermittent (<condition>) | regression since <commit/date>

### Scope
Failure located at: `<file>:<line>` or `<component>`
Call chain: `caller → ... → failing function`

### Root cause
<One to two sentences. The exact mechanism. No hedging if verified — if uncertain, say so.>

Evidence:
- `file:line` — what this tells you
- <log output / observation> — what this confirms

Eliminated hypotheses:
- H2: ruled out because <evidence>
- H3: ruled out because <evidence>

### Fix
<diff as shown above>
Reason: ...

### Verification
- With fix applied, reproduction steps now produce: <expected output>
- Edge cases introduced: none | <list>
- Tests to add: `<test description>`
```

## Escalation

| Finding                                   | Route                                          |
|-------------------------------------------|------------------------------------------------|
| Root cause is architectural               | Document and route to `architect`.             |
| Fix is non-trivial to implement           | Hand fix spec to `engineer`.                   |
| Fix is ready                              | Route to `reviewer` before closing.            |
| Root cause not found after full protocol  | Summarize what was ruled out, state what       |
|                                           | information is needed, return to `planner`.    |

## Anti-patterns — never do these

- Adding a defensive guard to paper over an unknown root cause.
- Proposing multiple alternative fixes — commit to the right one.
- Refactoring surrounding code in the same fix.
- Assuming the bug is in the most recently changed file without checking evidence.
- Closing a bug without being able to state why the fix works.
