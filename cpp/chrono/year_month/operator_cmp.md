---
title: std::chrono::operators (std::chrono::year_month)
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/year_month/operator_cmp
---


```cpp
**Header:** `<`chrono`>`
dcl|since=c++20|num=1|1=
constexpr bool operator==( const std::chrono::year_month& x,
const std::chrono::year_month& y ) noexcept;
dcl|since=c++20|num=2|1=
constexpr std::strong_ordering operator<=>( const std::chrono::year_month& x,
const std::chrono::year_month& y ) noexcept;
```

Compares the two `year_month` values `x` and `y`.

## Return value

1. `1=x.year() == y.year() && x.month() == y.month()`
2. `1=x.year() <=> y.year() != 0 ? x.year() <=> y.year() : x.month() <=> y.month()`

## Example


### Example

```cpp
#include <chrono>
#include <iostream>

int main()
{
    using namespace std::chrono;

    constexpr year_month ym1{year(2021), month(7)};
    constexpr year_month ym2{year(2021)/7};
    static_assert(ym1 == ym2);
    std::cout << ym1 << '\n';

    static_assert((2020y/1 < 2020y/2) && (2020y/2 == 2020y/2) && (2020y/3 <= 2021y/3) &&
                  (2023y/1 > 2020y/2) && (3020y/2 != 2020y/2) && (2020y/3 >= 2020y/3));
}
```


**Output:**
```
2021/Jul
```

