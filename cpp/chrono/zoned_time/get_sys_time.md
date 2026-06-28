---
title: std::chrono::zoned_time::operators
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/zoned_time/get_sys_time
---


```cpp
dcl|since=c++20|
operator std::chrono::sys_time<duration>() const;
dcl|since=c++20|
std::chrono::sys_time<duration> get_sys_time() const;
```

Obtains a `std::chrono::sys_time<duration>` representing the same point in time as this `zoned_time` object.

## Return value

A `std::chrono::sys_time<duration>` representing the same point in time as `*this`.
