---
title: std::chrono::gps_clock
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/gps_clock
---


```cpp
**Header:** `<`chrono`>`
dcl|since=c++20|1=
class gps_clock;
```

The clock `std::chrono::gps_clock` is a *Clock* that represents Global Positioning System (GPS) time. It measures time since 00:00:00, 6 January 1980 UTC.
Leap seconds are not inserted into GPS. Thus, every time a leap second is inserted into UTC, UTC  falls another second behind GPS. As of December 2017, UTC is 18 seconds behind GPS, reflecting the 18 leap seconds inserted between 1980 and 2017. Thus, 2018-01-01 00:00:00 UTC is equivalent to 2018-01-01 00:00:18 GPS. GPS is a constant 19 seconds behind TAI.
`gps_clock` meets the *Clock* requirements. It does not meet the *TrivialClock* requirements unless the implementation can guarantee that  does not throw an exception.

## Member functions


| 1=cpp/chrono/gps_clock/dsc now | (see dedicated page) |
| 1=cpp/chrono/gps_clock/dsc to_utc | (see dedicated page) |
| 1=cpp/chrono/gps_clock/dsc from_utc | (see dedicated page) |

