---
title: iter_swap(ranges::join_with_view::iterator)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/join_with_view/iterator/iter_swap
---


# iter_swapsmall|(ranges::join_with_view::''iterator'')

ddcl|since=c++23|
friend constexpr void iter_swap( const /*iterator*/& x, const /*iterator*/& y )
requires std::indirectly_swappable<ranges::iterator_t</*InnerBase*/>,
ranges::iterator_t</*PatternBase*/>>;
Applies `ranges::iter_swap` to the inner iterators as if by .

## Parameters


### Parameters

- `x, y` - iterators to the elements to swap

## See also


| cpp/iterator/ranges/dsc iter swap | (see dedicated page) |
| cpp/algorithm/dsc iter swap | (see dedicated page) |

