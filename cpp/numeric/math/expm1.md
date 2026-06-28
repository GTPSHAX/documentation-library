---
title: std::expm1
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/expm1
---

cpp/numeric/math/declarations
|family=expm1
|param1=num
|constexpr_since=26
|desc=Computes the $e$ ([E (mathematical_constant)|Euler's number](https://en.wikipedia.org/wiki/E (mathematical_constant)|Euler's number), `2.7182818...`) raised to the given power `num`, minus `1.0`. This function is more accurate than the expression `std::exp(num) - 1.0` if `num` is close to zero.

## Parameters


### Parameters

- `num` - floating-point or integer value

## Return value

If no errors occur $e is returned.
If a range error due to overflow occurs, `HUGE_VAL|+HUGE_VAL`, `+HUGE_VALF`, or `+HUGE_VALL` is returned.
If a range error occurs due to underflow, the correct result (after rounding) is returned.

## Error handling

Errors are reported as specified in `math_errhandling`.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* If the argument is ±0, it is returned, unmodified.
* If the argument is -∞, -1 is returned.
* If the argument is +∞, +∞ is returned.
* If the argument is NaN, NaN is returned.

## Notes

The functions `std::expm1` and `std::log1p` are useful for financial calculations, for example, when calculating small daily interest rates: $(1+x) can be expressed as `std::expm1(n * std::log1p(x))`. These functions also simplify writing accurate inverse hyperbolic functions.
For IEEE-compatible type `double`, overflow is guaranteed if $709.8 < num$.

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
    std::cout << "expm1(1) = " << std::expm1(1) << '\n'
              << "Interest earned in 2 days on $100, compounded daily at 1%\n"
              << "    on a 30/360 calendar = "
              << 100 * std::expm1(2 * std::log1p(0.01 / 360)) << '\n'
              << "exp(1e-16)-1 = " << std::exp(1e-16) - 1
              << ", but expm1(1e-16) = " << std::expm1(1e-16) << '\n';

    // special values
    std::cout << "expm1(-0) = " << std::expm1(-0.0) << '\n'
              << "expm1(-Inf) = " << std::expm1(-INFINITY) << '\n';

    // error handling
    errno = 0;
    std::feclearexcept(FE_ALL_EXCEPT);

    std::cout << "expm1(710) = " << std::expm1(710) << '\n';

    if (errno == ERANGE)
        std::cout << "    errno == ERANGE: " << std::strerror(errno) << '\n';
    if (std::fetestexcept(FE_OVERFLOW))
        std::cout << "    FE_OVERFLOW raised\n";
}
```


**Output:**
```
expm1(1) = 1.71828
Interest earned in 2 days on $100, compounded daily at 1%
    on a 30/360 calendar = 0.00555563
exp(1e-16)-1 = 0, but expm1(1e-16) = 1e-16
expm1(-0) = -0
expm1(-Inf) = -1
expm1(710) = inf
    errno == ERANGE: Result too large
    FE_OVERFLOW raised
```


## See also


| cpp/numeric/math/dsc exp | (see dedicated page) |
| cpp/numeric/math/dsc exp2 | (see dedicated page) |
| cpp/numeric/math/dsc log1p | (see dedicated page) |

