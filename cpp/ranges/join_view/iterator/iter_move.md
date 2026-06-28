---
title: iter_move(ranges::join_view::iterator)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/join_view/iterator/iter_move
---


# iter_movesmall|(ranges::join_view::''iterator'')


```cpp
dcl|since=c++20|
friend constexpr decltype(auto) iter_move( const /*iterator*/& i )
noexcept( /*see below*/ );
```

Casts the result of dereferencing the underlying iterator  to its associated rvalue reference type.

## Parameters


### Parameters

- `i` - iterator

## Return value

Equivalent to: `1=ranges::iter_move(i.inner_)`.

## Exceptions


## See also


| cpp/iterator/ranges/dsc iter_move | (see dedicated page) |

