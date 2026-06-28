---
title: std::basic_stacktrace::swap
type: Diagnostics
source: https://en.cppreference.com/w/cpp/utility/basic_stacktrace/swap
---

ddcl | since=c++23 |
void swap( basic_stacktrace& other ) noexcept(/* see below */);
Exchanges the contents of the container with those of `other`. Does not invoke any move, copy, or swap operations on individual `stacktrace_entry` objects.
If `std::allocator_traits<allocator_type>::propagate_on_container_swap::value` is true, then the allocators are exchanged using an unqualified call to non-member `swap`. Otherwise, they are not swapped (and if `1=get_allocator() != other.get_allocator()`, the behavior is undefined).

## Parameters


### Parameters


## Return value

(none)

## Exceptions

noexcept|std::allocator_traits<Allocator>::propagate_on_container_swap::value
std::allocator_traits<Allocator>::is_always_equal::value

## Complexity

Constant.

## Example

