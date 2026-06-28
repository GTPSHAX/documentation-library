---
title: std::stacktrace_entry::source_line
type: Diagnostics
source: https://en.cppreference.com/w/cpp/utility/stacktrace_entry/source_line
---

ddcl | since=c++23 |
std::uint_least32_t source_line() const;
Returns a 1-based line number that lexically relates to the evaluation represented by `*this`, or 0 on failure other than allocation failure, e.g. when `*this` is empty.
Either `source_file` returns the presumed source file name and `source_line` returns the presumed line number, or `source_file` returns the actual source file name and `source_line` returns the actual line number.

## Parameters

(none)

## Return value

The line number specified above on success, 0 on failure other than allocation failure.

## Exceptions

Throws `std::bad_alloc` if memory for the internal data structures cannot be allocated.

## Notes

The presumed line number is what the predefined macro `cpp/preprocessor/replace|__LINE__` expands to, and can be changed by the `cpp/preprocessor/line|#line` directive.
> **TODO:** definition of "actual line number" is missing (
This function is not required to be `noexcept` because getting source line requires allocation on some platforms.

## Example

