---
title: std::chrono::zoned_time::get_time_zone
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/zoned_time/get_time_zone
---


```cpp
dcl|since=c++20|
TimeZonePtr get_time_zone() const;
```

Retrieves the stored time zone pointer.

## Return value

A copy of the stored time zone pointer.

## Notes

There's no way to access the time zone pointer when `TimeZonePtr` is a move-only type.
