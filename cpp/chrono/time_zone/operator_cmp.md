---
title: std::chrono::operators (std::chrono::time_zone)
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/time_zone/operator_cmp
---


```cpp
**Header:** `<`chrono`>`
dcl|since=c++20|num=1|1=
bool operator==( const std::chrono::time_zone& x,
const std::chrono::time_zone& y ) noexcept;
dcl|since=c++20|num=2|1=
std::strong_ordering operator<=>( const std::chrono::time_zone& x,
const std::chrono::time_zone& y ) noexcept;
```

Compares the two `time_zone` values `x` and `y` by name.

## Return value

1. `1=x.name() == y.name()`
2. `1=x.name() <=> y.name()`
