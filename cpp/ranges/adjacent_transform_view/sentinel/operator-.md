---
title: operator-(ranges::adjacent_transform_view::sentinel)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/adjacent_transform_view/sentinel/operator-
---


# operator-small|(ranges::adjacent_transform_view::''sentinel'')


```cpp
dcl|num=1|since=c++23|
template< bool OtherConst >
requires std::sized_sentinel_for</*inner-sentinel*/<Const>,
/*inner-iterator*/<OtherConst>>
friend constexpr
ranges::range_difference_t</*maybe-const*/<OtherConst, InnerView>>
operator-( const /*iterator*/<OtherConst>& x, const /*sentinel*/& y );
dcl|num=2|since=c++23|
template< bool OtherConst >
requires std::sized_sentinel_for</*inner-sentinel*/<Const>,
/*inner-iterator*/<OtherConst>>
friend constexpr
ranges::range_difference_t</*maybe-const*/<OtherConst, InnerView>>
operator-( const /*sentinel*/& y, const /*iterator*/<OtherConst>& x );
```

Computes the distance between the  `x` and the `sentinel` `y`.
1. Equivalent to:
.
2. Equivalent to:
.

## Parameters


### Parameters

- `x` - the iterator
- `y` - the sentinel

## Return value

The distance between iterator and sentinel.

## Example

