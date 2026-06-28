---
title: std::chrono::year_month::year
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/year_month/accessors
---


```cpp
dcl|since=c++20|num=1|1=
constexpr std::chrono::year year() const noexcept;
dcl|since=c++20|num=2|1=
constexpr std::chrono::month month() const noexcept;
```

Retrieves the year and month values stored in this `year_month` object.

## Return value

1. Returns the stored `std::chrono::year` value.
2. Returns the stored `std::chrono::month` value.

## Example


### Example

```cpp
#include <chrono>
#include <iostream>

int main()
{
    std::cout << std::boolalpha;

    constexpr auto ym{std::chrono::year(2021)/std::chrono::July};  
    std::cout << (ym.year() == std::chrono::year(2021)) << ' ';
    std::cout << (ym.month() == std::chrono::month(7)) << '\n';
}
```


**Output:**
```
true true
```

