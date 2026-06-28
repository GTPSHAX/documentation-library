---
title: std::chrono::operator==(std::chrono::year_month_weekday)
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/year_month_weekday/operator_cmp
---


```cpp
**Header:** `<`chrono`>`
dcl|since=c++20|1=
constexpr bool operator==( const std::chrono::year_month_weekday& x,
const std::chrono::year_month_weekday& y ) noexcept;
```

Compares the two `year_month_weekday` values `x` and `y`.

## Return value

`1=x.year() == y.year() && x.month() == y.month() && x.weekday_indexed() == y.weekday_indexed()`

## Example


### Example

```cpp
#include <chrono>
#include <iostream>
using namespace std::chrono;

int main()
{
    constexpr auto ymwdi1{Wednesday[1]/January/2021};
    constexpr year_month_weekday ymwdi2{year(2021), month(1), weekday(3)[1]};
    std::cout << std::boolalpha << (ymwdi1 == ymwdi2) << '\n';
}
```


**Output:**
```
true
```

