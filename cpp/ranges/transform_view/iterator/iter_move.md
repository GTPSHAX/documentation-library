---
title: iter_move(ranges::transform_view::iterator)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/transform_view/iterator/iter_move
---


# iter_movesmall|(ranges::transform_view::''iterator'')

ddcl|since=c++20|
friend constexpr decltype(auto) iter_move( const /*iterator*/& i )
noexcept(/* see below */);
If `*i` is an lvalue reference, returns ; otherwise returns `*i`.

## Parameters


### Parameters

- `i` - `iterator`

## Return value

`std::move(*i)` if `*i` is an lvalue reference, otherwise `*i`

## Exceptions

where `*i.parent_->fun_` denotes the transformation function, `i.current_` denotes the underlying iterator.
