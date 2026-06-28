---
title: std::basic_stacktrace::~basic_stacktrace
type: Diagnostics
source: https://en.cppreference.com/w/cpp/utility/basic_stacktrace/~basic_stacktrace
---

ddcl | since=c++23 |
~basic_stacktrace();
Destructs the `basic_stacktrace`. The destructors of the `std::stacktrace_entry` objects it holds are called and the used storage is deallocated.

## Complexity

Linear in the size of the `basic_stacktrace`.
