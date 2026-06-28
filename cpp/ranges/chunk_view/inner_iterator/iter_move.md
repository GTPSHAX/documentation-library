---
title: iter_move(ranges::chunk_view::inner-iterator)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/chunk_view/inner_iterator/iter_move
---


# iter_movesmall|(ranges::chunk_view::''inner-iterator'')

ddcl|since=c++23|
friend constexpr auto iter_move( const /*inner-iterator*/& i ) noexcept(/* see below */)
Returns the result of applying `ranges::iter_move` to the stored inner iterator.
Let  be the underlying pointer to the enclosing `chunk_view`, and `*i.parent_->current_` denote the cached underlying iterator of type `ranges::iterator_t<V>`.
Equivalent to: `return ranges::iter_move(*i.parent_->current_);`.

## Parameters


### Parameters

- `i` - iterator

## Return value

The result of applying `ranges::iter_move` to the stored iterator of type `ranges::iterator_t<V>`.

## Exceptions


## See also


| cpp/iterator/ranges/dsc iter_move | (see dedicated page) |

