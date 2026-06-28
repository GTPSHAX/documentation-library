---
title: operator-(ranges::adjacent_view::sentinel)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/adjacent_view/sentinel/operator-
---


# operator-small|(ranges::adjacent_view::''sentinel'')


```cpp
dcl|num=1|since=c++23|
template< bool OtherConst >
requires std::sized_sentinel_for<ranges::sentinel_t<Base>,
ranges::iterator_t</*maybe-const*/<OtherConst, V>>>
friend constexpr ranges::range_difference_t</*maybe-const*/<OtherConst, V>>
operator-( const /*iterator*/<OtherConst>& x, const /*sentinel*/& y );
dcl|num=2|since=c++23|
template< bool OtherConst >
requires std::sized_sentinel_for<ranges::sentinel_t<Base>,
ranges::iterator_t</*maybe-const*/<OtherConst, V>>>
friend constexpr ranges::range_difference_t</*maybe-const*/<OtherConst, V>>
operator-( const /*sentinel*/& y, const /*iterator*/<OtherConst>& x );
```

Computes the distance between the underlying iterator of `x` and the underlying sentinel of `y`.
Let  denote the underlying array of iterators in `x`, and  denote the underlying sentinel in `y`.
1. Equivalent to: `return x.current_.back() - y.end_;`
2. Equivalent to: `return y.end_ - x.current_.back();`

## Parameters


### Parameters

- `x` - an iterator
- `y` - a `sentinel`

## Return value

The distance between `x` and `y`.

## Example

