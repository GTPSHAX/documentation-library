---
title: iter_swap(ranges::chunk_view::inner-iterator)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/chunk_view/inner_iterator/iter_swap
---


# iter_swapsmall|(ranges::chunk_view::''inner-iterator'')

ddcl|since=c++23|
friend constexpr void iter_swap( const /*inner-iterator*/& x,
const /*inner-iterator*/& y )
noexcept(noexcept(ranges::iter_swap(*x.parent_->current_,
*y.parent_->current_)))
requires std::indirectly_swappable<ranges::iterator_t<V>>;
Applies `ranges::iter_swap` to the underlying cached iterators.
Let  be the underlying pointer to the enclosing `chunk_view`, and `*i.parent_->current_` denote the underlying cached iterator of type `ranges::iterator_t<V>`.
Equivalent to: `ranges::iter_swap(*x.parent_->current_, *y.parent_->current_);`.

## Parameters


### Parameters

- `x, y` - iterators to the elements to swap

## Return value

(none)

## See also


| cpp/iterator/ranges/dsc iter swap | (see dedicated page) |
| cpp/algorithm/dsc iter swap | (see dedicated page) |

