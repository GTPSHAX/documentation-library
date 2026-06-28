---
title: std::swap(std::basic_spanbuf)
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_spanbuf/swap2
---

ddcl|header=spanstream|since=c++23|
template< class CharT, class Traits >
void swap( std::basic_spanbuf<CharT, Traits>& lhs,
std::basic_spanbuf<CharT, Traits>& rhs );
Overloads the `std::swap` algorithm for `std::basic_spanbuf`. Exchanges the state of `lhs` with that of `rhs`. Equivalent to `lhs.swap(rhs);`.

## Parameters


### Parameters

- `lhs, rhs` - `std::basic_spanbuf` objects whose states to swap

## Return value

(none)

## Example

