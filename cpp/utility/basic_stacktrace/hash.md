---
title: std::hash<std::basic_stacktrace>
type: Diagnostics
source: https://en.cppreference.com/w/cpp/utility/basic_stacktrace/hash
---

ddcl | header=stacktrace | since=c++23 |
template< class Allocator > struct hash<std::basic_stacktrace<Allocator>>;
The template specialization of `std::hash` for `std::basic_stacktrace` allows users to obtain hashes of values of type `std::basic_stacktrace`.
`operator()` of this specialization is noexcept.

## Example

