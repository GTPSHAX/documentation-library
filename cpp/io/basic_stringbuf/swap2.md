---
title: std::swap(std::basic_stringbuf)
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_stringbuf/swap2
---


```cpp
**Header:** `<`sstream`>`
dcl rev multi
|since1=c++11|dcl1=
template< class CharT, class Traits, class Alloc >
void swap( std::basic_stringbuf<CharT,Traits,Alloc>& lhs,
std::basic_stringbuf<CharT,Traits,Alloc>& rhs );
|since2=c++20|dcl2=
template< class CharT, class Traits, class Alloc >
void swap( std::basic_stringbuf<CharT,Traits,Alloc>& lhs,
std::basic_stringbuf<CharT,Traits,Alloc>& rhs )
noexcept(noexcept(lhs.swap(rhs)));
```

Overloads the `std::swap` algorithm for `std::basic_stringbuf`. Exchanges the state of `lhs` with that of `rhs`. Effectively calls `lhs.swap(rhs)`.

## Parameters


### Parameters

- `lhs, rhs` - `std::basic_stringbuf` objects whose states to swap

## Return value

(none)

## Example


## See also


| cpp/io/basic_stringbuf/dsc swap | (see dedicated page) |
| cpp/algorithm/dsc swap | (see dedicated page) |

