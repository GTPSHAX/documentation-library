---
title: operators (ranges::join_with_view::sentinel)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/join_with_view/sentinel/operator_cmp
---


# 1= operator==small|(ranges::join_with_view::''iterator'', ranges::join_with_view::''sentinel'')


```cpp
dcl|since=c++23|1=
friend constexpr bool operator==( const /*iterator*/<Const>& x, const /*sentinel*/& y );
```

Compares the underlying iterator of `x` with the underlying sentinel of `y`. The comparison returns true if the underlying outer iterator stored in `x` is the end iterator.

## Parameters


### Parameters

- `x` - iterator to compare
- `y` - sentinel to compare

## Return value

`1= x.outer_it_ == y.end_`, where  denotes the underlying outer iterator,  denotes the underlying sentinel.

## Example

