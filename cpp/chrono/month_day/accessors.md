---
title: std::chrono::month_day::month
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/month_day/accessors
---


```cpp
dcl|since=c++20|num=1|1=
constexpr std::chrono::month month() const noexcept;
dcl|since=c++20|num=1|1=
constexpr std::chrono::day day() const noexcept;
```

Retrieves the month and day values stored in this `month_day` object.

## Return value

1. Returns the stored `std::chrono::month` value.
2. Returns the stored `std::chrono::day` value.

## Example


### Example

```cpp
#include <chrono>

int main()
{
    constexpr auto md{std::chrono::July/15};  
    static_assert(md.month() == std::chrono::month(7));
    static_assert(md.day() == std::chrono::day(15));
}
```

