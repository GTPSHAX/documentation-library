---
title: operator-(ranges::zip_transform_view::sentinel)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/zip_transform_view/sentinel/operator-
---


# operator-small|(ranges::zip_transform_view::''sentinel'')


```cpp
dcl|num=1|since=c++23|
template< bool OtherConst >
requires std::sized_sentinel_for</*zentinel*/<Const>, /*ziperator*/<OtherConst>>
friend constexpr ranges::range_difference_t</*maybe-const*/<OtherConst, /*InnerView*/>>
operator-( const /*iterator*/<OtherConst>& x, const /*sentinel*/& y );
dcl|num=2|since=c++23|
template< bool OtherConst >
requires std::sized_sentinel_for</*zentinel*/<Const>, /*ziperator*/<OtherConst>>
friend constexpr ranges::range_difference_t</*maybe-const*/<OtherConst, /*InnerView*/>>
operator-( const /*sentinel*/& y, const /*iterator*/<OtherConst>& x );
```

Computes the distance between the underlying iterator of `x` and the underlying sentinel of `y`.

## Parameters


### Parameters

- `x` - an iterator
- `y` - a sentinel

## Return value

Let  denote the underlying iterator or sentinel respectively.
1. `x.inner_ - y.inner_`
2. `y.inner_ - x.inner_`
