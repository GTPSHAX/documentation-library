---
title: iter_swap(ranges::stride_view::iterator)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/stride_view/iterator/iter_swap
---


# iter_swapsmall|(ranges::stride_view::''iterator'')

ddcl|since=c++23|
friend constexpr void iter_swap( const /*iterator*/& x, const /*iterator*/& y )
noexcept( /*see below*/ )
requires std::indirectly_swappable<ranges::iterator_t<Base>>;
Swaps the objects pointed to by two underlying iterators (each denoted as ).
Equivalent to `ranges::iter_swap(x.current_, y.current_);`.

## Parameters


### Parameters

- `x, y` - `iterator`s

## Return value

(none)

## Exceptions


## Example

