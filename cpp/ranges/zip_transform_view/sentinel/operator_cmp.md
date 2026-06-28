---
title: operator==(ranges::zip_transform_view::sentinel)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/zip_transform_view/sentinel/operator_cmp
---


# 1= operator==small|(ranges::zip_transform_view::''sentinel'')


```cpp
dcl|since=c++23|1=
template< bool OtherConst >
requires std::sentinel_for</*zentinel*/<Const>, /*ziperator*/<OtherConst>>
friend constexpr bool operator==( const /*iterator*/<OtherConst>& x,
const /*sentinel*/& y );
```

Compares the underlying iterator of `x` with the underlying sentinel of `y`.

## Parameters


### Parameters

- `x` - iterator to compare
- `y` - sentinel to compare

## Return value

`1= x.inner_ == y.inner_`, where  denotes the underlying iterator or sentinel respectively.

## Example

