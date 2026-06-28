---
title: std::chrono::operators (std::chrono::month_day)
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/month_day/operator_cmp
---


```cpp
**Header:** `<`chrono`>`
dcl|since=c++20|num=1|1=
constexpr bool operator==( const std::chrono::month_day& x,
const std::chrono::month_day& y ) noexcept;
dcl|since=c++20|num=2|1=
constexpr std::strong_ordering operator<=>( const std::chrono::month_day& x,
const std::chrono::month_day& y ) noexcept;
```

Compares two `month_day` values.

## Return value

1. `1=x.month() == y.month() && x.day() == y.day()`
2. `1=x.month() <=> y.month() != 0 ? x.month() <=> y.month() : x.day() <=> y.day()`

## Example


### Example

```cpp
#include <chrono>
#include <iostream>

int main()
{
    constexpr auto md1{std::chrono::August/15};
    constexpr auto md2{std::chrono::month(8)/std::chrono::day(15)};
    std::cout << std::boolalpha << (md1 == md2) << '\n';

    static_assert(md1 <= md2);
}
```


**Output:**
```
true
```

