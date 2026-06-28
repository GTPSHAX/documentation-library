---
title: std::chrono::time_zone_link::target
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/time_zone_link/accessors
---


```cpp
dcl|num=1|
std::string_view name() const noexcept;
dcl|num=2|
std::string_view target() const noexcept;
```

Accesses the name and target of this `time_zone_link` object.

## Return value

1. The alternative name this `time_zone_link` object represents.
2. The name of the `std::chrono::time_zone` for which this `time_zone_link` object provides an alternative name.
