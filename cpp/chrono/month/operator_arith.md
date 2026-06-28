---
title: std::chrono::month::operators
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/month/operator_arith
---


```cpp
dcl|since=c++20|num=1|1=
constexpr std::chrono::month& operator+=( const std::chrono::months& m ) noexcept;
dcl|since=c++20|num=2|1=
constexpr std::chrono::month& operator-=( const std::chrono::months& m ) noexcept;
```

Adds or subtracts `m.count()` from the month value, reducing the result modulo 12 to an integer in the range .
1. Performs `1=*this = *this + m;`.
2. Performs `1=*this = *this - m;`.

## Return value

A reference to this `month` after modification.

## Notes

After a call to one of these functions,  is always `true` if no overflow occurred during the operation.

## Example


### Example

```cpp
#include <chrono>
#include <iostream>

int main()
{
    std::cout << std::boolalpha;

    std::chrono::month m{6};
    m += std::chrono::months(2);
    std::cout << (m == std::chrono::month(8)) << ' '
              << (m == std::chrono::August) << ' ';

    m -= std::chrono::months(3);
    std::cout << (m == std::chrono::month(5)) << ' '
              << (m == std::chrono::May) << ' ';

    m = std::chrono::October;
    m += std::chrono::months{8}; // ((10 += 8 == 18) % 12) == 6;
    std::cout << (m == std::chrono::June) << ' ';

    m -= std::chrono::months{std::chrono::December - std::chrono::February}; // -= 10
    // (6 -= 10) == -4; -4 % 12 == (12 - 4) == 8
    std::cout << (m == std::chrono::August) << '\n';
}
```


**Output:**
```
true true true true true true
```


## See also


| cpp/chrono/month/dsc operator_inc dec | (see dedicated page) |
| cpp/chrono/month/dsc operator_arith 2 | (see dedicated page) |

