---
title: std::chrono::operators (std::chrono::day)
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/day/operator_cmp
---


```cpp
**Header:** `<`chrono`>`
dcl|since=c++20|num=1|1=
constexpr bool operator==( const std::chrono::day& x,
const std::chrono::day& y ) noexcept;
dcl|since=c++20|num=2|1=
constexpr std::strong_ordering operator<=>( const std::chrono::day& x,
const std::chrono::day& y ) noexcept;
```

Compare the two `std::chrono::day` `x` and `y`.

## Return value

1. `1=unsigned(x) == unsigned(y)`
2. `1=unsigned(x) <=> unsigned(y)`

## Example


### Example

```cpp
#include <chrono>
#include <iostream>

int main()
{
    constexpr std::chrono::day x{13}, y{31};
    static_assert(x != y);

    if constexpr (constexpr auto res = x <=> y; res < 0)
        std::cout << "x is less than y\n";
    else if constexpr (res > 0)
        std::cout << "x is greater than y\n";
    else
        std::cout << "x and y are equal\n";

    using namespace std::literals::chrono_literals;

    static_assert
    (
        (6d < 9d) && (6d == 6d) && (6d <= 9d) &&
        (9d > 6d) && (9d != 6d) && (9d >= 6d)
    );
}
```


**Output:**
```
x is less than y
```

