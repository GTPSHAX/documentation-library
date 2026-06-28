---
title: std::numeric_limits::tinyness_before
type: Utilities
source: https://en.cppreference.com/w/cpp/types/numeric_limits/tinyness_before
---


```cpp
dcl rev multi|until1=c++11
|dcl1=
static const bool tinyness_before;
|dcl2=
static constexpr bool tinyness_before;
```

The value of `std::numeric_limits<T>::tinyness_before` is `true` for all floating-point types `T` that test results of floating-point expressions for underflow before rounding.

## Standard specializations


## Notes

Standard-compliant IEEE 754 floating-point implementations are required to detect the floating-point underflow, and have two alternative situations where this can be done
# Underflow occurs (and `FE_UNDERFLOW` may be raised) if a computation produces a result whose absolute value, computed as though both the exponent range and the precision were unbounded, is smaller than `std::numeric_limits<T>::min()`. Such implementation detects tinyness before rounding (e.g. UltraSparc, POWER).
# Underflow occurs (and `FE_UNDERFLOW` may be raised) if after the rounding of the result to the target floating-point type (that is, rounding to `std::numeric_limits<T>::digits` bits), the result's absolute value is smaller than `std::numeric_limits<T>::min()`. Formally, the absolute value of a nonzero result computed as though the exponent range were unbounded is smaller than `std::numeric_limits<T>::min()`. Such implementation detects tinyness after rounding (e.g. SuperSparc).

## Example


### Example

```cpp
#include <iostream>
#include <limits>
#include <cmath>
#include <cfenv>

int main()
{
    std::cout << "Tinyness before: " << std::boolalpha
              << std::numeric_limits<double>::tinyness_before << '\n';

    double denorm_max = std::nextafter(std::numeric_limits<double>::min(), 0);
    double multiplier = 1 + std::numeric_limits<double>::epsilon();

    std::feclearexcept(FE_ALL_EXCEPT);

    double result = denorm_max * multiplier; // Underflow only if tinyness_before

    if (std::fetestexcept(FE_UNDERFLOW))
        std::cout << "Underflow detected\n";

    std::cout << std::hexfloat << denorm_max << " x " << multiplier  <<  " = "
              << result << '\n';
}
```


**Output:**
```
Tinyness before: true
Underflow detected
0xf.ffffffffffffp-1030 x 0x1.0000000000001p+0 = 0x1p-1022
```


## See also


| cpp/types/numeric_limits/dsc has_denorm_loss | (see dedicated page) |
| cpp/types/numeric_limits/dsc has_denorm | (see dedicated page) |

