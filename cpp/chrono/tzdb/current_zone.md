---
title: std::chrono::tzdb::current_zone
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/tzdb/current_zone
---


```cpp
dcl|since=c++20|1=
const std::chrono::time_zone* current_zone() const;
```

Obtains a pointer to a `std::chrono::time_zone` in this database that represents the local time zone of the computer.

## Return value

A pointer to the `std::chrono::time_zone` in this database that represents the local time zone of the computer.
