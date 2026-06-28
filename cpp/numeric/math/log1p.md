---
title: std::log1p
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/log1p
---

cpp/numeric/math/declarations
|family=log1p
|param1=num
|constexpr_since=26
|desc=Computes the [Natural logarithm|natural (base-$e$) logarithm](https://en.wikipedia.org/wiki/Natural logarithm|natural (base-$e$) logarithm) of `1 + num`. This function is more precise than the expression `std::log(1 + num)` if `num` is close to zero.

## Parameters


### Parameters

- `num` - floating-point or integer value

## Return value

If no errors occur $ln(1+num)$ is returned.
If a domain error occurs, an implementation-defined value is returned (NaN where supported).
If a pole error occurs, `HUGE_VAL|-HUGE_VAL`, `-HUGE_VALF`, or `-HUGE_VALL` is returned.
If a range error occurs due to underflow, the correct result (after rounding) is returned.

## Error handling

Errors are reported as specified in `math_errhandling`.
Domain error occurs if `num` is less than $-1$.
Pole error may occur if `num` is $-1$.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* If the argument is ±0, it is returned unmodified.
* If the argument is -1, -∞ is returned and `FE_DIVBYZERO` is raised.
* If the argument is less than -1, NaN is returned and `FE_INVALID` is raised.
* If the argument is +∞, +∞ is returned.
* If the argument is NaN, NaN is returned.

## Notes

The functions `std::expm1` and `std::log1p` are useful for financial calculations, for example, when calculating small daily interest rates: $(1 + x) can be expressed as `std::expm1(n * std::log1p(x))`. These functions also simplify writing accurate inverse hyperbolic functions.

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
    std::cout << "log1p(0) = " << log1p(0) << '\n'
              << "Interest earned in 2 days on $100, compounded daily at 1%\n"
              << "    on a 30/360 calendar = "
              << 100 * expm1(2 * log1p(0.01 / 360)) << '\n'
              << "log(1+1e-16) = " << std::log(1 + 1e-16)
              << ", but log1p(1e-16) = " << std::log1p(1e-16) << '\n';

    // special values
    std::cout << "log1p(-0) = " << std::log1p(-0.0) << '\n'
              << "log1p(+Inf) = " << std::log1p(INFINITY) << '\n';

    // error handling
    errno = 0;
    std::feclearexcept(FE_ALL_EXCEPT);

    std::cout << "log1p(-1) = " << std::log1p(-1) << '\n';

    if (errno == ERANGE)
        std::cout << "    errno == ERANGE: " << std::strerror(errno) << '\n';
    if (std::fetestexcept(FE_DIVBYZERO))
        std::cout << "    FE_DIVBYZERO raised\n";
}
```


**Output:**
```
log1p(0) = 0
Interest earned in 2 days on $100, compounded daily at 1%
    on a 30/360 calendar = 0.00555563
log(1+1e-16) = 0, but log1p(1e-16) = 1e-16
log1p(-0) = -0
log1p(+Inf) = inf
log1p(-1) = -inf
    errno == ERANGE: Result too large
    FE_DIVBYZERO raised
```


## See also


| cpp/numeric/math/dsc log | (see dedicated page) |
| cpp/numeric/math/dsc log10 | (see dedicated page) |
| cpp/numeric/math/dsc log2 | (see dedicated page) |
| cpp/numeric/math/dsc expm1 | (see dedicated page) |

