---
title: operator-(ranges::slide_view::sentinel)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/slide_view/sentinel/operator-
---


# operator-small|(ranges::slide_view::''sentinel'')


```cpp
dcl|num=1|since=c++23|
friend constexpr ranges::range_difference_t<V>
operator-( const /*iterator*/<false>& x, const /*sentinel*/& y )
requires std::sized_sentinel_for<ranges::sentinel_t<V>,
ranges::iterator_t<V>>;
dcl|num=2|since=c++23|
friend constexpr ranges::range_difference_t<V>
operator-( const /*sentinel*/& y, const /*iterator*/<false>& x )
requires std::sized_sentinel_for<ranges::sentinel_t<V>,
ranges::iterator_t<V>>;
```

Computes the distance between the underlying  of `x` and the underlying `sentinel` of `y`.
Let  denote the underlying iterator of `x` and  denote the underlying sentinel of `y`.
1. Equivalent to: `return x.last_ele_ - y.end_;`.
2. Equivalent to: `return y.end_ - x.last_ele_;`.

## Parameters


### Parameters

- `x` - an 
- `y` - a `sentinel`

## Return value

The distance between the iterator and the sentinel.

## Example

