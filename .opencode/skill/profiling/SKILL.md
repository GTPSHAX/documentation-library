---
name: profiling
description: "Classify an incoming request by type and complexity before routing to a specialist agent. Use when a request needs to be categorized to determine which agent and pipeline to invoke."
---

# Profiling skill

Profiling classifies a request across three dimensions before any work begins.
It is the first step in every non-trivial session and the entry point for any
request that could go to more than one agent.

## When to invoke

Invoke this skill when:
- A new user request arrives and the destination agent is unclear.
- A request spans multiple types (e.g. "find the bug and fix it and review it").
- A request is ambiguous enough that the wrong agent would waste a full turn.
- A task mid-flight reveals a scope larger than initially classified.

Do not invoke this skill for pure `lookup` requests that clearly target a single
library or API — route directly to `doc-library` instead.

## Dimension 1 — Request type

| Type       | Signal keywords / patterns                                       |
|------------|------------------------------------------------------------------|
| `lookup`   | "how does", "what option/version/API", "does X support Y"        |
| `design`   | "architecture", "ADR", "pattern", "data model", "integrate"      |
| `feature`  | "implement", "add", "build", "write", "create", "refactor"       |
| `review`   | "review", "check my code", "is this right", "any issues"         |
| `bug`      | "broken", "error", "exception", "crash", "not working"           |
| `compound` | Two or more types present in the same request                    |

**When type is `compound`:** list each sub-type in order of logical execution.
Standard sequences:
- Bug + fix: `bug → feature → review`
- New feature: `design → feature → review` (skip design for `S`)
- Refactor: `review → design → feature → review`

## Dimension 2 — Size

| Size | Definition                                                      |
|------|-----------------------------------------------------------------|
| `S`  | Single file, self-contained, answer fits in one reply.          |
| `M`  | Multi-file, one subsystem, clear bounded scope.                 |
| `L`  | Cross-subsystem or cross-library, requires design before code.  |
| `XL` | Greenfield, major refactor, or scope is not yet determined.     |

**When size is `XL`:** do not profile fully. Ask one clarifying question to
bound the scope, then re-profile.

## Dimension 3 — Risk

| Risk level | Triggers                                                         |
|------------|------------------------------------------------------------------|
| `low`      | Read-only queries, internal tooling, isolated utility code.      |
| `medium`   | User-facing features, external API integrations, data mutations. |
| `high`     | Auth, payment, PII, secrets handling, LLM prompt construction.   |

**When risk is `high`:** the reviewer must review the design (if `L`) before
implementation starts, and must review the implementation before it is done.

## Profiling output format

```
Type: <type>  |  Size: <S/M/L/XL>  |  Risk: <low/medium/high>

Sub-types (if compound): <ordered list>
Clarifying question (if XL): <single question>
```

## Transition

After profiling, hand the result to the task-breakdown skill to produce the
task list, or route directly to the target agent for `S` + `lookup` cases.
