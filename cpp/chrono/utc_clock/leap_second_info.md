---
title: std::chrono::leap_second_info
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/utc_clock/leap_second_info
---

ddcl|header=chrono|since=c++20|
struct leap_second_info {
bool is_leap_second;
std::chrono::seconds elapsed;
};
A `leap_second_info` indicates whether a UTC time is during a positive leap second insertion and the total number of leap seconds between 1 January 1970 and the UTC time.
`leap_second_info` has no base classes or members other than `is_leap_second`, `elapsed`, and implicitly declared special member functions.

## Member objects


## Notes

`leap_second_info` is typically obtained from `std::chrono::get_leap_second_info`.

## See also


| cpp/chrono/dsc leap_second | (see dedicated page) |

