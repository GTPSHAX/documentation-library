---
title: std::sin
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/sin
---

cpp/numeric/math/declarations
|family=sin
|param1=num
|constexpr_since=26
|desc=Computes the sine of `num` (measured in radians).

## Parameters


### Parameters

- `num` - floating-point or integer value representing angle in radians

## Return value

If no errors occur, the sine of `num` ($sin(num)$) in the range , is returned.
rrev|until=c++11|
The result may have little or no significance if the magnitude of `num` is large.
If a domain error occurs, an implementation-defined value is returned (NaN where supported).
If a range error occurs due to underflow, the correct result (after rounding) is returned.

## Error handling

Errors are reported as specified in `math_errhandling`.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* if the argument is ±0, it is returned unmodified.
* if the argument is ±∞, NaN is returned and `FE_INVALID` is raised.
* if the argument is NaN, NaN is returned.

## Notes

The case where the argument is infinite is not specified to be a domain error in C (to which C++ defers), but it is defined as a [https://pubs.opengroup.org/onlinepubs/9699919799/functions/sin.html domain error in POSIX].
POSIX also specifies that in case of underflow, `num` is returned unmodified, and if that is not supported, an implementation-defined value no greater than `DBL_MIN`, `FLT_MIN`, and `LDBL_MIN` is returned.

## Example


### Example

```cpp
#include <cerrno>
#include <cfenv>
#include <cmath>
#include <iomanip>
#include <iostream>

// #pragma STDC FENV_ACCESS ON

const double pi = std::acos(-1); // or std::numbers::pi since C++20

constexpr double your_sin(double x)
{
    double sin{0}, pow{x};
    for (auto fac{1LLU}, n{1ULL}; n != 20; fac *= ++n, pow *= x)
        if (n & 1)
            sin += (n & 2 ? -pow : pow) / fac;
    return sin;
}

int main()
{
    std::cout << std::setprecision(10) << std::showpos
              << "Typical usage:\n"
              << "std::sin(pi/6) = " << std::sin(pi / 6) << '\n'
              << "your sin(pi/6) = " << your_sin(pi / 6) << '\n'
              << "std::sin(pi/2) = " << std::sin(pi / 2) << '\n'
              << "your sin(pi/2) = " << your_sin(pi / 2) << '\n'
              << "std::sin(-3*pi/4) = " << std::sin(-3 * pi / 4) << '\n'
              << "your sin(-3*pi/4) = " << your_sin(-3 * pi / 4) << '\n'
              << "Special values:\n"
              << "std::sin(+0) = " << std::sin(0.0) << '\n'
              << "std::sin(-0) = " << std::sin(-0.0) << '\n';

    // error handling
    std::feclearexcept(FE_ALL_EXCEPT);

    std::cout << "std::sin(INFINITY) = " << std::sin(INFINITY) << '\n';
    if (std::fetestexcept(FE_INVALID))
        std::cout << "    FE_INVALID raised\n";
}
```


**Output:**
```
Typical usage:
std::sin(pi/6) = +0.5
your sin(pi/6) = +0.5
std::sin(pi/2) = +1
your sin(pi/2) = +1
std::sin(-3*pi/4) = -0.7071067812
your sin(-3*pi/4) = -0.7071067812
Special values:
std::sin(+0) = +0
std::sin(-0) = -0
std::sin(INFINITY) = -nan
    FE_INVALID raised
```


## See also


| cpp/numeric/math/dsc cos | (see dedicated page) |
| cpp/numeric/math/dsc tan | (see dedicated page) |
| cpp/numeric/math/dsc asin | (see dedicated page) |
| cpp/numeric/complex/dsc sin | (see dedicated page) |
| cpp/numeric/valarray/dsc sin | (see dedicated page) |

