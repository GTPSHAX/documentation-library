---
title: std::numeric_limits::round_style
type: Utilities
source: https://en.cppreference.com/w/cpp/types/numeric_limits/round_style
---


```cpp
dcl rev multi|until1=c++11
|dcl1=
static const std::float_round_style round_style;
|dcl2=
static constexpr std::float_round_style round_style;
```

The value of `std::numeric_limits<T>::round_style` identifies the rounding style used by the floating-point type `T` whenever a value that is not one of the exactly repesentable values of `T` is stored in an object of that type.

## Standard specializations


## Notes

These values are constants, and do not reflect the changes to the rounding made by `std::fesetround`. The changed values may be obtained from `FLT_ROUNDS` or `std::fegetround`.

## Example

The decimal value `0.1` cannot be represented by a binary floating-point type. When stored in an IEEE-754 `double`, it falls between $0x1.9999999999999*2 and $0x1.999999999999a*2. Rounding to nearest representable value results in $0x1.999999999999a*2.
Similarly, the decimal value `0.3`, which is between $0x1.3333333333333*2 and $0x1.3333333333334*2 is rounded to nearest and is stored as $0x1.3333333333333*2.

### Example

```cpp
#include <iostream>
#include <limits>

auto print(std::float_round_style frs)
{
    switch (frs)
    {
        case std::round_indeterminate:
            return "Rounding style cannot be determined";
        case std::round_toward_zero:
            return "Rounding toward zero";
        case std::round_to_nearest:
            return "Rounding toward nearest representable value";
        case std::round_toward_infinity:
            return "Rounding toward positive infinity";
        case std::round_toward_neg_infinity:
            return "Rounding toward negative infinity";
    }
    return "unknown round style";
}

int main()
{
    std::cout << std::hexfloat
              << "The decimal 0.1 is stored in a double as "
              << 0.1 << '\n'
              << "The decimal 0.3 is stored in a double as "
              << 0.3 << '\n'
              << print(std::numeric_limits<double>::round_style) << '\n';
}
```


**Output:**
```
The decimal 0.1 is stored in a double as 0x1.999999999999ap-4
The decimal 0.3 is stored in a double as 0x1.3333333333333p-2
Rounding toward nearest representable value
```


## See also


| cpp/types/numeric_limits/dsc float_round_style | (see dedicated page) |

