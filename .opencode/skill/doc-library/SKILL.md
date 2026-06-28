---
name: doc-library
description: "Look up API, option, config, or usage details for any library declared in ./sources.txt by walking its local documentation tree. Use when the user asks how a documented feature works, requests an example, or asks for a version check."
---

# doc-library skill

The repository is a **versioned documentation library**. This skill guides a
precise, file-grounded lookup against local snapshots, scaled to however
many libraries are currently declared in `./sources.txt`.

## When to invoke

Invoke this skill when the user asks about:

- Any component, class, API, option, command, or config value for a
  library that has a snapshot in this repository.
- "What's the right option/property/method for X in this library?"
- Any question that requires citing a specific documentation page and
  version.

## Discovery (read `sources.txt` first)

1. Read `./sources.txt`. Skip blank lines and lines starting with `#`.
2. Each non-comment line has the format
   `name|repo|ref|sparse_path|mode`. The doc tree for that entry lives at
   `./<name>/` (or `./.<name>/` if the name is dot-prefixed).
3. Match the user's question to a `name` from `sources.txt`. If the
   question references a library not present in `sources.txt`, that
   library is **not in scope** — say so and stop.
4. If a `name` in `sources.txt` has no matching sibling directory, the
   snapshot is **unsynced** — recommend `./scripts/add.sh`.

`sources.txt` is the single source of truth. The human-readable
"Documentation Sources" table in `./README.md` is a cache; if the two
disagree, `sources.txt` wins.

## Lookup procedure

1. **Identify the target library** by matching the user's question to a
   `name` in `sources.txt`.
2. **Locate the relevant section** by reading the directory tree under
   `./<name>/`. Use the in-repo path structure as the authoritative
   index.
3. **Open the matching `.md` file(s)** and read the section that
   addresses the question. Prefer the most specific file over a
   top-level overview.
4. **Quote the documentation** (paraphrased if long) and **cite the file
   path** in the answer. Path format: `<name>/<rest-of-path>.md`.
5. **State the version** (from the `ref` field in `sources.txt` and/or
   the `Updated` date in `README.md`) alongside the citation so the
   user can confirm the snapshot matches their project.

## Fallback behavior

- If the local snapshot is **missing** the topic, say so explicitly. Do
  not invent the answer from memory.
- Suggest the user check the upstream repo (the `repo` URL from
  `sources.txt`) for the latest version, or add the source to
  `sources.txt` and re-run `./scripts/add.sh`.
- If the user is on a **different version** than the snapshot, warn them
  and recommend syncing or consulting upstream.

## What this skill does not do

- Does not edit any directory listed in `sources.txt` (read-only
  snapshots).
- Does not re-sync documentation.
- Does not run the opencode CLI; it is a behavior loaded into the agent
  via the `skill` tool.

## Output template

When answering, use this shape:

```text
Library: <name from sources.txt>
Version: <ref / updated date>
Source: <relative path to the .md file>
Reference: <short paraphrase or quote>
```

If a single question spans multiple libraries, repeat the block per
library.
