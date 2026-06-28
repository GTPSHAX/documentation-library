---
title: std::cosh
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/cosh
---

cpp/numeric/math/declarations
|family=cosh
|param1=num
|constexpr_since=26
|desc=Computes the hyperbolic cosine of `num`.

## Parameters


### Parameters

- `num` - floating-point or integer value

## Return value

If no errors occur, the hyperbolic cosine of `num` ($cosh(num)$, or $) is returned.
If a range error due to overflow occurs, `HUGE_VAL|+HUGE_VAL`, `+HUGE_VALF`, or `+HUGE_VALL` is returned.

## Error handling

Errors are reported as specified in `math_errhandling`.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* if the argument is ±0, 1 is returned.
* If the argument is ±∞, +∞ is returned.
* if the argument is NaN, NaN is returned.

## Notes

For the IEEE-compatible type `double`, if $, then `std::cosh(num)` overflows.

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

    std::cout << "cosh(1) = " << std::cosh(1) << '\n'
              << "cosh(-1) = " << std::cosh(-1) << '\n'
              << "log(sinh(" << x << ")+cosh(" << x << ")) = "
              << std::log(std::sinh(x) + std::cosh(x)) << '\n';

    // special values
    std::cout << "cosh(+0) = " << std::cosh(0.0) << '\n'
              << "cosh(-0) = " << std::cosh(-0.0) << '\n';

    // error handling
    errno=0;
    std::feclearexcept(FE_ALL_EXCEPT);

    std::cout << "cosh(710.5) = " << std::cosh(710.5) << '\n';

    if (errno == ERANGE)
        std::cout << "    errno == ERANGE: " << std::strerror(errno) << '\n';
    if (std::fetestexcept(FE_OVERFLOW))
        std::cout << "    FE_OVERFLOW raised\n";
}
```


**Output:**
```
cosh(1) = 1.54308
cosh(-1) = 1.54308
log(sinh(42)+cosh(42)) = 42
cosh(+0) = 1
cosh(-0) = 1
cosh(710.5) = inf
    errno == ERANGE: Numerical result out of range
    FE_OVERFLOW raised
```


## See also


| cpp/numeric/math/dsc sinh | (see dedicated page) |
| cpp/numeric/math/dsc tanh | (see dedicated page) |
| cpp/numeric/math/dsc acosh | (see dedicated page) |
| cpp/numeric/complex/dsc cosh | (see dedicated page) |
| cpp/numeric/valarray/dsc cosh | (see dedicated page) |

