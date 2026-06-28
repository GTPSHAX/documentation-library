---
title: std::chrono::tzdb
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/tzdb
---


```cpp
**Header:** `<`chrono`>`
dcl|since=c++20|
struct tzdb;
```

The class `tzdb` represents a copy of the [https://www.iana.org/time-zones IANA time zone database]. Users cannot construct a `tzdb` and can only obtain read-only access to one via the free functions `std::chrono::get_tzdb_list` and `std::chrono::get_tzdb`.

## Member objects


| Item | Description |
|------|-------------|
| **Member object** | Description |


## Member functions


| cpp/chrono/tzdb/dsc locate_zone | (see dedicated page) |
| cpp/chrono/tzdb/dsc current_zone | (see dedicated page) |

