---
title: std::chrono::operator==(std::chrono::month_weekday)
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/month_weekday/operator_cmp
---


```cpp
**Header:** `<`chrono`>`
dcl|since=c++20|1=
constexpr bool operator==( const std::chrono::month_weekday& x,
const std::chrono::month_weekday& y ) noexcept;
```

Compares the two `month_weekday` values `x` and `y`.

## Return value

`1=x.month() == y.month() && x.weekday_indexed() == y.weekday_indexed()`

## Example


### Example

```cpp
#include <chrono>

int main()
{
    constexpr auto mwdi1{std::chrono::March/std::chrono::Friday[1]};

    constexpr auto mwdi2
    {
        std::chrono::month_weekday
        {
            std::chrono::month(3), std::chrono::weekday(5)[1]
        }
    };

    static_assert(mwdi1 == mwdi2);
}
```

