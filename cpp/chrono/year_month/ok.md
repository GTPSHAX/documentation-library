---
title: std::chrono::year_month::ok
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/year_month/ok
---


```cpp
dcl|since=c++20|1=
constexpr bool ok() const noexcept;
```

Checks if the year and month values stored in this object are valid.

## Return value

`year().ok() && month().ok()`

## Example


### Example

```cpp
#include <chrono>
using namespace std::chrono_literals;

int main()
{
    constexpr std::chrono::year_month ym1{3030y, std::chrono::July};
    static_assert(ym1.ok());

    constexpr std::chrono::year_month ym2{std::chrono::year(2020)/16};
    static_assert(!ym2.ok());
}
```

