---
title: std::chrono::tzdb_list::erase_after
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/tzdb_list/erase_after
---

ddcl|since=c++20|
const_iterator erase_after( const_iterator p );
Erases the `std::chrono::tzdb` referred to by the iterator following `p`.
No pointers, references, or iterators are invalidated except for those referring to the erased element.

## Parameters


### Parameters

- `p` - an iterator to the position to erase after

## Return value

An iterator pointing to the element following the erased element, or  if no such element exists.

## Notes

`tzdb_list` is intended to be implementable as a singly linked list, and its interface resembles that of `std::forward_list`. It has no `before_begin()`, however, and so it is not possible to erase the first element.
