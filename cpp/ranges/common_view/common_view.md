---
title: std::ranges::common_view::common_view
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/common_view/common_view
---


```cpp
dcl | num=1 | since=c++20 |1=
common_view() = default;
dcl | num=2 | since=c++20 |
constexpr explicit common_view( V r );
```

Constructs a `common_view`.
1. Default constructor. Value-initializes the underlying view. After construction, `base()` returns a copy of `V()`.
2. Initializes the underlying view with `std::move(r)`.

## Parameters


### Parameters


## Example


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-3405 | C++20 | the redundant converting constructor might cause constraint recursion | removed |

