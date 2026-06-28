---
title: std::chrono::weekday::operators
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/weekday/operator_inc_dec
---


```cpp
dcl|since=c++20|num=1|
constexpr std::chrono::weekday& operator++() noexcept;
dcl|since=c++20|num=2|
constexpr std::chrono::weekday operator++( int ) noexcept;
dcl|since=c++20|num=3|
constexpr std::chrono::weekday& operator--() noexcept;
dcl|since=c++20|num=4|
constexpr std::chrono::weekday operator--( int ) noexcept;
```

Adds or subtracts `1` from the weekday value, reducing the result modulo `7` to an integer in the range .
@1,2@ Performs }.
@3,4@ Performs }.

## Parameters

(none)

## Return value

@1,3@ A reference to this `weekday` after modification.
@2,4@ A copy of the `weekday` made before modification.

## Notes

After a call to one of these functions,  is always `true`.

## Example


### Example

```cpp
#include <cassert>
#include <chrono>
#include <iostream>

int main()
{
    std::cout << std::boolalpha;

    std::chrono::weekday wd{0}; // Sunday is 0 or 7

    --wd;
    std::cout << (wd == std::chrono::Saturday) << ' ';

    ++wd;
    std::cout << (wd == std::chrono::Sunday) << '\n';

    wd = std::chrono::weekday{13};
    assert(!wd.ok());
    wd++;
    assert(wd.ok());
}
```


**Output:**
```
true true
```


## See also


| cpp/chrono/weekday/dsc operator_arith | (see dedicated page) |
| cpp/chrono/weekday/dsc operator_arith 2 | (see dedicated page) |

