---
title: std::chrono::tai_clock
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/tai_clock
---


```cpp
**Header:** `<`chrono`>`
dcl|since=c++20|1=
class tai_clock;
```

The clock `std::chrono::tai_clock` is a *Clock* that represents [International Atomic Time](https://en.wikipedia.org/wiki/International Atomic Time) (TAI). It measures time since 00:00:00, 1 January 1958, and is offset 10 seconds ahead of UTC at that date (i.e., its epoch, 1958-01-01 00:00:00 TAI, is 1957-12-31 23:59:50 UTC).
Leap seconds are not inserted into TAI. Thus, every time a leap second is inserted into UTC, UTC falls another second behind TAI. As of December 2017, UTC is 37 seconds behind TAI, reflecting the 10-second initial offset and the 27 leap seconds inserted between 1958 and 2017. Thus, 2018-01-01 00:00:00 UTC is equivalent to 2018-01-01 00:00:37 TAI.
`tai_clock` meets the *Clock* requirements. It does not meet the *TrivialClock* requirements unless the implementation can guarantee that  does not throw an exception.

## Member functions


| 1=cpp/chrono/tai_clock/dsc now | (see dedicated page) |
| 1=cpp/chrono/tai_clock/dsc to_utc | (see dedicated page) |
| 1=cpp/chrono/tai_clock/dsc from_utc | (see dedicated page) |

