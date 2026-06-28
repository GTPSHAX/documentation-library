---
title: operator-(ranges::transform_view::sentinel)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/transform_view/sentinel/operator-
---


# operator-small|(ranges::transform_view::''sentinel'')


```cpp
dcl|num=1|since=c++20|
friend constexpr ranges::range_difference_t<Base>
operator-( const /*iterator*/<Const>& x, const /*sentinel*/& y )
requires std::sized_sentinel_for<ranges::sentinel_t<Base>,
ranges::iterator_t<Base>>;
dcl|num=2|since=c++20|
friend constexpr ranges::range_difference_t<Base>
operator-( const /*sentinel*/& y, const /*iterator*/<Const>& x )
requires std::sized_sentinel_for<ranges::sentinel_t<Base>,
ranges::iterator_t<Base>>;
```

Computes the distance between the underlying iterator of `x` and the underlying sentinel of `y`.

## Parameters


### Parameters

- `x` - an 
- `y` - a sentinel

## Return value

Let  denote the underlying iterator,  denote the underlying sentinel.
1. `1= x.current_ - y.end_`
2. `1= y.end_ - x.current_`
