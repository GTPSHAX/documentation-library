---
title: std::chrono::month::month
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/month/month
---


```cpp
dcl|since=c++20|num=1|1=
month() = default;
dcl|since=c++20|num=2|1=
constexpr explicit month( unsigned m ) noexcept;
```

Constructs a `month` object.
1. Default constructor leaves the month value uninitialized.
2. If `m <, constructs a `month` object holding the month value `m`. Otherwise the value held is unspecified.
