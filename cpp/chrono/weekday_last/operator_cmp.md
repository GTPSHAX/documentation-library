---
title: std::chrono::operator==(std::chrono::weekday_last)
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/weekday_last/operator_cmp
---


```cpp
**Header:** `<`chrono`>`
dcl|since=c++20|1=
constexpr bool operator==( const std::chrono::weekday_last& x,
const std::chrono::weekday_last& y ) noexcept;
```

Compares the two `weekday_last` values `x` and `y`.

## Return value

`1=x.weekday() == y.weekday()`

## Example


### Example

```cpp
#include <chrono>
#include <iostream>

int main()
{
    constexpr auto wdl1{std::chrono::Tuesday[std::chrono::last]};
    constexpr std::chrono::weekday_last wdl2{std::chrono::weekday(2)};
    std::cout << std::boolalpha
              << (wdl1 == wdl2) << ' '
              << (wdl1 == std::chrono::Wednesday[std::chrono::last]) << '\n';
}
```


**Output:**
```
true false
```

