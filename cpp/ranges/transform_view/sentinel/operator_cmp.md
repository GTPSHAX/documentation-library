---
title: operator==(ranges::transform_view::sentinel)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/transform_view/sentinel/operator_cmp
---


# 1= operator==small|(ranges::transform_view::''sentinel'')


```cpp
dcl|since=c++20|1=
friend constexpr bool operator==( const /*iterator*/<Const>& x, const /*sentinel*/& y );
```

Compares the underlying iterator of `x` with the underlying sentinel of `y`.

## Parameters


### Parameters

- `x` - iterator to compare
- `y` - sentinel to compare

## Return value

`1= x.current_ == y.end_`, where  denotes the underlying iterator,  denotes the underlying sentinel.

## Example

