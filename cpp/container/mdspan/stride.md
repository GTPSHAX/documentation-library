---
title: std::mdspan::stride
type: Containers
source: https://en.cppreference.com/w/cpp/container/mdspan/stride
---


```cpp
dcl|since=c++23|
constexpr index_type stride( rank_type r ) const;
```

Returns the stride of the layout mapping  in `r` dimension. Equivalent to `return map_.stride(r);`.

## Parameters


### Parameters

- `r` - the index of the dimension

## Return value

The stride.

## Example

