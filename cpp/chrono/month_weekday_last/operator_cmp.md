---
title: std::chrono::operator==(std::chrono::month_weekday_last)
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/month_weekday_last/operator_cmp
---

ddcl|header=chrono|since=c++20|1=
constexpr bool operator==( const std::chrono::month_weekday_last& x,
const std::chrono::month_weekday_last& y ) noexcept;
Compares the two `month_weekday_last` values `x` and `y`.

## Return value

`1=x.month() == y.month() && x.weekday_last() == y.weekday_last()`

## Example


### Example

```cpp
#include <chrono>

int main()
{
    constexpr std::chrono::month_weekday_last mwdl1
    {
        std::chrono::March/std::chrono::Friday[std::chrono::last]
    };

    constexpr std::chrono::month_weekday_last mwdl2
    {
        std::chrono::March, std::chrono::Friday[std::chrono::last]
    };

    static_assert(mwdl1 == mwdl2);
}
```

