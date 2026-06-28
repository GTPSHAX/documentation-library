---
title: std::chrono::day::operators
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/day/operator_inc_dec
---


```cpp
dcl|since=c++20|num=1|
constexpr std::chrono::day& operator++() noexcept;
dcl|since=c++20|num=2|
constexpr std::chrono::day operator++( int ) noexcept;
dcl|since=c++20|num=3|
constexpr std::chrono::day& operator--() noexcept;
dcl|since=c++20|num=4|
constexpr std::chrono::day operator--( int ) noexcept;
```

Adds or subtracts 1 from the day value.
@1,2@ Performs }.
@3,4@ Performs }.

## Parameters

(none)

## Return value

@1,3@ A reference to this `day` after modification.
@2,4@ A copy of the `day` made before modification.

## Notes

If the result would be outside the range , the actual stored value is unspecified.

## Example


### Example

```cpp
#include <cassert>
#include <chrono>

int main()
{
    std::chrono::day d{15};

    ++d;
    assert(d == std::chrono::day(16));

    --d;
    assert(d == std::chrono::day(15));
}
```


## See also


| cpp/chrono/day/dsc operator_arith | (see dedicated page) |
| cpp/chrono/day/dsc operator_arith 2 | (see dedicated page) |

