---
title: Vs...>::iterator::operator[]
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/cartesian_product_view/iterator/operator_at
---

ddcl|since=c++23|
constexpr reference operator[]( difference_type n ) const
requires /*cartesian-product-is-random-access*/<Const, First, Vs...>;
Returns an element at specified relative location. Equivalent to: `return *((*this) + n);`.

## Parameters


### Parameters

- `n` - position relative to current location

## Return value

The element at displacement `n` relative to the current location.

## Example


## See also

