---
title: std::chrono::utc_clock
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/utc_clock
---

ddcl|header=chrono|since=c++20|
class utc_clock;
The clock `std::chrono::utc_clock` is a *Clock* that represents [Coordinated Universal Time](https://en.wikipedia.org/wiki/Coordinated Universal Time) (UTC). It measures time since 00:00:00 UTC, Thursday, 1 January 1970, including leap seconds.
`utc_clock` meets the *Clock* requirements. It does not meet the *TrivialClock* requirements unless the implementation can guarantee that  does not throw an exception.

## Member functions


| 1=cpp/chrono/utc_clock/dsc now | (see dedicated page) |
| 1=cpp/chrono/utc_clock/dsc to_sys | (see dedicated page) |
| 1=cpp/chrono/utc_clock/dsc from_sys | (see dedicated page) |


## Non-member functions


| cpp/chrono/utc_clock/dsc get_leap_second_info | (see dedicated page) |


## Helper classes


| cpp/chrono/utc_clock/dsc leap_second_info | (see dedicated page) |


## Notes

The official UTC epoch is 1 January 1972. `utc_clock` uses 1 January 1970 instead to be consistent with `std::chrono::system_clock`.
