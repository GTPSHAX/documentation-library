---
title: std::chrono::month_day::ok
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/month_day/ok
---


```cpp
dcl|since=c++20|1=
constexpr bool ok() const noexcept;
```

Determines whether this `month_day` stores a valid month-day combination.
The combination is valid if `month()` represents a valid month (`month().ok() ), }, and }, where D is the number of days in the month represented by `month()`. The number of days in February is considered to be 29.

## Return value

`true` if the month and day combination is valid, otherwise false.

## Example


### Example

```cpp
#include <chrono>
#include <iostream>

int main()
{
    std::cout << std::boolalpha;

    constexpr auto md1{std::chrono::July/15};
    std::cout << (md1.ok()) << ' ';
    constexpr std::chrono::month_day md2{std::chrono::month(14), std::chrono::day(42)};
    std::cout << (md2.ok()) << ' ';
    constexpr auto md3{std::chrono::February/29};
    std::cout << (md3.ok()) << '\n';
}
```


**Output:**
```
true false true
```

