---
title: std::swap(std::basic_filebuf)
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_filebuf/swap2
---


```cpp
dcl|since=c++11|
template< class CharT, class Traits >
void swap( std::basic_filebuf<CharT,Traits>& lhs,
std::basic_filebuf<CharT,Traits>& rhs );
```

Overloads the `std::swap` algorithm for `std::basic_filebuf`. Exchanges the state of `lhs` with that of `rhs`. Effectively calls `lhs.swap(rhs)`.

## Parameters


### Parameters

- `lhs, rhs` - `std::basic_filebuf` objects whose states to swap

## Return value

(none)

## Example


## See also


| cpp/io/basic_filebuf/dsc swap | (see dedicated page) |
| cpp/algorithm/dsc swap | (see dedicated page) |

