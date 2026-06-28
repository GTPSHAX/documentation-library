---
title: std::stacktrace_entry
type: Diagnostics
source: https://en.cppreference.com/w/cpp/utility/stacktrace_entry
---

ddcl|header=stacktrace|since=c++23|
class stacktrace_entry;
The `stacktrace_entry` class provides operations for querying information about an evaluation in a stacktrace. Each `stacktrace_entry` object is either empty, or represents an evaluation in a stacktrace.
`stacktrace_entry` models `std::regular` and `std::three_way_comparable<std::strong_ordering>`.

## Member types


## Member functions


| cpp/utility/stacktrace_entry/dsc constructor | (see dedicated page) |

#### Observers


#### Query

| cpp/utility/stacktrace_entry/dsc source_file | (see dedicated page) |
| cpp/utility/stacktrace_entry/dsc source_line | (see dedicated page) |


## Non-member functions


| cpp/utility/stacktrace_entry/operator cmp|title=operator==<br>operator<=>|notes= | |
| cpp/utility/stacktrace_entry/dsc to_string | (see dedicated page) |
| cpp/utility/stacktrace_entry/dsc operator ltlt | (see dedicated page) |


## Helper classes


| cpp/utility/stacktrace_entry/dsc hash | (see dedicated page) |
| cpp/utility/stacktrace_entry/dsc formatter | (see dedicated page) |


## Notes

`boost::stacktrace::frame` (available in [https://www.boost.org/doc/libs/release/doc/html/stacktrace.html Boost.Stacktrace]) can be used instead when `std::stacktrace_entry` is not available.

## Example

