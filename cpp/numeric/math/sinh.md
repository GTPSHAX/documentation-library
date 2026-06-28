---
title: std::sinh
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/sinh
---

cpp/numeric/math/declarations
|family=sinh
|param1=num
|constexpr_since=26
|desc=Computes the hyperbolic sine of `num`.

## Parameters


### Parameters

- `num` - floating-point or integer value

## Return value

If no errors occur, the hyperbolic sine of `num` ($sinh(num)$, or $) is returned.
If a range error due to overflow occurs, `HUGE_VAL|±HUGE_VAL`, `±HUGE_VALF`, or `±HUGE_VALL` is returned.
If a range error occurs due to underflow, the correct result (after rounding) is returned.

## Error handling

Errors are reported as specified in `math_errhandling`.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* if the argument is ±0 or ±∞, it is returned unmodified.
* if the argument is NaN, NaN is returned.

## Notes

[https://pubs.opengroup.org/onlinepubs/9699919799/functions/sinh.html POSIX specifies] that in case of underflow, `num` is returned unmodified, and if that is not supported, and implementation-defined value no greater than `DBL_MIN`, `FLT_MIN`, and `LDBL_MIN` is returned.

## Example


### Example

```cpp
#include <cerrno>
#include <cfenv>
#include <cmath>
#include <cstring>
#include <iostream>
// #pragma STDC FENV_ACCESS ON

int main()
{
    const double x = 42;

    std::cout << "sinh(1) = " << std::sinh(1) << '\n'
              << "sinh(-1) = " << std::sinh(-1) << '\n'
              << "log(sinh(" << x << ")+cosh(" << x << ")) = "
              << std::log(std::sinh(x) + std::cosh(x)) << '\n';

    // special values
    std::cout << "sinh(+0) = " << std::sinh(0.0) << '\n'
              << "sinh(-0) = " << std::sinh(-0.0) << '\n';

    // error handling
    errno = 0;
    std::feclearexcept(FE_ALL_EXCEPT);

    std::cout << "sinh(710.5) = " << std::sinh(710.5) << '\n';

    if (errno == ERANGE)
        std::cout << "    errno == ERANGE: " << std::strerror(errno) << '\n';
    if (std::fetestexcept(FE_OVERFLOW))
        std::cout << "    FE_OVERFLOW raised\n";
}
```


**Output:**
```
sinh(1) = 1.1752
sinh(-1) = -1.1752
log(sinh(42)+cosh(42)) = 42
sinh(+0) = 0
sinh(-0) = -0
sinh(710.5) = inf
    errno == ERANGE: Numerical result out of range
    FE_OVERFLOW raised
```


## See also


| cpp/numeric/math/dsc cosh | (see dedicated page) |
| cpp/numeric/math/dsc tanh | (see dedicated page) |
| cpp/numeric/math/dsc asinh | (see dedicated page) |
| cpp/numeric/complex/dsc sinh | (see dedicated page) |
| cpp/numeric/valarray/dsc sinh | (see dedicated page) |

