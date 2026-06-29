---
name: system-design
description: "Produce architecture decisions, system designs, and integration patterns. Use when a feature spans more than one subsystem or when a design decision must be documented before implementation starts."
---

# System design skill

This skill guides the production of architecture artifacts: ADRs, system designs,
data models, and interface contracts. Use it before any `L` implementation or
whenever a decision must survive longer than one session.

## When to invoke

Invoke this skill when:
- A feature spans more than one subsystem or file boundary.
- A choice between two or more valid implementation approaches must be recorded.
- A new service boundary, data model, or integration point is being established.
- A security-sensitive design needs to be reviewed before code is written.
- The user explicitly asks for an ADR or architecture document.

## Prerequisite: read first

Before designing:
1. Read the existing codebase structure around the feature's landing zone.
2. Read `./sources.txt` and open `doc-library` for any library the design depends on.
3. Check for existing ADRs that might conflict or that this decision supersedes.

## Artifact 1 — Architecture Decision Record (ADR)

Use an ADR when the decision is not obvious, has lasting consequences, or
involves trade-offs between two or more valid options.

```markdown
# ADR-NNN: <short imperative title — "Use X for Y", "Split Z into A and B">

**Status:** Proposed | Accepted | Superseded by ADR-NNN
**Date:** YYYY-MM-DD

## Context
What is the problem, and why must a decision be made now?
One paragraph. Concrete, not abstract.

## Constraints
- <hard constraint 1> (library version, team size, latency budget, etc.)
- <hard constraint 2>

## Options considered

### Option A — <name>
What it is and how it addresses the problem.
Pros: (bullet list, specific to this project's constraints)
Cons: (bullet list, honest)

### Option B — <name>
...

## Decision
**Option X** — because <one or two sentences tying the choice to the actual constraints>.

## Consequences
- Becomes easier: ...
- Becomes harder or deferred: ...
- Follow-up decisions required: ...
```

Rules for ADRs:
- One decision per ADR. Bundle decisions = unclear accountability.
- At least two options, always. A decision with no alternatives was not a decision.
- Consequences must include at least one negative — all designs have trade-offs.

## Artifact 2 — System design (for M/L features)

Use a system design when the change involves multiple components or subsystems
and the engineer needs interface contracts before starting.

```markdown
## System design: <feature name>

### Scope
What this design covers. What it explicitly defers to a follow-up.

### Components
- `ComponentName` — single-sentence responsibility.
- `ComponentName` — ...

### Data model (if applicable)
Key entities, their fields, and their relationships.
Use a plain table or entity list — not UML, not a diagram tool.

| Entity       | Key fields                | Relations                     |
|--------------|--------------------------|-------------------------------|
| User         | id, email, role           | has many Sessions             |
| Session      | id, userId, token, expiry | belongs to User               |

### Interface contracts
The public surface this design exposes. Enough for the engineer to implement
without guessing.

- **Function / endpoint**: `POST /sessions`
  - Input: `{ email: string, password: string }`
  - Output: `{ token: string, expiresAt: ISO8601 }`
  - Errors: `401 Unauthorized`, `422 Unprocessable Entity`

### Integration points
Which existing systems, libraries, or services this touches.
Library: cite version from `sources.txt`. If not snapshotted, flag it.

### Open questions
Decisions not yet made. Block implementation until these are resolved.
- [ ] Should token refresh be stateless (JWT) or stateful (DB session)?
```

## Checklist before handing to engineer

- [ ] All interface contracts are complete enough to implement without asking
      architectural questions.
- [ ] All library versions are confirmed in `./sources.txt`.
- [ ] Security-sensitive decisions are flagged for reviewer to check before code starts.
- [ ] Open questions are either answered or explicitly deferred.

## Output

End every design artifact with the handoff block:

```markdown
## Ready for implementation
Tasks for engineer:
1. [engineer] <concrete task — scoped to one file or component>
2. [engineer] ...

Route to /agent engineer when ready.
```
