---
title: std::chrono::time_zone::get_info
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/time_zone/get_info
---


```cpp
dcl|since=c++20|
template< class Duration >
std::chrono::sys_info get_info( const std::chrono::sys_time<Duration>& tp ) const;
dcl|since=c++20|
template< class Duration >
std::chrono::local_info get_info( const std::chrono::local_time<Duration>& tp ) const;
```

Obtains information about this time zone at the time point `tp`.

## Return value

1. A `std::chrono::sys_info` structure `i` containing the time zone information in effect for this time zone at the time point `tp`. `tp` will be in the range [i.begin, i.end).
2. A `std::chrono::local_info` structure containing information about the local time `tp` in this time zone.
