---
title: std::chrono::weekday_indexed::index
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/weekday_indexed/index
---


```cpp
dcl|since=c++20|
constexpr unsigned index() const noexcept;
```

Accesses the index stored in `*this`.

## Return value

The index stored in `*this`.

## Example


### Example

```cpp
#include <chrono>
#include <iostream>

int main()
{
    std::cout << std::boolalpha;

    std::chrono::weekday_indexed wdi {std::chrono::Tuesday[2]}; // 2nd Tuesday of a month
    std::cout << (std::chrono::year_month_day{wdi/10/2019} == 
                  std::chrono::year_month_day{std::chrono::October/8/2019}) << ' ';

    wdi = {wdi.weekday()[wdi.index() + 2]}; // 2nd Tuesday => 4th Tuesday
    std::cout << (std::chrono::year_month_day{wdi/10/2019} == 
                  std::chrono::year_month_day{std::chrono::October/22/2019}) << '\n';
}
```


**Output:**
```
true true
```

