---
title: std::chrono::steady_clock
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/steady_clock
---


```cpp
**Header:** `<`chrono`>`
dcl|since=c++11|1=
class steady_clock;
```

Class `std::chrono::steady_clock` represents a monotonic clock. The time points of this clock cannot decrease as physical time moves forward and the time between ticks of this clock is constant. This clock is not related to wall clock time (for example, it can be time since last reboot), and is most suitable for measuring intervals.
`std::chrono::steady_clock` meets the requirements of *TrivialClock*.

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Member constants


## Member functions


## See also


| cpp/chrono/system_clock|wall clock time from the system-wide realtime clock|notes= | |
| cpp/chrono/high_resolution_clock|the clock with the shortest tick period available|notes= | |

