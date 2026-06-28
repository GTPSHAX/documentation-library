---
title: operator==(ranges::elements_view::sentinel)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/elements_view/sentinel/operator_cmp
---


# 1=operator==small|(ranges::elements_view::''sentinel'')

ddcl|since=c++20|1=
template< bool OtherConst >
requires std::sentinel_for<ranges::sentinel_t<Base>,
ranges::iterator_t</*maybe-const*/<OtherConst, V>>>
friend constexpr bool operator==( const /*iterator*/<OtherConst>& x,
const /*sentinel*/& y );
Compares the underlying iterator of `x` with the underlying sentinel of `y`.

## Parameters


### Parameters

- `x` - iterator to compare
- `y` - sentinel to compare

## Return value

`1=x.base() == y.base()`.

## Example

