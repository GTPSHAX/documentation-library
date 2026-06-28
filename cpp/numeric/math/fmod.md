---
title: std::fmod
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/fmod
---

cpp/numeric/math/declarations
|family=fmod
|param1=x
|param2=y
|constexpr_since=23
|desc=Computes the floating-point remainder of the division operation `x / y`.
The floating-point remainder of the division operation `x / y` calculated by this function is exactly the value `x - iquot * y`, where `iquot` is `x / y` with its fractional part truncated.
The returned value has the same sign as `x` and is less than `y` in magnitude.

## Parameters


### Parameters

- `x, y` - floating-point or integer values

## Return value

If successful, returns the floating-point remainder of the division `x / y` as defined above.
If a domain error occurs, an implementation-defined value is returned (NaN where supported).
If a range error occurs due to underflow, the correct result (after rounding) is returned.

## Error handling

Errors are reported as specified in `math_errhandling`.
Domain error may occur if `y` is zero.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* If `x` is ±0 and `y` is not zero, ±0 is returned.
* If `x` is ±∞ and `y` is not NaN, NaN is returned and `FE_INVALID` is raised.
* If `y` is ±0 and `x` is not NaN, NaN is returned and `FE_INVALID` is raised.
* If `y` is ±∞ and `x` is finite, `x` is returned.
* If either argument is NaN, NaN is returned.

## Notes

[https://pubs.opengroup.org/onlinepubs/9699919799/functions/fmod.html POSIX requires] that a domain error occurs if `x` is infinite or `y` is zero.
`std::fmod`, but not `std::remainder` is useful for doing silent wrapping of floating-point types to unsigned integer types: `1=(0.0 <= (y = std::fmod(std::rint(x), 65536.0)) ? y : 65536.0 + y)` is in the range , which corresponds to `unsigned short`, but `std::remainder(std::rint(x), 65536.0` is in the range , which is outside of the range of `signed short`.
The `double` version of `std::fmod` behaves as if implemented as follows:

```cpp
double fmod(double x, double y)
{
#pragma STDC FENV_ACCESS ON
    double result = std::remainder(std::fabs(x), y = std::fabs(y));
    if (std::signbit(result))
        result += y;
    return std::copysign(result, x);
}
```

The expression `x - std::trunc(x / y) * y` may not equal `std::fmod(x, y)`, when the rounding of `x / y` to initialize the argument of `std::trunc` loses too much precision (example: `1=x = 30.508474576271183309`, `1=y = 6.1016949152542370172`).

## Example


### Example

```cpp
#include <cfenv>
#include <cmath>
#include <iostream>
// #pragma STDC FENV_ACCESS ON

int main()
{
    std::cout << "fmod(+5.1, +3.0) = " << std::fmod(5.1, 3) << '\n'
              << "fmod(-5.1, +3.0) = " << std::fmod(-5.1, 3) << '\n'
              << "fmod(+5.1, -3.0) = " << std::fmod(5.1, -3) << '\n'
              << "fmod(-5.1, -3.0) = " << std::fmod(-5.1, -3) << '\n';

    // special values
    std::cout << "fmod(+0.0, 1.0) = " << std::fmod(0, 1) << '\n'
              << "fmod(-0.0, 1.0) = " << std::fmod(-0.0, 1) << '\n'
              << "fmod(5.1, Inf) = " << std::fmod(5.1, INFINITY) << '\n';

    // error handling
    std::feclearexcept(FE_ALL_EXCEPT);
    std::cout << "fmod(+5.1, 0) = " << std::fmod(5.1, 0) << '\n';
    if (std::fetestexcept(FE_INVALID))
        std::cout << "    FE_INVALID raised\n";
}
```


**Output:**
```
fmod(+5.1, +3.0) = 2.1
fmod(-5.1, +3.0) = -2.1
fmod(+5.1, -3.0) = 2.1
fmod(-5.1, -3.0) = -2.1
fmod(+0.0, 1.0) = 0
fmod(-0.0, 1.0) = -0
fmod(5.1, Inf) = 5.1
fmod(+5.1, 0) = -nan
    FE_INVALID raised
```


## See also


| cpp/numeric/math/dsc div | (see dedicated page) |
| cpp/numeric/math/dsc remainder | (see dedicated page) |
| cpp/numeric/math/dsc remquo | (see dedicated page) |

