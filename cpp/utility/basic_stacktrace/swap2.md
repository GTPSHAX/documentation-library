---
title: std::swap(std::basic_stacktrace)
type: Diagnostics
source: https://en.cppreference.com/w/cpp/utility/basic_stacktrace/swap2
---

ddcl|header=stacktrace|since=c++23|
template< class Allocator >
void swap( std::basic_stacktrace<Allocator>& lhs, std::basic_stacktrace<Allocator>& rhs )
noexcept(noexcept(lhs.swap(rhs)));
Specializes the `std::swap` algorithm for `std::basic_stacktrace`. Swaps the contents of `lhs` and `rhs`. Equivalent to `lhs.swap(rhs);`.

## Parameters


### Parameters

- `lhs, rhs` - stacktraces whose contents to swap

## Return value

(none)

## Complexity

Constant.

## Example

