---
title: std::chrono::year_month_day::year_month_day
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/year_month_day/year_month_day
---


```cpp
dcl|since=c++20|num=1|1=
year_month_day() = default;
dcl|since=c++20|num=2|
constexpr year_month_day( const std::chrono::year& y,
const std::chrono::month& m,
const std::chrono::day& d ) noexcept;
dcl|since=c++20|num=3|
constexpr year_month_day( const std::chrono::year_month_day_last& ymdl ) noexcept;
dcl|since=c++20|num=4|
constexpr year_month_day( const std::chrono::sys_days& dp ) noexcept;
dcl|since=c++20|num=5|
constexpr explicit year_month_day( const std::chrono::local_days& dp ) noexcept;
```

Constructs a `year_month_day` object.
1. Default constructor leaves the date uninitialized.
2. Constructs a `year_month_day` object that stores the year `y`, month `m` and day `d`.
3. Constructs a `year_month_day` object that stores the year `ymdl.year()`, month `ymdl.month()` and day `ymdl.day()`.
4. Constructs a `year_month_day` object that represent the same date as the one represented by `dp`.
5. Constructs a `year_month_day` object that represent the same date as the one represented by `dp`, as if by `year_month_day(sys_days(dp.time_since_epoch()))`.
Constructors  define implicit conversions from `std::chrono::year_month_day_last` and `std::chrono::sys_days`, respectively.
For any `year_month_day` object `ymd` representing a valid date (`ymd.ok() ), converting `ymd` to `std::chrono::sys_days|sys_days` and back yields the same value.

## Notes

A `year_month_day` can also be created by combining one of the partial-date types `std::chrono::year_month` and `std::chrono::month_day` with the missing component (day and year, respectively) using `operator/`.

## Example


### Example


**Output:**
```
ymd2: 2020-01-31
ymd3: 2023-04-24
ymd4: 2023-08-30
```


## See also


| cpp/chrono/dsc operator/ | (see dedicated page) |

