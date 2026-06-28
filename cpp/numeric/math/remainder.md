---
title: std::remainder
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/remainder
---

cpp/numeric/math/declarations
|family=remainder
|param1=x
|param2=y
|constexpr_since=23
|desc=Computes the IEEE remainder of the floating point division operation `x / y`.
The IEEE floating-point remainder of the division operation `x / y` calculated by this function is exactly the value `x - quo * y`, where the value `quo` is the integral value nearest the exact value `x / y`. When $, the value `quo` is chosen to be even.
In contrast to `std::fmod`, the returned value is not guaranteed to have the same sign as `x`.
If the returned value is zero, it will have the same sign as `x`.

## Parameters


### Parameters

- `x, y` - floating-point or integer values

## Return value

If successful, returns the IEEE floating-point remainder of the division `x / y` as defined above.
If a domain error occurs, an implementation-defined value is returned (NaN where supported).
If a range error occurs due to underflow, the correct result is returned.
If `y` is zero, but the domain error does not occur, zero is returned.

## Error handling

Errors are reported as specified in `math_errhandling`.
Domain error may occur if `y` is zero.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* The current rounding mode has no effect.
* `FE_INEXACT` is never raised, the result is always exact.
* If `x` is ±∞ and `y` is not NaN, NaN is returned and `FE_INVALID` is raised.
* If `y` is ±0 and `x` is not NaN, NaN is returned and `FE_INVALID` is raised.
* If either argument is NaN, NaN is returned.

## Notes

[https://pubs.opengroup.org/onlinepubs/9699919799/functions/remainder.html POSIX requires] that a domain error occurs if `x` is infinite or `y` is zero.
`std::fmod`, but not `std::remainder` is useful for doing silent wrapping of floating-point types to unsigned integer types: `1=(0.0 <= (y = std::fmod(std::rint(x), 65536.0))) ? y : 65536.0 + y` is in the range , which corresponds to `unsigned short`, but `std::remainder(std::rint(x), 65536.0)` is in the range , which is outside of the range of `signed short`.

## Example


### Example

```cpp
#include <cfenv>
#include <cmath>
#include <iostream>
// #pragma STDC FENV_ACCESS ON

int main()
{
    std::cout << "remainder(+5.1, +3.0) = " << std::remainder(5.1, 3) << '\n'
              << "remainder(-5.1, +3.0) = " << std::remainder(-5.1, 3) << '\n'
              << "remainder(+5.1, -3.0) = " << std::remainder(5.1, -3) << '\n'
              << "remainder(-5.1, -3.0) = " << std::remainder(-5.1, -3) << '\n';

    // special values
    std::cout << "remainder(-0.0, 1.0) = " << std::remainder(-0.0, 1) << '\n'
              << "remainder(5.1, Inf) = " << std::remainder(5.1, INFINITY) << '\n';

    // error handling
    std::feclearexcept(FE_ALL_EXCEPT);
    std::cout << "remainder(+5.1, 0) = " << std::remainder(5.1, 0) << '\n';
    if (fetestexcept(FE_INVALID))
        std::cout << "    FE_INVALID raised\n";
}
```


**Output:**
```
remainder(+5.1, +3.0) = -0.9
remainder(-5.1, +3.0) = 0.9
remainder(+5.1, -3.0) = -0.9
remainder(-5.1, -3.0) = 0.9
remainder(-0.0, 1.0) = -0
remainder(5.1, Inf) = 5.1
remainder(+5.1, 0) = -nan
    FE_INVALID raised
```


## See also


| cpp/numeric/math/dsc div | (see dedicated page) |
| cpp/numeric/math/dsc fmod | (see dedicated page) |
| cpp/numeric/math/dsc remquo | (see dedicated page) |

