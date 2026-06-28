---
title: std::chrono::month_weekday_last::month_weekday_last
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/month_weekday_last/month_weekday_last
---

ddcl|since=c++20|1=
constexpr month_weekday_last( const std::chrono::month& m,
const std::chrono::weekday_last& wdl ) noexcept;
Constructs a `month_weekday_last` object that stores the `cpp/chrono/month` `m` and the `cpp/chrono/weekday_last` `wdl`.

## Notes

A more convenient way to construct a `month_weekday_last` is with `operator/`, e.g., `std::chrono::April/std::chrono::Sunday[std::chrono::last]`.

## See also


| cpp/chrono/dsc operator/ | (see dedicated page) |

