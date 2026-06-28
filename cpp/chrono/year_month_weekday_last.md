---
title: std::chrono::year_month_weekday_last
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/year_month_weekday_last
---

ddcl|header=chrono|since=c++20|
class year_month_weekday_last;
The class `year_month_weekday_last` represents the last weekday of a specific year and month. It is a field-based time point, with a resolution of `std::chrono::days`, except that it is limited to pointing to the last weekday of a year and month. `std::chrono::years`- and `std::chrono::months`-oriented arithmetic are supported directly. An implicit conversion to `std::chrono::sys_days` allows `std::chrono::days`-oriented arithmetic to be performed efficiently.
`year_month_weekday_last` is a *TriviallyCopyable* *StandardLayoutType*.

## Member functions


| cpp/chrono/year_month_weekday_last/dsc constructor | (see dedicated page) |
| cpp/chrono/year_month_weekday_last/dsc operator arith | (see dedicated page) |
| cpp/chrono/year_month_weekday_last/dsc accessors | (see dedicated page) |
| cpp/chrono/year_month_weekday_last/dsc operator days | (see dedicated page) |
| cpp/chrono/year_month_weekday_last/dsc ok | (see dedicated page) |


## Nonmember functions


| cpp/chrono/year_month_weekday_last/dsc operator cmp | (see dedicated page) |
| cpp/chrono/year_month_weekday_last/dsc operator arith 2 | (see dedicated page) |
| cpp/chrono/year_month_weekday_last/dsc operator ltlt | (see dedicated page) |


## Helper classes


| cpp/chrono/dsc formatter|year_month_weekday_last | (see dedicated page) |
| cpp/chrono/year_month_weekday_last|nested=true|notes= | |

