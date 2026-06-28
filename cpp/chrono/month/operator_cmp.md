---
title: std::chrono::operators (std::chrono::month)
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/month/operator_cmp
---


```cpp
**Header:** `<`chrono`>`
dcl|since=c++20|num=1|1=
constexpr bool operator==( const std::chrono::month& x,
const std::chrono::month& y ) noexcept;
dcl|since=c++20|num=2|1=
constexpr std::strong_ordering operator<=>( const std::chrono::month& x,
const std::chrono::month& y ) noexcept;
```

Compare the two `std::chrono::month` `x` and `y`.

## Return value

1. `1=unsigned(x) == unsigned(y)`
2. `1=unsigned(x) <=> unsigned(y)`

## Example


### Example

```cpp
#include <chrono>

int main()
{
    constexpr std::chrono::month m1{6}, m2{8};

    static_assert
    (
        m1 < m2 && m1 == m1 && m1 <= m2 &&
        m2 > m1 && m2 != m1 && m2 >= m1 &&
        m1 <=> m2 != 0
    );
}
```

