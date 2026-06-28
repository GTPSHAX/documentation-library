---
title: iter_swap(ranges::join_view::iterator)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/join_view/iterator/iter_swap
---


# iter_swapsmall|(ranges::join_view::''iterator'')


```cpp
dcl|since=c++20|
friend constexpr void iter_swap( const /*iterator*/& x, const /*iterator*/& y )
noexcept( /*see below*/ )
requires std::indirectly_swappable<InnerIter>;
```

Swaps the objects pointed to by two underlying iterators (denoted as ).
Equivalent to: `ranges::iter_swap(x.inner_, y.inner_);`.

## Parameters


### Parameters

- `x, y` - iterators

## Return value

(none)

## Exceptions


## See also


| cpp/iterator/ranges/dsc iter swap | (see dedicated page) |
| cpp/algorithm/dsc iter swap | (see dedicated page) |

