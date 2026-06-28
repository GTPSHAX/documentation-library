---
title: std::numeric_limits::traps
type: Utilities
source: https://en.cppreference.com/w/cpp/types/numeric_limits/traps
---


```cpp
dcl rev multi|until1=c++11
|dcl1=
static const bool traps;
|dcl2=
static constexpr bool traps;
```

The value of `std::numeric_limits<T>::traps` is `true` for all arithmetic types `T` that have at least one value at the start of the program that, if used as an argument to an arithmetic operation, will generate a [Trap (computing)|trap](https://en.wikipedia.org/wiki/Trap (computing)|trap).

## Standard specializations


## Notes

On most platforms integer division by zero always traps, and `std::numeric_limits<T>::traps` is `true` for all integer types that support the value `0`. The exception is the type `bool`: even though division by `false` traps due to integral promotion from `bool` to `int`, it is the zero-valued `int` that traps. Zero is not a value of type `bool`.
On most platforms, floating-point exceptions may be turned on and off at run time (e.g. `feenableexcept()` on Linux or `_controlfp` on Windows), in which case the value of `std::numeric_limits<T>::traps` for floating-point types reflects the state of floating-point trapping facility at the time of program startup, which is `false` on most modern systems. An exception would be a [DEC Alpha](https://en.wikipedia.org/wiki/DEC Alpha) program, where it is `true` if compiled without `-ieee`.

## Example


### Example

```cpp
#include <iostream>
#include <limits>

int main()
{
    std::cout << std::boolalpha
              << "bool:     traps = " << std::numeric_limits<bool>::traps << '\n'
              << "char:     traps = " << std::numeric_limits<char>::traps << '\n'
              << "char16_t: traps = " << std::numeric_limits<char16_t>::traps << '\n'
              << "long:     traps = " << std::numeric_limits<long>::traps << '\n'
              << "float:    traps = " << std::numeric_limits<float>::traps << '\n';
}
```


**Output:**
```
// GCC output:
bool:     traps = true
char:     traps = true
char16_t: traps = true
long:     traps = true
float:    traps = false

// Clang output:
bool:     traps = false
char:     traps = true
char16_t: traps = true
long:     traps = true
float:    traps = false
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-497 | C++98 | it was unclear what is returned if trapping<br>is enabled or disabled at runtime | returns the enable status<br>at the start of the program |


## See also


| cpp/types/numeric_limits/dsc tinyness_before | (see dedicated page) |
| cpp/types/numeric_limits/dsc has_denorm_loss | (see dedicated page) |

