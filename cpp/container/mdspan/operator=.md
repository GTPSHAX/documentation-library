---
title: std::mdspan::operator=
type: Containers
source: https://en.cppreference.com/w/cpp/container/mdspan/operator=
---


```cpp
**Header:** `<`mdspan`>`
dcl|num=1|since=c++23|1=
constexpr mdspan& operator=( const mdspan& rhs ) = default;
dcl|num=2|since=c++23|1=
constexpr mdspan& operator=( mdspan&& rhs ) = default;
```

Assigns `rhs` to `*this` with
1. defaulted copy assignment operator,
2. defaulted move assignment operator.

## Parameters


### Parameters

- `other` - another mdspan to copy or move from

## Return value

`*this`

## Example


## See also

