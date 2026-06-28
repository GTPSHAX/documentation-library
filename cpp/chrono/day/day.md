---
title: std::chrono::day::day
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/day/day
---


```cpp
dcl|since=c++20|num=1|1=
day() = default;
dcl|since=c++20|num=2|1=
constexpr explicit day( unsigned d ) noexcept;
```

Constructs a `day` object.
1. Default constructor leaves the day value uninitialized.
2. If `d <, constructs a `day` object holding the day value `d`. Otherwise the value held is unspecified.
