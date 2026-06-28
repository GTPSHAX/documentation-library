---
title: std::chrono::year_month_weekday_last::year_month_weekday_last
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/year_month_weekday_last/year_month_weekday_last
---


```cpp
dcl|since=c++20|
constexpr
year_month_weekday_last( const std::chrono::year& y, const std::chrono::month& m,
const std::chrono::weekday_last& wdl ) noexcept;
```

Constructs a `year_month_weekday_last` object storing the year `y`, the month `m`, and the weekday `wdl.weekday()`. The constructed object represents the last weekday of that year and month.

## Notes

A `year_month_weekday_last` can also be created by combining one of the partial-date types `std::chrono::year_month` and `std::chrono::month_weekday_last` with the missing component (`std::chrono::weekday_last|weekday_last` and `std::chrono::year|year`, respectively) using `operator/`.

## See also


| cpp/chrono/dsc operator/ | (see dedicated page) |

