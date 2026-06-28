---
title: iter_swap(ranges::zip_view::iterator)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/zip_view/iterator/iter_swap
---


# iter_swapsmall|(ranges::zip_view::''iterator'')

ddcl|since=c++23|
friend constexpr void iter_swap( const /*iterator*/& x, const /*iterator*/& y )
noexcept(/* see below */)
requires (std::indirectly_swappable<ranges::iterator_t<
/*maybe-const*/<Const, Views>>> && ...);
Performs `ranges::iter_swap(std::get<i>(x.current_), std::get<i>(y.current_))` for every integer `i` in [0, sizeof...(Views)), where  denotes the underlying tuple-like object that holds iterators to elements of adapted views.

## Parameters


### Parameters

- `x, y` - iterators to the elements to swap

## Return value

(none)

## Exceptions

noexcept|
(noexcept(ranges::iter_swap(
declval<const ranges::iterator_t</*maybe-const*/<Const, Views>>&>(),
declval<const ranges::iterator_t</*maybe-const*/<Const, Views>>&>())) &&...)
