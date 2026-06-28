---
title: std::chrono::operator==(std::chrono::weekday_indexed)
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/weekday_indexed/operator_cmp
---

ddcl|header=chrono|since=c++20|1=
constexpr bool operator==( const std::chrono::weekday_indexed& x,
const std::chrono::weekday_indexed& y ) noexcept;
Compares the two `weekday_indexed` `x` and `y`.

## Return value

`1=x.weekday() == y.weekday() && x.index() == y.index()`

## Example


### Example

```cpp
#include <chrono>

int main()
{
    constexpr std::chrono::weekday_indexed wdi1{std::chrono::Wednesday[2]};
    constexpr std::chrono::weekday_indexed wdi2{std::chrono::weekday(3), 2};
    static_assert(wdi1 == wdi2);
}
```

