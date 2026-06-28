---
title: std::chrono::get_leap_second_info
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/utc_clock/get_leap_second_info
---

ddcl|header=chrono|since=c++20|
template< class Duration >
std::chrono::leap_second_info
get_leap_second_info( const std::chrono::utc_time<Duration>& ut );
Obtains a `std::chrono::leap_second_info` whose `is_leap_second` and `elapsed` indicate whether `ut` is during a positive leap second insertion and the sum of leap seconds between 1 January 1970 and `ut`, respectively.

## Parameters


### Parameters

- `ut` - UTC time to examine

## Return value

A `leap_second_info` value specified above.

## See also


| cpp/chrono/utc_clock/dsc leap_second_info | (see dedicated page) |
| cpp/chrono/dsc leap_second | (see dedicated page) |

