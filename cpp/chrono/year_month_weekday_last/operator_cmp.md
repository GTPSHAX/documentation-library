---
title: std::chrono::operator==(std::chrono::year_month_weekday_last)
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/year_month_weekday_last/operator_cmp
---


```cpp
**Header:** `<`chrono`>`
dcl|since=c++20|1=
constexpr bool operator==( const std::chrono::year_month_weekday_last& x,
const std::chrono::year_month_weekday_last& y ) noexcept;
```

Compares the two `year_month_weekday_last` values `x` and `y`.

## Return value

`1=x.year() == y.year() && x.month() == y.month() && x.weekday() == y.weekday()`

## Example


### Example

```cpp
#include <chrono>
#include <iostream>
using namespace std::chrono;

int main()
{
    constexpr auto ymwdl1{Tuesday[last]/11/2021};
    auto ymwdl2 = Tuesday[last]/11/2020;
    ymwdl2 += months(12);
    std::cout << std::boolalpha << (ymwdl1 == ymwdl2) << '\n';
}
```


**Output:**
```
true
```

