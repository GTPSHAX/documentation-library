---
title: iter_move(ranges::zip_view::iterator)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/zip_view/iterator/iter_move
---


# iter_movesmall|(ranges::zip_view::''iterator'')

ddcl|since=c++23|
friend constexpr auto iter_move( const iterator& i ) noexcept(/* see below */);
Equivalent to: `return /*tuple-transform*/(ranges::iter_move, i.current_);`, where  denotes the underlying tuple-like object that holds iterators to elements of adapted views.

## Parameters


### Parameters

- `i` - iterator

## Return value

`std::move(*i)` if `*i` is an lvalue reference, otherwise `*i`

## Exceptions

noexcept|
(
noexcept
(
ranges::iter_move
(
declval<const ranges::iterator_t</*maybe-const*/<Const, Views>>&>()
)
)
and ...
)
and
(
std::is_nothrow_move_constructible_v
<
ranges::range_rvalue_reference_t</*maybe-const*/<Const, Views>>
>
and ...
)
