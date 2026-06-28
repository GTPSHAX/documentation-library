---
title: std::ranges::enumerate_view::iterator<Const>::operator[]
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/enumerate_view/iterator/operator_at
---

ddcl|since=c++23|
constexpr auto operator[]( difference_type n ) const
requires ranges::random_access_range<Base>
Returns an element at specified relative location.
Equivalent to:
.

## Parameters


### Parameters

- `n` - position relative to current location

## Return value

The element at displacement `n` relative to the current location.

## Example


## See also

