---
title: std::atanh
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/atanh
---

cpp/numeric/math/declarations
|family=atanh
|param1=num
|constexpr_since=26
|desc=Computes the inverse hyperbolic tangent of `num`.

## Parameters


### Parameters

- `num` - floating-point or integer value

## Return value

If no errors occur, the inverse hyperbolic tangent of `num` ($tanh, or $artanh(num)$), is returned.
If a domain error occurs, an implementation-defined value is returned (NaN where supported).
If a pole error occurs, `HUGE_VAL|±HUGE_VAL`, `±HUGE_VALF`, or `±HUGE_VALL` is returned (with the correct sign).
If a range error occurs due to underflow, the correct result (after rounding) is returned.

## Error handling

Errors are reported as specified in `math_errhandling`.
If the argument is not on the interval , a range error occurs.
If the argument is ±1, a pole error occurs.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* if the argument is ±0, it is returned unmodified.
* if the argument is ±1, ±∞ is returned and `FE_DIVBYZERO` is raised.
* if $, NaN is returned and `FE_INVALID` is raised.
* if the argument is NaN, NaN is returned.

## Notes

Although the C standard (to which C++ refers for this function) names this function "arc hyperbolic tangent", the inverse functions of the hyperbolic functions are the area functions. Their argument is the area of a hyperbolic sector, not an arc. The correct name is "inverse hyperbolic tangent" (used by POSIX) or "area hyperbolic tangent".
[https://pubs.opengroup.org/onlinepubs/9699919799/functions/atanh.html POSIX specifies] that in case of underflow, `num` is returned unmodified, and if that is not supported, an implementation-defined value no greater than `DBL_MIN`, `FLT_MIN`, and `LDBL_MIN` is returned.

## Example


### Example

```cpp
#include <cerrno>
#include <cfenv>
#include <cfloat>
#include <cmath>
#include <cstring>
#include <iostream>
// #pragma STDC FENV_ACCESS ON

int main()
{
    std::cout << "atanh(0) = " << std::atanh(0) << '\n'
              << "atanh(-0) = " << std::atanh(-0.0) << '\n'
              << "atanh(0.9) = " << std::atanh(0.9) << '\n';

    // error handling
    errno = 0;
    std::feclearexcept(FE_ALL_EXCEPT);

    std::cout << "atanh(-1) = " << std::atanh(-1) << '\n';

    if (errno == ERANGE)
        std::cout << "    errno == ERANGE: " << std::strerror(errno) << '\n';
    if (std::fetestexcept(FE_DIVBYZERO))
        std::cout << "    FE_DIVBYZERO raised\n";
}
```


**Output:**
```
atanh(0) = 0
atanh(-0) = -0
atanh(0.9) = 1.47222
atanh(-1) = -inf
    errno == ERANGE: Numerical result out of range
    FE_DIVBYZERO raised
```


## See also


| cpp/numeric/math/dsc asinh | (see dedicated page) |
| cpp/numeric/math/dsc acosh | (see dedicated page) |
| cpp/numeric/math/dsc tanh | (see dedicated page) |
| cpp/numeric/complex/dsc atanh | (see dedicated page) |


## External links

