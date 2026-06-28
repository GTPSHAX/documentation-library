---
title: operator-(ranges::elements_view::sentinel)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/elements_view/sentinel/operator-
---


# operator-small|(ranges::elements_view::''sentinel'')


```cpp
dcl|num=1|since=c++20|
template< bool OtherConst >
requires std::sized_sentinel_for<ranges::sentinel_t<Base>,
ranges::iterator_t</*maybe-const*/<OtherConst, V>>>
friend constexpr ranges::range_difference_t</*maybe-const*/<OtherConst, V>>
operator-( const /*iterator*/<OtherConst>& x, const /*sentinel*/& y );
dcl|num=2|since=c++20|
template< bool OtherConst >
requires std::sized_sentinel_for<ranges::sentinel_t<Base>,
ranges::iterator_t</*maybe-const*/<OtherConst, V>>>
friend constexpr ranges::range_difference_t</*maybe-const*/<OtherConst, V>>
operator-( const /*sentinel*/& y, const /*iterator*/<OtherConst>& x );
```

Computes the distance between the underlying iterator of `x` and the underlying sentinel of `y`.

## Parameters


### Parameters

- `x` - an iterator
- `y` - a sentinel

## Return value

1. `x.base() - y.base()`
2. `y.base() - x.base()`
