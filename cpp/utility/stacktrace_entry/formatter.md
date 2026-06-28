---
title: std::formatter<std::stacktrace_entry>
type: Diagnostics
source: https://en.cppreference.com/w/cpp/utility/stacktrace_entry/formatter
---


# formattersmall|<std::stacktrace_entry>

ddcl|header=stacktrace|since=c++23|1=
template<>
struct formatter<std::stacktrace_entry>;
The template specialization of `std::formatter` for `std::stacktrace_entry` allows users to convert a stacktrace entry object to string using formatting functions such as `std::format`.

## Format specification

The syntax of format specifications is:

**Syntax:**

- `*width* (optional)`
*fill-and-align* and *width* have the same meaning as in standard format specification.
The formatted output matches the result of `to_string`, adjusted as appropriate for the format specifiers.

## Example


## See also


| cpp/utility/format/dsc formatter | (see dedicated page) |
| cpp/io/dsc print | (see dedicated page) |

