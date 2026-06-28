---
title: operators (ranges::adjacent_view::sentinel)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/adjacent_view/sentinel/operator_cmp
---


# 1= operator==small|(ranges::adjacent_view::''iterator'', ranges::adjacent_view::''sentinel'')


```cpp
dcl|since=c++23|1=
template< bool OtherConst >
requires std::sentinel_for<ranges::sentinel_t<Base>,
ranges::iterator_t</*maybe-const*/<OtherConst, V>>>
friend constexpr bool operator==( const /*iterator*/<OtherConst>& x,
const /*sentinel*/& y );
```

Compares the underlying iterator of `x` with the underlying sentinel of `y`.
Equivalent to: `1=return x.current_.back() == y.end_`, where  is underlying array of iterators in `x`, and  is the underlying sentinel in `y`.

## Parameters


### Parameters

- `x` - iterator to compare
- `y` - `sentinel` to compare

## Return value

`true` if the underlying iterator stored in `x` is the end iterator.

## Example

