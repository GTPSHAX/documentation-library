---
title: operator==(ranges::adjacent_transform_view::sentinel)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/adjacent_transform_view/sentinel/operator_cmp
---


# 1= operator==small|(ranges::adjacent_transform_view::''sentinel'')


```cpp
dcl|since=c++23|1=
template< bool OtherConst >
requires std::sentinel_for</*inner-sentinel*/<Const>,
/*inner-iterator*/<OtherConst>>
friend constexpr bool operator==( const /*iterator*/<OtherConst>& x,
const /*sentinel*/& y );
```

Compares the underlying iterator of `x` with the underlying sentinel of `y`.
Equivalent to:
box|
`return x.`
`1=== y.`
`;`
.

## Parameters


### Parameters

- `x` - an  to compare
- `y` - a `sentinel` to compare

## Return value

The result of comparison.

## Example

