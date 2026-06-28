#!/usr/bin/env python3
"""
Synchronize C++ documentation from cppreference.com into cpp/ as Markdown.

Sources:
  - https://devdocs.io/cpp/  (entry index)
  - https://en.cppreference.com/  (raw wiki text, CC-BY-SA)

Usage:
  python3 scripts/sync_cpp.py [--limit N] [--types T] [--resume] [--delay D]
"""

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
import textwrap
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "cpp"
INDEX_URL = "https://devdocs.io/docs/cpp/index.json"
RAW_WIKI_URL = "https://en.cppreference.com/w/index.php?title={title}&action=raw"
REQUEST_DELAY = 0.3


# ---------------------------------------------------------------------------
# MediaWiki → Markdown conversion
# ---------------------------------------------------------------------------

def convert_wikitext(text: str, title_hint: str = "") -> str:
    """Convert cppreference MediaWiki source to Markdown."""
    lines = text.split("\n")
    out = []
    i = 0

    # State machines for multi-line constructs
    state = {
        "dcl": False,        # {{dcl begin}} ... {{dcl end}}
        "source": False,     # {{source|1= ... }}
        "source_buf": [],
        "example": False,    # {{example ... }} ... }}
        "example_code": [],
        "example_output": [],
        "example_sec": "none",
        "dsc": False,        # {{dsc begin}} ... {{dsc end}}
        "dsc_rows": [],
        "par": False,        # {{par begin}} ... {{par end}}
        "dr": False,         # {{dr list begin}} ... {{dr list end}}
        "dr_rows": [],
        "ftm": False,        # {{ftm begin}} ... {{ftm end}}
        "ftm_rows": [],
    "table": False,      # wiki table {| ... |}
    "sdsc": False,       # {{sdsc begin}} ... {{sdsc end}}
    "rev_multi": False,  # {{rev|...| ... }} multi-line
    "rev_buf": [],
    }

    def flush_state():
        if state["dcl"]:
            out.append("```")
            state["dcl"] = False
        if state["source"]:
            _emit_source()
            state["source"] = False
        if state["example"]:
            _emit_example()
            state["example"] = False
        if state["dsc"]:
            _emit_dsc_table()
            state["dsc"] = False
        if state["par"]:
            state["par"] = False
        if state["dr"]:
            _emit_dr_table()
            state["dr"] = False
        if state["ftm"]:
            _emit_ftm_table()
            state["ftm"] = False
        if state["table"]:
            state["table"] = False

    def _emit_source():
        code = "\n".join(state["source_buf"])
        code = textwrap.dedent(code).strip()
        if code:
            out.append("\n```cpp\n" + code + "\n```\n")

    def _emit_example():
        # Check if we have just code, or code+output
        has_code = bool(state["example_code"])
        has_output = bool(state["example_output"])
        if has_code or has_output:
            out.append("\n### Example\n")
        if has_code:
            c = textwrap.dedent("\n".join(state["example_code"])).strip()
            if c:
                out.append("```cpp\n" + c + "\n```\n")
        if has_output:
            o = textwrap.dedent("\n".join(state["example_output"])).strip()
            if o:
                out.append("\n**Output:**\n```\n" + o + "\n```\n")

    def _emit_dsc_table():
        rows = state["dsc_rows"]
        if not rows:
            return
        has_header = any(
            line.startswith("| **") for line in rows
        )
        out.append("\n")
        if any("---" in r for r in rows):
            out.extend(rows)
        elif has_header:
            out.append("| Item | Description |")
            out.append("|------|-------------|")
            out.extend(rows)
        else:
            out.extend(rows)
        out.append("")

    def _emit_dr_table():
        rows = state["dr_rows"]
        if rows:
            out.append("\n### Defect Reports\n")
            out.append("| WG | Std | Before | After |")
            out.append("|----|------|--------|-------|")
            out.extend(rows)
            out.append("")

    def _emit_ftm_table():
        rows = state["ftm_rows"]
        if rows:
            out.append("\n### Feature Test Macros\n")
            out.append("| Macro | Value | Std | Description |")
            out.append("|-------|-------|-----|-------------|")
            out.extend(rows)
            out.append("")

    while i < len(lines):
        raw = lines[i]

        # ------------------------------------------------------------------
        # Multi-line state handlers
        # ------------------------------------------------------------------

        # ---- dcl begin ----
        if "{{dcl begin}}" in raw:
            flush_state()
            state["dcl"] = True
            out.append("\n```cpp")
            i += 1
            continue

        if state["dcl"]:
            if "{{dcl end}}" in raw:
                if "dcl_buf" in state and state["dcl_buf"]:
                    out.extend(state["dcl_buf"])
                    state["dcl_buf"] = []
                out.append("```\n")
                state["dcl"] = False
                i += 1
                continue

            if "dcl_buf" not in state:
                state["dcl_buf"] = []

            # Check for dcl header
            if "{{dcl header|" in raw:
                m = re.search(r"\{\{dcl header\|([^}]+)\}\}", raw)
                if m:
                    state["dcl_buf"].append(f'\n**Header:** `<`{m.group(1)}`>`')
                i += 1
                continue

            # Check for {{dcl|...}} start
            if "{{dcl" in raw:
                # Extract content after the last | before }}
                # Multi-line dcl: extract code between last | and }}
                # For lines like {{dcl|num=1|...|template<...>
                content = raw
                # Strip {{dcl and leading params
                content = re.sub(r"^\{\{dcl\|[^|]*\|[^|]*\|?", "", content)
                content = re.sub(r"^\{\{dcl\|[^|]*\|?", "", content)
                content = content.strip()
                if content.startswith("template") or content.startswith("void") or content.startswith("int") or content.startswith("std"):
                    # This line has actual code
                    content = content.replace("}}", "")
                    content = _strip_inline_templates(content)
                    content = content.strip()
                    if content:
                        state["dcl_buf"].append(content)
                # else: it's just template params, content will come on next lines
                i += 1
                continue

            # Check for }} ending a dcl template on this line
            if "}}" in raw and raw.strip().startswith("template"):
                # Code line followed by }}
                content = raw.replace("}}", "").strip()
                content = _strip_inline_templates(content)
                if content:
                    state["dcl_buf"].append(content)
                i += 1
                continue

            # Check for lines that start after dcl params (no {{dcl prefix)
            # These are continuation lines of multi-line dcl templates
            if not raw.strip().startswith("{{") and not raw.strip().startswith("}}"):
                line = raw.rstrip()
                if line.strip():
                    state["dcl_buf"].append(line)
                i += 1
                continue

            i += 1
            continue

        # ---- source block ----
        if "{{source|" in raw and "}}" not in raw[raw.index("{{source|"):]:
            flush_state()
            state["source"] = True
            state["source_buf"] = []
            # extract content after {{source|1=
            rest = re.sub(r"^.*?\{\{source\|(?:1=)?", "", raw)
            if rest:
                state["source_buf"].append(rest)
            i += 1
            continue
        # inline {{source|...}}
        m = re.search(r"\{\{source\|(?:1=)?([^}]*)\}\}", raw)
        if m:
            code = m.group(1).strip()
            if code:
                out.append("\n```cpp\n" + code.replace("\\n", "\n") + "\n```\n")
            i += 1
            continue

        if state["source"]:
            if "}}" in raw:
                before, _, after = raw.partition("}}")
                if before.strip():
                    state["source_buf"].append(before)
                _emit_source()
                state["source"] = False
                # process 'after' as new line? Usually empty.
                i += 1
                continue
            state["source_buf"].append(raw)
            i += 1
            continue

        # ---- example block ----
        if "{{example" in raw:
            flush_state()
            # Check inline {{example|...}}
            if "}}" in raw and not raw.strip().startswith("{{example") and raw.strip().endswith("}}"):
                # inline
                m = re.search(r"\|code=(.*?)(?:\|output=(.*?))?\}\}", raw)
                if m:
                    code = m.group(1).strip() if m.group(1) else ""
                    output = m.group(2).strip() if m.group(2) else ""
                    if code or output:
                        out.append("\n### Example\n")
                        if code:
                            out.append("```cpp\n" + code.replace("\\n", "\n").strip() + "\n```\n")
                        if output:
                            out.append("\n**Output:**\n```\n" + output.replace("\\n", "\n").strip() + "\n```\n")
                i += 1
                continue
            state["example"] = True
            state["example_code"] = []
            state["example_output"] = []
            state["example_sec"] = "none"
            i += 1
            continue

        if state["example"]:
            # end
            if "}}" in raw and not raw.strip().startswith("|"):
                before, _, after = raw.partition("}}")
                if before.strip():
                    if state["example_sec"] == "code":
                        state["example_code"].append(before)
                    elif state["example_sec"] == "output":
                        state["example_output"].append(before)
                _emit_example()
                state["example"] = False
                i += 1
                continue

            s = raw.strip()
            if s.startswith("|code="):
                state["example_sec"] = "code"
                content = s[6:]
                if content:
                    state["example_code"].append(content)
            elif s.startswith("|output="):
                state["example_sec"] = "output"
                content = s[8:]
                if content:
                    state["example_output"].append(content)
            elif s.startswith("|") or s.startswith("}}") or s.startswith("{{"):
                pass
            else:
                if state["example_sec"] == "code":
                    state["example_code"].append(raw)
                elif state["example_sec"] == "output":
                    state["example_output"].append(raw)
            i += 1
            continue

        # ---- dsc begin ----
        if "{{dsc begin}}" in raw:
            flush_state()
            state["dsc"] = True
            state["dsc_rows"] = []
            i += 1
            continue

        if state["dsc"]:
            if "{{dsc end}}" in raw:
                _emit_dsc_table()
                state["dsc"] = False
                i += 1
                continue
            self_closing = False
            # h2 → section header
            m = re.search(r"\{\{dsc h2\|([^}]+)\}\}", raw)
            if m:
                state["dsc_rows"].append(f"\n#### {m.group(1)}\n")
                i += 1
                continue
            # hitem → table header
            m = re.search(r"\{\{dsc hitem\|([^|]+)\|([^}]*)\}\}", raw)
            if m:
                state["dsc_rows"].append(f"| **{m.group(1).strip()}** | {_clean(m.group(2).strip())} |")
                i += 1
                continue
            # inc → reference
            m = re.search(r"\{\{dsc inc\|([^}]+)\}\}", raw)
            if m:
                ref = m.group(1)
                state["dsc_rows"].append(f"| {ref} | (see dedicated page) |")
                i += 1
                continue
            # Other dsc templates
            cleaned = raw
            if "{{dsc" in cleaned:
                # dsc macro const, dsc see cpp, dsc concept, dsc class, etc
                cleaned = re.sub(r"\{\{dsc [a-z_]+\|([^}]+)\}\}", r"\1", cleaned)
                cleaned = _strip_inline_templates(cleaned)
                cleaned = cleaned.strip()
                if cleaned and not cleaned.startswith("{{"):
                    state["dsc_rows"].append(f"| {cleaned} | |")
                i += 1
                continue
            # plain text in dsc context
            c = _strip_inline_templates(raw).strip()
            if c:
                state["dsc_rows"].append(f"| {c} | |")
            i += 1
            continue

        # ---- sdsc begin ----
        if "{{sdsc begin}}" in raw:
            flush_state()
            state["sdsc"] = True
            out.append("\n**Syntax:**\n")
            i += 1
            continue
        if state["sdsc"]:
            if "{{sdsc end}}" in raw:
                state["sdsc"] = False
                i += 1
                continue
            # Process sdsc line
            line = raw
            line = re.sub(r"\{\{sdsc\|[^}]*\}\}", "", line)
            # sdsc checks
            line = line.replace("{{sdsc begin}}", "").replace("{{sdsc end}}", "")
            line = _strip_inline_templates(line)
            line = line.strip()
            if line:
                # wrap as code
                out.append("- `" + line + "`")
            i += 1
            continue

        # ---- par begin ----
        if "{{par begin}}" in raw:
            flush_state()
            state["par"] = True
            out.append("\n### Parameters\n")
            i += 1
            continue
        if state["par"]:
            if "{{par end}}" in raw:
                state["par"] = False
                i += 1
                continue
            line = _strip_inline_templates(raw).strip()
            if "par range" in raw:
                m = re.search(r"par range\|([^|]*)\|([^|]*)", raw)
                if m:
                    r1, r2 = m.group(1), m.group(2)
                    rest = _strip_inline_templates(raw.split("}}")[-1] if "}}" in raw else "")
                    out.append(f"- `[{r1}, {r2})` - {rest}")
            elif "par exec pol" in raw:
                out.append("- `policy` - execution policy")
            elif "par cmp ord" in raw:
                out.append("- `comp` - comparison function")
            elif "par hreq" in raw:
                out.append("\n**Type requirements:**\n")
            elif "par req named" in raw:
                m = re.search(r"par req named\|([^|}]+)", raw)
                if m:
                    out.append(f"- `{m.group(1)}`")
            elif "par" in raw and "|" in raw:
                m = re.search(r"par\|([^|]*)\|(.*)", raw)
                if m:
                    out.append(f"- `{m.group(1).strip()}` - {_strip_inline_templates(m.group(2))}")
            elif line:
                out.append(f"- {line}")
            i += 1
            continue

        # ---- dr list ----
        if "{{dr list begin}}" in raw:
            flush_state()
            state["dr"] = True
            state["dr_rows"] = []
            i += 1
            continue
        if state["dr"]:
            if "{{dr list end}}" in raw:
                _emit_dr_table()
                state["dr"] = False
                i += 1
                continue
            m = re.search(r"dr list item\|wg=(\w+)\|dr=(\d+)\|std=([^|]*)\|before=([^|]*)\|after=([^|}]+)", raw)
            if m:
                state["dr_rows"].append(
                    f"| {m.group(1)}-{m.group(2)} | {m.group(3)} | {_clean(m.group(4))} | {_clean(m.group(5))} |"
                )
            i += 1
            continue

        # ---- ftm begin ----
        if "{{ftm begin}}" in raw:
            flush_state()
            state["ftm"] = True
            state["ftm_rows"] = []
            i += 1
            continue
        if state["ftm"]:
            if "{{ftm end}}" in raw:
                _emit_ftm_table()
                state["ftm"] = False
                i += 1
                continue
            m = re.search(r"ftm\|([^|]*)\|value=([^|]*)\|std=([^|]*)\|(.+)", raw)
            if m:
                state["ftm_rows"].append(
                    f"| `{m.group(1)}` | {m.group(2)} | {m.group(3)} | {_clean(m.group(4))} |"
                )
            i += 1
            continue

        # ---- wiki table {| ... |} ----
        if raw.strip().startswith("{|"):
            flush_state()
            state["table"] = True
            out.append("\n")
            i += 1
            continue
        if state["table"]:
            if raw.strip().startswith("|}"):
                state["table"] = False
                out.append("")
                i += 1
                continue
            if raw.strip().startswith("|") or raw.strip().startswith("!"):
                cells = re.findall(r"(?:\|\||!!|!|\|)([^|\n]*)", raw)
                cleaned_cells = [_clean(c.strip()) for c in cells]
                out.append("| " + " | ".join(cleaned_cells) + " |")
            i += 1
            continue

        # ---- multi-line {{rev|...}} block ----
        if re.match(r"^\{\{rev\|", raw) and "}}" not in raw:
            state["rev_multi"] = True
            state["rev_buf"] = []
            # Extract version info for a prefix label
            vmatch = re.search(r"(?:until|since)=c\+\+(\d+)", raw)
            if vmatch:
                ver = vmatch.group(1)
                direction = "since" if "since=" in raw else "until" if "until=" in raw else ""
                state["rev_prefix"] = f"<sup>({direction} C++{ver})</sup>"
            else:
                state["rev_prefix"] = ""
            i += 1
            continue
        if state["rev_multi"]:
            if raw.strip() == "}}":
                # Emit the cleaned rev content
                content = "\n".join(state["rev_buf"])
                content = _apply_inline_conversions(content)
                content = _strip_remaining_templates(content)
                content = content.strip()
                if content:
                    if state.get("rev_prefix"):
                        out.append(state["rev_prefix"])
                    out.append(content)
                state["rev_multi"] = False
                state["rev_buf"] = []
                i += 1
                continue
            state["rev_buf"].append(raw)
            i += 1
            continue

        # ------------------------------------------------------------------
        # Line-level processing
        # ------------------------------------------------------------------

        line = raw

        # Skip navigation / metadata templates on their own line
        nav_patterns = [
            r"^\{\{cpp/title\|[^}]*\}\}$",
            r"^\{\{cpp/[\w/]+/navbar\}\}$",
            r"^\{\{cpp/[\w/]+/navbar\}\}$",
            r"^\{\{cpp/[\w/]+/title\}\}$",
            r"^\{\{langlinks\|[^}]*\}\}$",
            r"^\{\{todo\|[^}]*\}\}$",
        ]
        is_nav = any(re.match(p, line) for p in nav_patterns)
        if is_nav:
            i += 1
            continue

        # Handle {{title|...}} standalone
        if re.match(r"^\{\{title\|", line):
            m = re.search(r"\{\{title\|([^}]+)\}\}", line)
            if m:
                out.append(f"\n# {_clean(m.group(1))}\n")
            i += 1
            continue

        # {{cpp/title|...}} → heading
        if re.search(r"\{\{cpp/title\|", line):
            m = re.search(r"\{\{cpp/title\|([^}]+)\}\}", line)
            if m:
                t = _clean(m.group(1))
                out.append(f"\n# {t}\n")
                line = re.sub(r"\{\{cpp/title\|[^}]*\}\}", "", line)

        # Strip known nav templates
        if re.search(r"\{\{cpp/\S*?/navbar\}\}", line):
            line = re.sub(r"\{\{cpp/\S*?/navbar\}\}", "", line)
        # {{cpp/.../title}}
        if re.search(r"\{\{cpp/[\w/]+/title\}\}", line):
            line = re.sub(r"\{\{cpp/[\w/]+/title\}\}", "", line)

        # {{dcl header}} not already in dcl block
        line = re.sub(r"\{\{dcl header\|([^}]+)\}\}", r'**Header:** `<`\1`>`', line)

        # Headings: ===...=== → ##...##
        hm = re.match(r"^(={2,})\s*(.*?)\s*\1\s*$", line)
        if hm:
            level = len(hm.group(1)) - 1  # === → ##, ==== → ###
            heading_text = _clean(hm.group(2).strip())
            out.append(f"\n{'#' * level} {heading_text}\n")
            i += 1
            continue

        # @1@, @2,4@ → numbered list
        if re.match(r"@[\d,]+\s*@", line.strip()):
            line = re.sub(r"@(\d[\d,]*)\s*@\s*", r"\1. ", line)

        # Apply all inline template conversions
        line = _apply_inline_conversions(line)

        # Final strip of any remaining {{...}} artifacts
        line = _strip_remaining_templates(line)

        # Remove lines that are just whitespace after cleaning
        line = line.strip()
        if line:
            out.append(line)

        i += 1

    flush_state()
    return "\n".join(out)


def _clean(text: str) -> str:
    """Clean a string by applying inline conversions and removing templates."""
    text = _apply_inline_conversions(text)
    text = _strip_remaining_templates(text)
    return text.strip()


def _apply_inline_conversions(text: str) -> str:
    """Apply inline template → Markdown conversions."""
    t = text

    # {{range|first|last}} → [first, last)
    t = re.sub(r"\{\{range\|([^}|]+)\|([^}]+)\}\}", r"[\1, \2)", t)

    # {{c|...}} → `...`
    t = re.sub(r"\{\{c\|([^}]+)\}\}", r"`\1`", t)
    t = re.sub(r"\{\{c/core\|([^}]+)\}\}", r"`\1`", t)

    # {{lc|...}} → `...`
    t = re.sub(r"\{\{lc\|([^}]+)\}\}", r"`\1`", t)

    # {{tt|...}} → `...`
    t = re.sub(r"\{\{tt\|([^}]+)\}\}", r"`\1`", t)
    # {{ttb|1=...}} or {{ttb|...}} → **`...`**
    t = re.sub(r"\{\{ttb\|1=([^}]*)\}\}", r"**`\1`**", t)
    t = re.sub(r"\{\{ttb\|([^}]+)\}\}", r"**`\1`**", t)

    # {{ltt|...}} → `...` (list item template)
    t = re.sub(r"\{\{ltt\|([^}]+)\}\}", r"`\1`", t)

    # {{cmark|...}} → remove
    t = re.sub(r"\{\{c mark\|[^}]*\}\}", "", t)

    # Mark: since c++11, constexpr since c++20, deprecated c++17, etc
    t = re.sub(r"\{\{mark since c\+\+(\d+)\}\}", r"<sup>(C++\1)</sup>", t)
    t = re.sub(r"\{\{mark constexpr since c\+\+(\d+)\}\}", r"<sup>(constexpr C++\1)</sup>", t)
    t = re.sub(r"\{\{mark deprecated c\+\+(\d+)\}\}", r"<sup>(deprecated C++\1)</sup>", t)
    t = re.sub(r"\{\{mark optional\|[^}]*\}\}", "", t)
    t = re.sub(r"\{\{mark until c\+\+(\d+)\}\}", r"<sup>(until C++\1)</sup>", t)
    t = re.sub(r"\{\{mark\s*\|?.*?\}\}", "", t)

    # {{rev inl|since=c++11|...}} / {{rev inl|until=c++11|...}}
    t = re.sub(r"\{\{rev inl\|since=c\+\+(\d+)\|([^}]*)\}\}", r"<sup>(since C++\1)</sup> \2", t)
    t = re.sub(r"\{\{rev inl\|until=c\+\+(\d+)\|([^}]*)\}\}", r"<sup>(until C++\1)</sup> \2", t)
    # {{rev|since=c++11|...}} / {{rev|until=c++11|...}}
    t = re.sub(r"\{\{rev\|since=c\+\+(\d+)\|([^}]*)\}\}", r"<sup>(since C++\1)</sup> \2", t)
    t = re.sub(r"\{\{rev\|until=c\+\+(\d+)\|([^}]*)\}\}", r"<sup>(until C++\1)</sup> \2", t)

    # {{rrev|since=c++20|...}} or {{rrev|multi|...}}
    # Just extract the content
    t = re.sub(r"\{\{rrev\|[^}]*\|rev1=([^|]*)\|rev2=([^}]*)\}\}", r"\1 / \2", t)
    t = re.sub(r"\{\{rrev\|since=c\+\+(\d+)\|([^}]*)\}\}", r"<sup>(since C++\1)</sup> \2", t)
    t = re.sub(r"\{\{rrev\|[^}]*\}\}", "", t)

    # {{named req|...}} → *...*
    t = re.sub(r"\{\{named req\|([^}]+)\}\}", r"*\1*", t)

    # {{rlp|X}} → X, {{rlp|X|Y}} → Y, {{rlpt|X}} → X, {{rlpt|X|Y}} → Y
    t = re.sub(r"\{\{rlp[t]?\|([^}|]+)\|([^}]+)\}\}", r"`\2`", t)
    t = re.sub(r"\{\{rlp[t]?\|([^}]+)\}\}", r"`\1`", t)

    # {{math|...}} → $...$
    t = re.sub(r"\{\{math\|([^}]+)\}\}", r"$\1$", t)
    t = re.sub(r"\{\{mathjax-or\|[^}]*\}\}", "", t)

    # {{enwiki|...}} → [link]
    t = re.sub(r"\{\{enwiki\|([^}]+)\}\}", r"[\1](https://en.wikipedia.org/wiki/\1)", t)
    # {{wg21|...}} → `...`
    t = re.sub(r"\{\{wg21\|([^}]+)\}\}", r"`\1`", t)

    # {{todo|...}} → note
    t = re.sub(r"\{\{todo\|([^}]*)\}\}", r"> **TODO:** \1", t)

    # {{cpp/is_constexpr|...}} → remove
    t = re.sub(r"\{\{cpp/is_constexpr\|[^}]*\}\}", "", t)

    # {{spar|...}} → *...*
    t = re.sub(r"\{\{spar\|([^}]+)\}\}", r"*\1*", t)
    t = re.sub(r"\{\{spar optional\|([^}]+)\}\}", r"*\1* (optional)", t)
    t = re.sub(r"\{\{spar sep\|([^}]+)\}\}", r"\1", t)

    # {{anchor|...}} → invisible anchor
    t = re.sub(r"\{\{anchor\|[^}]*\}\}", "", t)

    # {{rev begin}}/{{rev end}} markers
    t = re.sub(r"\{\{rev begin\}\}", "", t)
    t = re.sub(r"\{\{rev end\}\}", "", t)

    # {{dsc see cpp|...}} and {{dsc see c|...}}
    t = re.sub(r"\{\{dsc see cpp\|[^}]*\}\}", "", t)
    t = re.sub(r"\{\{dsc see c\|[^}]*\}\}", "", t)

    # {{cpp/...}} nav template remnants
    t = re.sub(r"\{\{cpp/[\w/]+/navbar\}\}", "", t)
    t = re.sub(r"\{\{cpp/[\w/]+/title\}\}", "", t)

    # {{edit section|...}}
    t = re.sub(r"\{\{edit section\|[^}]*\}\}", "", t)

    # [[...]] wiki links → plain text
    t = re.sub(r"\[\[([^|\]]+)\]\]", r"\1", t)
    t = re.sub(r"\[\[([^|\]]+)\|([^\]]+)\]\]", r"\2", t)

    # <references/>, <ref>, </ref>
    t = re.sub(r"<references\s*/>", "", t)
    t = re.sub(r"<ref[^>]*>[^<]*</ref>", "", t)
    t = re.sub(r"<ref\s+name\s*=\s*\"[^\"]*\"\s*/>", "", t)

    # HTML comments
    t = re.sub(r"<!--.*?-->", "", t)
    t = t.replace("<!---->", "")
    # stray <! and > without proper comment
    t = re.sub(r"<!----?>", "", t)

    # {{!}} → |
    t = t.replace("{{!}}", "|")
    # {v|N,M} version references
    t = re.sub(r"\{v\|[\d,]+\}", "", t)

    # Handle rev/rev inl with complex nested content (greedy multi-pass)
    t = re.sub(r"\{\{rev inl\|[^}]*\}\}", "", t)
    t = re.sub(r"\{\{rev\|[^}]*\}\}", "", t)

    return t


def _strip_inline_templates(text: str) -> str:
    """Remove all remaining {{...}} template calls from text."""
    t = text
    t = _apply_inline_conversions(t)
    t = _strip_remaining_templates(t)
    return t


def _strip_remaining_templates(text: str) -> str:
    """Aggressively remove any remaining {{...}} constructs."""
    t = text
    # Remove simple {{...}} that contain no nested braces
    while re.search(r"\{\{[^{}]*\}\}", t):
        t = re.sub(r"\{\{[^{}]*\}\}", "", t)
    # Handle nested {{...}} - remove outermost
    while re.search(r"\{\{[^{}]*\{[^{}]*\}[^{}]*\}", t):
        t = re.sub(r"\{\{[^{}]*\{[^{}]*\}[^{}]*\}", "", t)
    # Remove any remaining dangling braces
    t = t.replace("{{", "").replace("}}", "")
    # Clean @@, {} artifacts from version ref removal (only standalone)
    t = re.sub(r"@@\s*", "", t)
    # Remove leftover {} only when surrounded by non-code chars (template remnant)
    t = re.sub(r"(?<=[,.(\s]){}\s*(?=[,.\s)])", "", t)
    t = re.sub(r",\s*,", ", ", t)  # double comma from template removal
    t = re.sub(r"^(\d+),\s*\.", r"\1.", t)  # "2, ." → "2."
    return t


# ---------------------------------------------------------------------------
# Fetch & save
# ---------------------------------------------------------------------------

def fetch_raw(title: str) -> str | None:
    """Fetch raw wiki text from cppreference.com."""
    url = RAW_WIKI_URL.format(title=title)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "center-docs-sync/1.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read().decode("utf-8")
            if data.strip().startswith("<!") or data.strip().startswith("<html"):
                return None
            if "Creates a new account" in data or "There is no page" in data:
                return None
            return data
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        print(f"  HTTP {e.code} for {title}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"  Error {title}: {e}", file=sys.stderr)
        return None


def devdocs_path_to_cppref(path: str) -> str:
    """Convert DevDocs path to cppreference.com page title."""
    return f"cpp/{path}"


def save_markdown(path: str, content: str) -> Path:
    """Save markdown file."""
    fp = OUTPUT_DIR / f"{path}.md"
    fp.parent.mkdir(parents=True, exist_ok=True)
    fp.write_text(content, encoding="utf-8")
    return fp


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def load_index() -> list:
    """Load DevDocs C++ index (cached)."""
    cache = BASE_DIR / ".cache" / "cpp_index.json"
    if cache.exists():
        with open(cache) as f:
            return json.load(f)["entries"]
    print("Downloading DevDocs C++ index...", file=sys.stderr)
    req = urllib.request.Request(INDEX_URL, headers={"User-Agent": "center-docs-sync/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    cache.parent.mkdir(parents=True, exist_ok=True)
    with open(cache, "w") as f:
        json.dump(data, f)
    print(f"  {len(data['entries'])} entries cached", file=sys.stderr)
    return data["entries"]


def main():
    parser = argparse.ArgumentParser(description="Sync C++ docs from cppreference.com")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--types", type=str, default=None)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--delay", type=float, default=REQUEST_DELAY)
    args = parser.parse_args()

    entries = load_index()

    if args.types:
        allowed = {t.strip() for t in args.types.split(",")}
        entries = [e for e in entries if e["type"] in allowed]
        print(f"Filtered: {len(entries)} entries of types {allowed}", file=sys.stderr)

    if args.limit:
        entries = entries[:args.limit]

    print(f"Starting: {len(entries)} entries", file=sys.stderr)
    tc = {}
    for e in entries:
        tc[e["type"]] = tc.get(e["type"], 0) + 1
    print(f"Types: {tc}", file=sys.stderr)

    ok = skip = fail = 0
    for idx, entry in enumerate(entries, 1):
        path, name, etype = entry["path"], entry["name"], entry["type"]
        fp = OUTPUT_DIR / f"{path}.md"

        if args.resume and fp.exists():
            skip += 1
            if idx % 200 == 0:
                print(f"  [{idx}/{len(entries)}] ok={ok} skip={skip} fail={fail}", file=sys.stderr)
            continue

        title_cppref = devdocs_path_to_cppref(path)
        raw = fetch_raw(title_cppref)
        if raw is None:
            fail += 1
            if fail <= 5:
                print(f"  NOT FOUND: {title_cppref}", file=sys.stderr)
            time.sleep(args.delay)
            continue

        md = convert_wikitext(raw, title_hint=name)
        # Clean up excessive blank lines
        md = re.sub(r"\n{4,}", "\n\n\n", md)
        md = f"""---
title: {name}
type: {etype}
source: https://en.cppreference.com/w/{title_cppref}
---

{md}
"""
        save_markdown(path, md)
        ok += 1
        if idx % 50 == 0 or idx == len(entries):
            print(f"  [{idx}/{len(entries)}] ok={ok} skip={skip} fail={fail}", file=sys.stderr)
        time.sleep(args.delay)

    print(f"\nDone: {ok} synced, {skip} skipped, {fail} failed", file=sys.stderr)


if __name__ == "__main__":
    main()
