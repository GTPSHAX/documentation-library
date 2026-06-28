---
title: std::chrono::operators
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/month_day_last/operator_cmp
---


```cpp
**Header:** `<`chrono`>`
dcl|num=1|since=c++20|1=
constexpr bool operator==( const std::chrono::month_day_last& x,
const std::chrono::month_day_last& y ) noexcept;
dcl|num=2|since=c++20|1=
constexpr std::strong_ordering operator<=>( const std::chrono::month_day_last& x,
const std::chrono::month_day_last& y ) noexcept;
```

Compares the two `month_day_last` values `x` and `y`.

## Return value

1. `1=x.month() == y.month()`
2. `1=x.month() <=> y.month()`

## Example


### Example

```cpp
#include <chrono>
#include <iostream>

int main()
{
    constexpr auto mdl1{std::chrono::February/std::chrono::last};
    constexpr std::chrono::month_day_last mdl2{std::chrono::month(2)};
    std::cout << std::boolalpha << (mdl1 == mdl2) << '\n';

    static_assert(mdl1 <= mdl2);
}
```


**Output:**
```
true
```

