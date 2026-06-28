---
title: std::exp
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/exp
---

cpp/numeric/math/declarations
|family=exp
|param1=num
|constexpr_since=26
|desc=Computes $e$ ([E (mathematical constant)|Euler's number](https://en.wikipedia.org/wiki/E (mathematical constant)|Euler's number), ) raised to the given power `num`.

## Parameters


### Parameters

- `num` - floating-point or integer value

## Return value

If no errors occur, the base-$e$ exponential of `num` ($e) is returned.
If a range error occurs due to overflow, `HUGE_VAL|+HUGE_VAL`, `+HUGE_VALF`, or `+HUGE_VALL` is returned.
If a range error occurs due to underflow, the correct result (after rounding) is returned.

## Error handling

Errors are reported as specified in `math_errhandling`.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* If the argument is ±0, 1 is returned.
* If the argument is -∞, +0 is returned.
* If the argument is +∞, +∞ is returned.
* If the argument is NaN, NaN is returned.

## Notes

For IEEE-compatible type `double`, overflow is guaranteed if $709.8 < num$, and underflow is guaranteed if $num < -708.4$.

## Example


### Example

```cpp
#include <cerrno>
#include <cfenv>
#include <cmath>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <numbers>

// #pragma STDC FENV_ACCESS ON

consteval double approx_e()
{
    long double e{1.0};
    for (auto fac{1ull}, n{1llu}; n != 18; ++n, fac *= n)
        e += 1.0 / fac;
    return e;
}

int main()
{
    std::cout << std::setprecision(16)
              << "exp(1) = e¹ = " << std::exp(1) << '\n'
              << "numbers::e  = " << std::numbers::e << '\n'
              << "approx_e    = " << approx_e() << '\n'
              << "FV of $100, continuously compounded at 3% for 1 year = "
              << std::setprecision(6) << 100 * std::exp(0.03) << '\n';

    // special values
    std::cout << "exp(-0) = " << std::exp(-0.0) << '\n'
              << "exp(-Inf) = " << std::exp(-INFINITY) << '\n';

    // error handling 
    errno = 0;
    std::feclearexcept(FE_ALL_EXCEPT);

    std::cout << "exp(710) = " << std::exp(710) << '\n';

    if (errno == ERANGE)
        std::cout << "    errno == ERANGE: " << std::strerror(errno) << '\n';
    if (std::fetestexcept(FE_OVERFLOW))
        std::cout << "    FE_OVERFLOW raised\n";
}
```


**Output:**
```
exp(1) = e¹ = 2.718281828459045
numbers::e  = 2.718281828459045
approx_e    = 2.718281828459045
FV of $100, continuously compounded at 3% for 1 year = 103.045
exp(-0) = 1
exp(-Inf) = 0
exp(710) = inf
    errno == ERANGE: Numerical result out of range
    FE_OVERFLOW raised
```


## See also


| cpp/numeric/math/dsc exp2 | (see dedicated page) |
| cpp/numeric/math/dsc expm1 | (see dedicated page) |
| cpp/numeric/math/dsc log | (see dedicated page) |
| cpp/numeric/complex/dsc exp | (see dedicated page) |
| cpp/numeric/valarray/dsc exp | (see dedicated page) |

