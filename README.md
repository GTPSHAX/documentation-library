# Documentation Library

A centralized collection of version-specific documentation used as reference material for AI systems, RAG pipelines, and Large Language Models (LLMs).

The goal of this repository is to provide documentation directly from upstream sources, reducing reliance on potentially outdated model knowledge.

## Purpose

- Store version-specific documentation snapshots.
- Provide up-to-date references for AI and LLM systems.
- Maintain consistency between development dependencies and documentation.
- Reduce the risk of using deprecated APIs, outdated examples, or unsupported features.
- Enable Retrieval-Augmented Generation (RAG) workflows using official documentation.

---

## Repository Structure

```text
.
├── cpp/
├── daisyui/
├── express/
├── scripts/
│   ├── add.sh
│   ├── add.bat
│   └── sync_cpp.py
├── sources.txt
└── README.md
```

Each documentation source is downloaded directly from its upstream repository using Git sparse checkout.

C++ documentation is synced via `scripts/sync_cpp.py` from cppreference.com (CC-BY-SA licensed).

---

## Documentation Sources

| Library      | Version    | Updated    | Local Path     | Source                                               |
| ------------ | ---------- | ---------- | -------------- | ---------------------------------------------------- |
| Express.js   | 4.x / 5.x  | 2026-06-21 | `express/`     | https://github.com/expressjs/expressjs.com           |
| DaisyUI      | 5.5.23     | 2026-06-21 | `daisyui/`     | https://github.com/saadeghi/daisyui                  |
| React.js     | 19.2       | 2026-06-22 | `reactjs/`     | https://github.com/reactjs/react.dev.git             |
| Next.js      | 16.2.9     | 2026-06-22 | `nextjs/`      | https://github.com/vercel/next.js.git                |
| Astro        | 6.4.8      | 2026-06-22 | `astro/`       | https://github.com/withastro/docs.git                |
| TailwindCSS  | 4.3        | 2026-06-22 | `tailwindcss/` | https://github.com/tailwindlabs/tailwindcss.com.git  |
| Node.js      | 26.3.1     | 2026-06-22 | `nodejs/`      | https://github.com/nodejs/node.git                   |
| C++ (cppref) | latest     | 2026-06-22 | `cpp/`         | https://en.cppreference.com (CC-BY-SA)               |
| CMake        | 4.3.4      | 2026-06-22 | `cmake/`       | https://github.com/Kitware/CMake.git                 |
| Cloudflare   | production | 2026-06-28 | `cloudflare/`  | https://github.com/cloudflare/cloudflare-docs.git    |
| Supabase     | v1.26.05   | 2026-06-28 | `supabase/`    | https://github.com/supabase/supabase.git             |
| Drizzle ORM  | main       | 2026-06-28 | `drizzle-orm/` | https://github.com/drizzle-team/drizzle-orm-docs.git |
| ENet         | v1.3.18    | 2026-06-28 | `enet/`        | https://github.com/lsalzman/enet.git                 |

---

## Source Configuration

Documentation sources are defined in `sources.txt`.

Format:

```text
name|repository|ref|path|mode
```

Example:

```text
# name|repo|ref|sparse_path|mode

daisyui|https://github.com/saadeghi/daisyui.git|v5.5.23|packages/docs|archive
express|https://github.com/expressjs/expressjs.com.git|main|src/content/docs/en|archive
```

### Fields

| Field         | Description            |
| ------------- | ---------------------- |
| `name`        | Local directory name   |
| `repo`        | Git repository URL     |
| `ref`         | Branch, tag, or commit |
| `sparse_path` | Directory to retrieve  |
| `mode`        | Synchronization mode   |

### Modes

| Mode      | Description                          |
| --------- | ------------------------------------ |
| `git`     | Keep Git metadata for future updates |
| `archive` | Remove `.git` after synchronization  |
| `script`  | Custom script-based synchronization  |

---

## Adding / Synchronizing

### Linux / macOS

```bash
./scripts/add.sh
```

### Windows

```bat
scripts\add.bat
```

The synchronization scripts:

1. Clone the upstream repository using sparse checkout.
2. Download only the specified documentation directory.
3. Checkout the requested branch or tag.
4. Optionally remove Git metadata when using `archive` mode.

C++ documentation is synced separately via `scripts/sync_cpp.py`, which fetches raw wiki text from cppreference.com and converts it to Markdown files in `cpp/`.

---

## Usage Rules

1. Use documentation in this repository as the primary reference source.
2. Prefer documentation over model memory when conflicts occur.
3. Verify library versions before generating code or recommendations.
4. Treat upstream documentation as the source of truth.
5. Do not assume undocumented behavior.
6. Avoid generating APIs, options, commands, or configuration values that are not explicitly documented.

---

## Instructions for AI / LLM Systems

When this repository is provided as context:

1. Read the relevant documentation before answering.
2. Prioritize documentation over model knowledge.
3. Follow documented behavior when conflicts exist.
4. Clearly state limitations when information cannot be found.
5. Avoid hallucinating APIs or undocumented features.
6. Prefer examples and patterns described by the documentation.
7. Reference documentation paths whenever possible.

---

## Date Format

All dates use:

```text
YYYY-MM-DD
```

Example:

```text
2026-06-21
```

---

## Disclaimer

The documentation stored in this repository is a snapshot of upstream sources at the listed update date.

Newer versions may exist in the original repositories and may contain changes not reflected in this repository.
