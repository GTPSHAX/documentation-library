---
title: std::chrono::year_month_day
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/year_month_day
---

ddcl|header=chrono|since=c++20|1=
class year_month_day;
The class `year_month_day` represents a specific year, month, and day. It is a field-based time point, with a resolution of `std::chrono::days`. `std::chrono::years`- and `std::chrono::months`-oriented arithmetic are supported directly. An implicit conversion to and from `std::chrono::sys_days` allows `std::chrono::days`-oriented arithmetic to be performed efficiently.
`year_month_day` is a *TriviallyCopyable* *StandardLayoutType*.

## Member functions


| cpp/chrono/year_month_day/dsc constructor | (see dedicated page) |
| cpp/chrono/year_month_day/dsc operator arith | (see dedicated page) |
| cpp/chrono/year_month_day/dsc accessors | (see dedicated page) |
| cpp/chrono/year_month_day/dsc operator days | (see dedicated page) |
| cpp/chrono/year_month_day/dsc ok | (see dedicated page) |


## Nonmember functions


| cpp/chrono/year_month_day/dsc operator cmp | (see dedicated page) |
| cpp/chrono/year_month_day/dsc operator arith 2 | (see dedicated page) |
| cpp/chrono/year_month_day/dsc operator ltlt | (see dedicated page) |
| cpp/chrono/year_month_day/dsc from_stream | (see dedicated page) |


## Helper classes


| cpp/chrono/dsc formatter|year_month_day | (see dedicated page) |
| cpp/chrono/year_month_day|nested=true|notes= | |


## Example


### Example


**Output:**
```
Current Year: 2023, Month: 9, Day: 4
ymd: 2023-09-04
```

