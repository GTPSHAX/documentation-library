---
title: std::hash<std::stacktrace_entry>
type: Diagnostics
source: https://en.cppreference.com/w/cpp/utility/stacktrace_entry/hash
---

ddcl | header=stacktrace | since=c++23 |
template<> struct hash<std::stacktrace_entry>;
The template specialization of `std::hash` for `std::stacktrace_entry` allows users to obtain hashes of values of type `std::stacktrace_entry`.
`operator()` of this specialization is noexcept.

## Example

