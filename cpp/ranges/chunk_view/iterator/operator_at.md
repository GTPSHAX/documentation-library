---
title: std::ranges::chunk_view::iterator<Const>::operator[]
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/chunk_view/iterator/operator_at
---

ddcl|since=c++23|
constexpr value_type operator[]( difference_type pos ) const
requires ranges::random_access_range<Base>;
Returns an element at specified relative location.
Equivalent to: `return *(*this + pos);`.

## Parameters


### Parameters

- `pos` - position relative to current location

## Return value

The element (of type ) at displacement `pos` relative to the current location.

## Example


## See also

