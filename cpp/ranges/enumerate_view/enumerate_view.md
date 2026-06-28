---
title: std::ranges::enumerate_view::enumerate_view
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/enumerate_view/enumerate_view
---


```cpp
dcl|num=1|since=c++23|1=
enumerate_view() requires std::default_initializable<V> = default;
dcl|num=2|since=c++23|1=
constexpr explicit enumerate_view( V base );
```

Constructs a `enumerate_view`.
1. Default constructor. Value-initializes the underlying view `''base_''`. After construction, `base()` returns a copy of `V()`.
2. Initializes the underlying view `''base_''` with `std::move(base)`.

## Parameters


### Parameters

- `base` - the underlying view

## Example

