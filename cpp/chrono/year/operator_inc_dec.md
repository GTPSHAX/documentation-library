---
title: std::chrono::year::operators
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/year/operator_inc_dec
---


```cpp
dcl|since=c++20|num=1|
constexpr std::chrono::year& operator++() noexcept;
dcl|since=c++20|num=2|
constexpr std::chrono::year operator++( int ) noexcept;
dcl|since=c++20|num=3|
constexpr std::chrono::year& operator--() noexcept;
dcl|since=c++20|num=4|
constexpr std::chrono::year operator--( int ) noexcept;
```

Adds or subtracts 1 from the year value.
@1,2@ Performs }.
@3,4@ Performs }.

## Parameters

(none)

## Return value

@1,3@ A reference to this `year` after modification.
@2,4@ A copy of the `year` made before modification.

## Notes

If the result would be outside the range , the actual stored value is unspecified.

## Example


### Example

```cpp
#include <chrono>
#include <iostream>

int main()
{
    std::cout << std::boolalpha;

    std::chrono::year y{2020};
    std::cout << (++y == std::chrono::year(2021)) << ' ';
    std::cout << (--y == std::chrono::year(2020)) << '\n';

    using namespace std::literals::chrono_literals;
    y = 32767y;
    y++; //← unspecified, see ↑ Notes ↑
    std::cout << static_cast<int>(y) << '\n';
}
```


**Output:**
```
true true
-32768
```


## See also


| cpp/chrono/year/dsc operator_arith | (see dedicated page) |
| cpp/chrono/year/dsc operator_arith 2 | (see dedicated page) |

