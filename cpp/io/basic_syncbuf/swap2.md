---
title: std::swap(std::basic_syncbuf)
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_syncbuf/swap2
---


```cpp
dcl|since=c++20|
template< class CharT, class Traits, class Allocator >
void swap( std::basic_syncbuf<CharT, Traits, Allocator>& lhs,
std::basic_syncbuf<CharT, Traits, Allocator>& rhs );
```

Overloads the `std::swap` algorithm for `std::basic_syncbuf`. Exchanges the state of `lhs` with that of `rhs`. Effectively calls `lhs.swap(rhs)`.

## Parameters


### Parameters

- `lhs, rhs` - `std::basic_syncbuf` objects whose states to swap

## Return value

(none)

## Example


## See also


| cpp/io/basic_syncbuf/dsc swap | (see dedicated page) |
| cpp/algorithm/dsc swap | (see dedicated page) |

