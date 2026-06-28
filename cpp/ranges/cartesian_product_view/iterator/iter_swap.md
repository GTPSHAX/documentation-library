---
title: iter_swap(ranges::cartesian_product_view::iterator)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/cartesian_product_view/iterator/iter_swap
---


# iter_swapsmall|(ranges::cartesian_product_view::''iterator'')

ddcl|since=c++23|
friend constexpr void iter_swap( const /*iterator*/& x, const /*iterator*/& y )
noexcept (/* see description */)
requires (std::indirectly_swappable<
ranges::iterator_t</*maybe-const*/<Const, First>>> and ... and
std::indirectly_swappable<ranges::iterator_t</*maybe-const*/<Const, Vs>>>);
Applies `ranges::iter_swap` to the stored underlying iterators. Formally, for every integer `1=0 ≤ i ≤ sizeof...(Vs)`, performs `ranges::iter_swap(std::get<i>(x.current_), std::get<i>(y.current_))`, where  is the underlying tuple of iterators.

## Parameters


### Parameters

- `x, y` - iterators to the elements to swap

## Return value

(none)

## Exceptions

The exception specification is equivalent to the logical AND of the expression `noexcept(ranges::iter_swap(std::get<i>(x.current_), std::get<i>(y.current_)))` for every integer `0 ≤ i ≤ sizeof...(Vs)`.

## See also


| cpp/iterator/ranges/dsc iter swap | (see dedicated page) |
| cpp/algorithm/dsc iter swap | (see dedicated page) |

