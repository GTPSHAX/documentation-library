---
title: std::swap(std::basic_regex)
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/basic_regex/swap2
---

ddcl|since=c++11|
template< class CharT, class Traits >
void swap( basic_regex<CharT, Traits>& lhs, basic_regex<CharT, Traits>& rhs ) noexcept;
Overloads the `std::swap` algorithm for `std::basic_regex`. Exchanges the state of `lhs` with that of `rhs`. Effectively calls `lhs.swap(rhs)`.

## Parameters


### Parameters

- `lhs, rhs` - regular expressions to swap

## Return value

(none)

## Example


## See also


| cpp/regex/basic_regex/dsc swap | (see dedicated page) |

