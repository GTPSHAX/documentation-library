---
title: std::chrono::tzdb_list::front
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/tzdb_list/front
---


```cpp
dcl|since=c++20|1=
const std::chrono::tzdb& front() const noexcept;
```

Obtains a reference to the first `std::chrono::tzdb` in the list. Simultaneous calls to this function and `std::chrono::reload_tzdb()` does not introduce a data race.

## Return value

A reference to the first `std::chrono::tzdb` in the list.
