---
title: operator==(ranges::chunk_by_view::iterator)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/chunk_by_view/iterator/operator_cmp
---


# 1=operator==small|(ranges::chunk_by_view::''iterator'')


```cpp
dcl|num=1|since=c++23|1=
friend constexpr bool operator==( const /*iterator*/& x, const /*iterator*/& y );
dcl|num=2|since=c++23|1=
friend constexpr bool operator==( const /*iterator*/& x, std::default_sentinel_t );
```

Compares the underlying iterators.
1. Equivalent to .
2. Equivalent to .

## Parameters


### Parameters

- `x, y` - `iterator`s to compare

## Return value

The result of comparison.

## Example

