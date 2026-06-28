---
title: std::chrono::month_day_last::month_day_last
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/month_day_last/month_day_last
---


```cpp
dcl|since=c++20|1=
constexpr explicit month_day_last( const std::chrono::month& m ) noexcept;
```

Constructs a `month_day_last` object that represents the last day of the month `m`.

## Notes

A more convenient way to construct a `month_day_last` is with `operator/`, e.g., `std::chrono::April/std::chrono::last`.

## See also


| cpp/chrono/dsc operator/ | (see dedicated page) |

