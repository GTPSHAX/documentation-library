---
title: std::basic_spanbuf::swap
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_spanbuf/swap
---

ddcl|since=c++23|
void swap( basic_spanbuf& rhs );
Swaps the state of `*this` and `rhs`.
Calls `std::basic_streambuf<Char, Traits>::swap(rhs)`, swaps the open mode of `*this` and `rhs`, and then makes them use the underlying buffer of each other.

## Parameters


### Parameters

- `rhs` - another `basic_stringbuf`

## Return value

(none)

## Notes

This function is called automatically when swapping stream objects, it is rarely necessary to call it directly.

## Example

