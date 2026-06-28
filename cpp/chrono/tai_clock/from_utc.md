---
title: std::chrono::tai_clock::from_utc
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/tai_clock/from_utc
---


```cpp
dcl|since=c++20|1=
template< class Duration >
static std::chrono::tai_time<std::common_type_t<Duration, std::chrono::seconds>>
from_utc( const std::chrono::utc_time<Duration>& ) noexcept;
```

Converts the `utc_time` `t` to a `tai_time` representing the same point in time.

## Return value

A `std::chrono::tai_time` representing the same point in time as `t`, computed as if by constructing a value of the return type from `t.time_since_epoch()` and adding `378691210s` (378691210 is the number of seconds between the epochs of the two clocks: 1958-01-01 00:00:00 TAI and 1970-01-01 00:00:00 UTC).

## See also


| cpp/chrono/tai_clock/dsc to_utc | (see dedicated page) |
| cpp/chrono/dsc clock_cast | (see dedicated page) |

