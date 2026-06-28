---
title: std::chrono::weekday_last::weekday
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/weekday_last/weekday
---


```cpp
dcl|since=c++20|1=
constexpr std::chrono::weekday weekday() const noexcept;
```

Retrieves a copy of the `std::chrono::weekday` object stored in `*this`.

## Return value

A copy of the `std::chrono::weekday` object stored in `*this`.

## Example


### Example

```cpp
#include <chrono>
#include <iostream>
using namespace std::chrono;

int main()
{
    std::cout << std::boolalpha;

    auto wdl{Tuesday[last]}; // Last Tuesday of a month
    std::cout << (year_month_day{wdl/10/2019} ==
                  year_month_day{October/29/2019}) << ' ';

    wdl = {(wdl.weekday() + days(2))[last]}; // Last Tuesday is now last Thursday
    std::cout << (year_month_day{wdl/10/2019} ==
                  year_month_day{October/31/2019}) << '\n';
}
```


**Output:**
```
true true
```

