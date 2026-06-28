---
title: std::chrono::month_weekday::month_weekday
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/month_weekday/month_weekday
---


```cpp
dcl|since=c++20|1=
constexpr month_weekday( const std::chrono::month& m,
const std::chrono::weekday_indexed& wdi ) noexcept;
```

Constructs a `month_weekday` object that stores the `cpp/chrono/month` `m` and the `cpp/chrono/weekday_indexed` `wdi`.

## Notes

A more convenient way to construct a `month_weekday` is with `operator/`, e.g., `std::chrono::April/std::chrono::Sunday[2]`.

## See also


| cpp/chrono/dsc operator/ | (see dedicated page) |

