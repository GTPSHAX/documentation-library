---
title: std::chrono::file_clock
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/file_clock
---


```cpp
**Header:** `<`chrono`>`
dcl|since=c++20|1=
using file_clock = /* see below */;
```

`std::chrono::file_clock` is an alias for the clock used for `std::filesystem::file_time_type`. Its epoch is unspecified.
`file_clock` meets the *TrivialClock* requirements.

## Member functions

`file_clock` provides exactly one of the following two pairs of static member functions:
* `to_utc` and `from_utc`; or
* `to_sys` and `from_sys`.


| 1=cpp/chrono/file_clock/dsc now | (see dedicated page) |
| 1=cpp/chrono/file_clock/dsc to_from_utc | (see dedicated page) |
| 1=cpp/chrono/file_clock/dsc to_from_sys | (see dedicated page) |

