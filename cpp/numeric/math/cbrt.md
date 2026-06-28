---
title: std::cbrt
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/cbrt
---

cpp/numeric/math/declarations
|family=cbrt
|param1=num
|constexpr_since=26
|desc=Computes the cube root of `num`.

## Parameters


### Parameters

- `num` - floating-point or integer value

## Return value

If no errors occur, the cube root of `num` (mathjax-or|1=\(\small{\sqrt[3]{num} }\)|2=), is returned.
If a range error occurs due to underflow, the correct result (after rounding) is returned.

## Error handling

Errors are reported as specified in `math_errhandling`.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* if the argument is ±0 or ±∞, it is returned, unchanged.
* if the argument is NaN, NaN is returned.

## Notes

`std::cbrt(num)` is not equivalent to `std::pow(num, 1.0 / 3)` because the rational number mathjax-or|1=\(\small{\frac1{3} }\)|2=  is typically not equal to `1.0 / 3` and `std::pow` cannot raise a negative base to a fractional exponent. Moreover, `std::cbrt(num)` usually gives more accurate results than `std::pow(num, 1.0 / 3)` (see example).

## Example


### Example

```cpp
#include <cmath>
#include <iomanip>
#include <iostream>
#include <limits>

int main()
{
    std::cout
        << "Normal use:\n"
        << "cbrt(729)       = " << std::cbrt(729) << '\n'
        << "cbrt(-0.125)    = " << std::cbrt(-0.125) << '\n'
        << "Special values:\n"
        << "cbrt(-0)        = " << std::cbrt(-0.0) << '\n'
        << "cbrt(+inf)      = " << std::cbrt(INFINITY) << '\n'
        << "Accuracy and comparison with `pow`:\n"
        << std::setprecision(std::numeric_limits<double>::max_digits10)
        << "cbrt(343)       = " << std::cbrt(343) << '\n'
        << "pow(343,1.0/3)  = " << std::pow(343, 1.0 / 3) << '\n'
        << "cbrt(-343)      = " << std::cbrt(-343) << '\n'
        << "pow(-343,1.0/3) = " << std::pow(-343, 1.0 / 3) << '\n';
}
```


**Output:**
```
Normal use:
cbrt(729)       = 9
cbrt(-0.125)    = -0.5
Special values:
cbrt(-0)        = -0
cbrt(+inf)      = inf
Accuracy and comparison with `pow`:
cbrt(343)       = 7
pow(343,1.0/3)  = 6.9999999999999991
cbrt(-343)      = -7
pow(-343,1.0/3) = -nan
```


## See also


| cpp/numeric/math/dsc pow | (see dedicated page) |
| cpp/numeric/math/dsc sqrt | (see dedicated page) |
| cpp/numeric/math/dsc hypot | (see dedicated page) |

