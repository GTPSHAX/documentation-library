---
title: std::ranges::join_view::join_view
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/join_view/join_view
---


```cpp
dcl | num=1 | since=c++20 |1=
join_view() requires std::default_initializable<V> = default;
dcl | num=2 | since=c++20 |1=
constexpr explicit join_view( V base );
```

Constructs a `join_view`.
1. Default constructor. Value-initializes the underlying view. After construction, `base()` returns a copy of `V()`.
2. Initializes the underlying view with `std::move(base)`.

## Parameters


### Parameters


## Example

