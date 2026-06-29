---
name: task-breakdown
description: "Decompose a profiled request into a concrete, ordered list of agent tasks. Use after profiling any M, L, or compound request to produce the task list the planner emits."
---

# Task breakdown skill

Task breakdown converts a profiling result into a concrete, ordered task list
where every task has exactly one responsible agent and one deliverable.

## When to invoke

Invoke this skill after profiling when:
- Size is `M`, `L`, or `XL`
- Type is `compound`
- The user's request implies more than one distinct deliverable

For `S` + single-type requests, a task list is usually one line and can be
written inline without this skill.

## Task anatomy

Every task has five fields:

```
Task N: [AGENT] <verb phrase — what gets done>
  Scope:    <what this task covers, not what it defers>
  Input:    <what the agent needs to start: an artifact, the codebase, a prior task's output>
  Output:   <the single deliverable this task produces>
  Depends:  <task numbers that must be complete first, or "none">
```

Keep each task to one agent and one output. If two things are output, split the task.

## Sizing heuristics

| Size | Expected task count | Notes                                              |
|------|---------------------|----------------------------------------------------|
| `S`  | 1–2                 | Often one task, review optional.                   |
| `M`  | 3–5                 | Design if cross-file, implement, review.           |
| `L`  | 6–9                 | ADR, design, implement (may be split), review.     |
| `XL` | TBD after scoping   | Do not estimate XL — scope it first.               |

## Standard pipelines

### Lookup (any size)
```
Task 1: [doc-library] Look up <API/option/version>
  Scope:   Verify the API signature, option name, or version.
  Input:   User's question + sources.txt
  Output:  Cited answer with file path and version.
  Depends: none
```

### S feature (no prior design)
```
Task 1: [engineer] Implement <change>
  Output: Working code diff.
Task 2: [reviewer] Review task 1 output
  Output: Approved or blockers list.
```

### M feature
```
Task 1: [doc-library] Verify <library API if involved>
Task 2: [engineer] Implement <feature>
Task 3: [reviewer] Review task 2 output
```

### L feature (cross-subsystem)
```
Task 1: [doc-library] Verify <library API if involved>
Task 2: [architect] Design <system/ADR>
Task 3: [engineer] Implement <feature> per task 2 design
Task 4: [reviewer] Review task 3 output — design and implementation
```

### Bug fix
```
Task 1: [debugger] Investigate <symptom> and identify root cause
Task 2: [engineer] Implement fix per task 1 root cause
Task 3: [reviewer] Review fix
```

### Refactor
```
Task 1: [reviewer] Assess current code, identify issues
Task 2: [architect] Design target structure (if M+)
Task 3: [engineer] Refactor per task 1/2
Task 4: [reviewer] Review task 3 output
```

## Output format

Produce the full task list followed by a routing instruction:

```markdown
## Tasks

Task 1: [AGENT] ...
  Scope: ...
  Input: ...
  Output: ...
  Depends: none

Task 2: [AGENT] ...
  Scope: ...
  Input: task 1 output
  Output: ...
  Depends: task 1

...

## First step
Switch to `/agent <first-agent>` and start with Task 1.
When Task 1 is complete, return here or continue to Task 2 with `/agent <next-agent>`.
```

## Rules

- Never assign implementation code to `planner` or `architect`.
- Never assign design or architecture to `engineer`.
- Never skip `reviewer` on `medium` or `high` risk tasks.
- If a task's output is ambiguous, make it concrete: "a working diff" beats "implementation."
- If a dependency is unclear, make it explicit rather than assuming the agent will figure it out.
