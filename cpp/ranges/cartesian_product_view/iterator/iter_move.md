---
title: iter_move(ranges::cartesian_product_view::iterator)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/cartesian_product_view/iterator/iter_move
---


# iter_movesmall|(ranges::cartesian_product_view::''iterator'')

ddcl|since=c++23|
friend constexpr auto iter_move( const /*iterator*/& i ) noexcept(/* see below */)
Let  be the underlying tuple of iterators.
Equivalent to: `return /*tuple-transform*/(ranges::iter_move, i.current_);`

## Parameters


### Parameters

- `i` - iterator

## Return value

A tuple that contains the result of applying `ranges::iter_move` to the stored underlying iterators converted to the return type, as described above.

## Exceptions

The exception specification is equivalent to the logical AND of the following expressions:
* `noexcept(ranges::iter_move(std::get<N>(i.current_)))` for every integer `1=0 ≤ N ≤ sizeof...(Vs)`,
* `std::is_nothrow_move_constructible_v<ranges::range_rvalue_reference_t</*maybe-const*/<Const, T>>>` for every type `T` in `First, Vs...`.

## See also


| cpp/iterator/ranges/dsc iter_move | (see dedicated page) |

