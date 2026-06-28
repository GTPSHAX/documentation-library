---
title: std::cos
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/cos
---

cpp/numeric/math/declarations
|family=cos
|param1=num
|constexpr_since=26
|desc=Computes the cosine of `num` (measured in radians).

## Parameters


### Parameters

- `num` - floating-point or integer value representing angle in radians

## Return value

If no errors occur, the cosine of `num` ($cos(num)$) in the range , is returned.
rrev|until=c++11|
The result may have little or no significance if the magnitude of `num` is large.
If a domain error occurs, an implementation-defined value is returned (NaN where supported).
If a range error occurs due to underflow, the correct result (after rounding) is returned.

## Error handling

Errors are reported as specified in `math_errhandling`.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* if the argument is ±0, the result is `1.0`.
* if the argument is ±∞, NaN is returned and `FE_INVALID` is raised.
* if the argument is NaN, NaN is returned.

## Notes

The case where the argument is infinite is not specified to be a domain error in C, but it is defined as a [https://pubs.opengroup.org/onlinepubs/9699919799/functions/cos.html domain error in POSIX].

## Example


### Example

```cpp
#include <cerrno>
#include <cfenv>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <numbers>

// #pragma STDC FENV_ACCESS ON

constexpr double pi = std::numbers::pi; // or std::acos(-1) before C++20

constexpr double your_cos(double x)
{
    double cos{1}, pow{x};
    for (auto fac{1ull}, n{1ull}; n != 19; fac *= ++n, pow *= x)
        if ((n & 1) == 0)
            cos += (n & 2 ? -pow : pow) / fac;
    return cos;
}

int main()
{
    std::cout << std::setprecision(10) << std::showpos
              << "Typical usage:\n"
              << "std::cos(pi/3) = " << std::cos(pi / 3) << '\n'
              << "your cos(pi/3) = " << your_cos(pi / 3) << '\n'
              << "std::cos(pi/2) = " << std::cos(pi / 2) << '\n'
              << "your cos(pi/2) = " << your_cos(pi / 2) << '\n'
              << "std::cos(-3*pi/4) = " << std::cos(-3 * pi / 4) << '\n'
              << "your cos(-3*pi/4) = " << your_cos(-3 * pi / 4) << '\n'
              << "Special values:\n"
              << "std::cos(+0) = " << std::cos(0.0) << '\n'
              << "std::cos(-0) = " << std::cos(-0.0) << '\n';

    // error handling
    std::feclearexcept(FE_ALL_EXCEPT);

    std::cout << "cos(INFINITY) = " << std::cos(INFINITY) << '\n';
    if (std::fetestexcept(FE_INVALID))
        std::cout << "    FE_INVALID raised\n";
}
```


**Output:**
```
Typical usage:
std::cos(pi/3) = +0.5
your cos(pi/3) = +0.5
std::cos(pi/2) = +6.123233996e-17
your cos(pi/2) = -3.373452105e-15
std::cos(-3*pi/4) = -0.7071067812
your cos(-3*pi/4) = -0.7071067812
Special values:
std::cos(+0) = +1
std::cos(-0) = +1
cos(INFINITY) = -nan
    FE_INVALID raised
```


## See also


| cpp/numeric/math/dsc sin | (see dedicated page) |
| cpp/numeric/math/dsc tan | (see dedicated page) |
| cpp/numeric/math/dsc acos | (see dedicated page) |
| cpp/numeric/complex/dsc cos | (see dedicated page) |
| cpp/numeric/valarray/dsc cos | (see dedicated page) |

