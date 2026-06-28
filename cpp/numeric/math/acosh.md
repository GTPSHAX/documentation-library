---
title: std::acosh
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/acosh
---

cpp/numeric/math/declarations
|family=acosh
|param1=num
|constexpr_since=26
|desc=Computes the inverse hyperbolic cosine of `num`.

## Parameters


### Parameters

- `num` - floating-point or integer value

## Return value

If no errors occur, the inverse hyperbolic cosine of `num` ($cosh, or $arcosh(num)$) on the interval $[0, +∞]$, is returned.
If a domain error occurs, an implementation-defined value is returned (NaN where supported).

## Error handling

Errors are reported as specified in `math_errhandling`.
If the argument is less than 1, a domain error occurs.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* if the argument is less than 1, `FE_INVALID` is raised an NaN is returned.
* if the argument is 1, +0 is returned.
* if the argument is +∞, +∞ is returned.
* if the argument is NaN, NaN is returned.

## Notes

Although the C standard (to which C++ refers for this function) names this function "arc hyperbolic cosine", the inverse functions of the hyperbolic functions are the area functions. Their argument is the area of a hyperbolic sector, not an arc. The correct name is "inverse hyperbolic cosine" (used by POSIX) or "area hyperbolic cosine".

## Examples


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
    std::cout << "acosh(1) = " << std::acosh(1) << '\n'
              << "acosh(10) = " << std::acosh(10) << '\n'
              << "acosh(DBL_MAX) = " << std::acosh(DBL_MAX) << '\n'
              << "acosh(Inf) = " << std::acosh(INFINITY) << '\n';

    // error handling
    errno = 0;
    std::feclearexcept(FE_ALL_EXCEPT);

    std::cout << "acosh(0.5) = " << std::acosh(0.5) << '\n';

    if (errno == EDOM)
        std::cout << "    errno == EDOM: " << std::strerror(errno) << '\n';
    if (std::fetestexcept(FE_INVALID))
        std::cout << "    FE_INVALID raised\n";
}
```


**Output:**
```
acosh(1) = 0
acosh(10) = 2.99322
acosh(DBL_MAX) = 710.476
acosh(Inf) = inf
acosh(0.5) = -nan
    errno == EDOM: Numerical argument out of domain
    FE_INVALID raised
```


## See also


| cpp/numeric/math/dsc asinh | (see dedicated page) |
| cpp/numeric/math/dsc atanh | (see dedicated page) |
| cpp/numeric/math/dsc cosh | (see dedicated page) |
| cpp/numeric/complex/dsc acosh | (see dedicated page) |


## External links

