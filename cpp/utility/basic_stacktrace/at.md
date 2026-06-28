---
title: std::basic_stacktrace::at
type: Diagnostics
source: https://en.cppreference.com/w/cpp/utility/basic_stacktrace/at
---

ddcl | since=c++23 |
const_reference at( size_type pos ) const;
Returns a reference to the entry at specified location `pos`, with bounds checking.
If `pos` is not within the range of the stacktrace, an exception of type `std::out_of_range` is thrown.

## Parameters


### Parameters


## Return value

Reference to the requested entry.

## Exceptions

`std::out_of_range` if `1=pos >= size()`.

## Complexity

Constant.

## Example

