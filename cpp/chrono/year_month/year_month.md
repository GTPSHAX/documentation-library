---
title: std::chrono::year_month::year_month
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/year_month/year_month
---


```cpp
dcl|since=c++20|num=1|1=
year_month() = default;
dcl|since=c++20|num=2|1=
constexpr year_month( const std::chrono::year& y,
const std::chrono::month& m ) noexcept;
```

Constructs a `year_month` object.
1. Default constructor leaves the year and month uninitialized.
2. Constructs a `year_month` object storing the year `y` and the month `m`.

## Notes

A more convenient way to construct a `year_month` is with `operator/`, e.g., `2007y/std::chrono::April`.

## See also


| cpp/chrono/dsc operator/ | (see dedicated page) |

