---
title: std::generator::operator=
type: Utilities
source: https://en.cppreference.com/w/cpp/coroutine/generator/operator=
---

ddcl|since=c++23|1=
generator& operator=( generator other ) noexcept;
Replaces the contents of the generator object. Equivalent to:
box|
`std::``cpp/utility/swap``(``,``other.``);`<br>
`std::``cpp/utility/swap``(``,``other.``);`

## Parameters


### Parameters

- `other` - another generator to be moved from

## Return value

`*this`

## Complexity


## Notes

Iterators previously obtained from `other` are not invalidated &ndash; they become iterators into `*this`.
This assignment operator is technically a copy assignment operator, although `std::generator` is only move assignable.

## Example

