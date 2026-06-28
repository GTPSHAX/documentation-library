---
title: std::chrono::tzdb_list
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/tzdb_list
---

ddcl|header=chrono|since=c++20|1=
class tzdb_list;
`tzdb_list` is a singleton list of `std::chrono::tzdb`s, each of which represents a copy of the [https://www.iana.org/time-zones IANA time zone database]. Users cannot construct a `tzdb_list` and can only obtain access to one via the `std::chrono::get_tzdb_list` free function.

## Member types


| Item | Description |
|------|-------------|
| **Type** | Description |


## Member functions


| 1=cpp/chrono/tzdb_list/dsc constructor | (see dedicated page) |
| 1=cpp/chrono/tzdb_list/dsc operator= | (see dedicated page) |
| 1=cpp/chrono/tzdb_list/dsc front | (see dedicated page) |
| 1=cpp/chrono/tzdb_list/dsc erase_after | (see dedicated page) |
| 1=cpp/chrono/tzdb_list/dsc begin | (see dedicated page) |
| 1=cpp/chrono/tzdb_list/dsc end | (see dedicated page) |

