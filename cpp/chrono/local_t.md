---
title: std::chrono::local_t
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/local_t
---

ddcl|header=chrono|since=c++20|1=
struct local_t {};
The class `local_t` is a pseudo-clock that is used as the first template argument to `std::chrono::time_point` to indicate that the time point represents local time with respect of a not-yet-specified time zone. `local_time` supports streaming and the full set of time point arithmetic.

## See also


| cpp/chrono/dsc zoned_time | (see dedicated page) |

