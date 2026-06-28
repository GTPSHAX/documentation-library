---
title: iter_move(ranges::stride_view::iterator)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/stride_view/iterator/iter_move
---


# iter_movesmall|(ranges::stride_view::''iterator'')

ddcl|since=c++23|
friend constexpr ranges::range_rvalue_reference_t<Base>
iter_move( const /*iterator*/& i ) noexcept(/* see below */);
Returns the result of applying `ranges::iter_move` to the underlying iterator .
Equivalent to `return ranges::iter_move(i.current_);`.

## Parameters


### Parameters

- `i` - `iterator`

## Return value

The result of applying `ranges::iter_move` to the stored iterator.

## Exceptions


## Example

