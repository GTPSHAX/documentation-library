---
title: std::range_format
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/format/range_format
---

ddcl|header=format|since=c++23|1=
enum class range_format {
disabled,
map,
set,
sequence,
string,
debug_string
};
Specifies how a range should be formatted.

## Constants


| Item | Description |
|------|-------------|
| **Enumerator** | Meaning |
| dsc|`map`|allows to format range as map representation with modified brackets `"{"`, c|"}" and separator `": "` for underlying  types in the following format:<br>{ *key-1* : *value-1*, ..., *key-n* : *value-n* } | |
| dsc|`set`|allows to format range as set representation with modified brackets `"{"` and c|"}" in the following format:<br>{ *key-1*, ..., *key-n* } | |
| dsc|`sequence`|allows to format range as sequence representation with default brackets `"["`, `"]"` and separator `", "` in the following format:<br>[ *element-1*, ..., *element-n* ] | |


## See also


| cpp/utility/format/dsc formatter | (see dedicated page) |
| cpp/utility/format/dsc format_kind | (see dedicated page) |

