---
title: std::stacktrace_entry::stacktrace_entry
type: Diagnostics
source: https://en.cppreference.com/w/cpp/utility/stacktrace_entry/stacktrace_entry
---


```cpp
dcl | num=1 | since=c++23 |
constexpr stacktrace_entry() noexcept;
dcl | num=2 | since=c++23 |
constexpr stacktrace_entry( const stacktrace_entry& other ) noexcept;
```

1. Default constructor. Creates an empty `stacktrace_entry`.
2. Copy constructor. Creates a copy of `other`.

## Parameters


### Parameters


## Notes

A non-empty `stacktrace_entry` can be obtained from a `std::basic_stacktrace` created by `std::basic_stacktrace::current` or a copy of such `std::basic_stacktrace`.

## Example

