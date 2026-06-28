---
title: std::chrono::month_day::month_day
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/month_day/month_day
---


```cpp
dcl|since=c++20|num=1|1=
month_day() = default;
dcl|since=c++20|num=2|1=
constexpr month_day( const std::chrono::month& m,
const std::chrono::day& d ) noexcept;
```

Constructs a `month_day`.
1. Default constructor leaves the stored month and day values uninitialized.
2. Constructs a `month_day` that stores the month `m` and the day `d`.

## Notes

A more convenient way to construct a `month_day` is with `operator/`, e.g., `std::chrono::April/1`.

## Example


### Example


**Output:**
```
29/2
```


## See also


| cpp/chrono/dsc operator/ | (see dedicated page) |

