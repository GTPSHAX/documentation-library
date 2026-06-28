---
title: std::chrono::operators (std::chrono::year)
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/year/operator_cmp
---


```cpp
**Header:** `<`chrono`>`
dcl|since=c++20|num=1|1=
constexpr bool operator==( const std::chrono::year& x,
const std::chrono::year& y ) noexcept;
dcl|since=c++20|num=2|1=
constexpr std::strong_ordering operator<=>( const std::chrono::year& x,
const std::chrono::year& y ) noexcept;
```

Compare the two `std::chrono::year` `x` and `y`.

## Return value

1. `1=int(x) == int(y)`
2. `1=int(x) <=> int(y)`

## Example


### Example

```cpp
#include <chrono>
#include <iostream>

int main()
{
    using namespace std::chrono;

    constexpr year y1{2020};
    constexpr year y2{2021};

    std::cout << std::boolalpha << (y1 != y2) << '\n';

    static_assert((2020y < 2023y) && (2020y == 2020y) && (2020y <= 2023y) &&
                  (2023y > 2020y) && (2023y != 2020y) && (2023y >= 2020y));
}
```


**Output:**
```
true
```

