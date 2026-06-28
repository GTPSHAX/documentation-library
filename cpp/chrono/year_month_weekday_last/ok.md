---
title: std::chrono::year_month_weekday_last::ok
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/year_month_weekday_last/ok
---


```cpp
dcl|since=c++20|
constexpr bool ok() const noexcept;
```

Checks if this object represents a valid date. Since a `year_month_weekday_last` represents the last weekday of a particular month, it is valid as long as the year, month and weekday are valid.

## Return value

`year().ok() && month().ok() && weekday().ok()`

## Example


### Example

```cpp
#include <cassert>
#include <chrono>
using namespace std::chrono;

int main()
{
    auto ymwdl{Tuesday[last]/11/2020};
    assert(ymwdl.ok());
    ymwdl = Tuesday[last]/-2/2021;
    assert(!ymwdl.ok());
    ymwdl += months(0); // Normalize month
    assert(ymwdl.ok());
}
```

